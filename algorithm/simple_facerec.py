import face_recognition
import os
import glob
import numpy as np
import cv2
import pickle
import traceback

# with open('outfile', 'wb') as fp:
#     pickle.dump(my_list, fp)

# with open ('outfile', 'rb') as fp:
#     itemlist = pickle.load(fp)

def extract_text(s):
    res = ''
    for i in s:
        if i.isalpha():
            res += str(i)
    return res

class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        self.known_face_professions = []
        # self.known_face_screen_names = []

        # Resize frame for a faster speed
        self.frame_resizing = 0.25
    
    def write_data_file(self, images_path):
        try:
            #Load images encodings if available
            print("{} encoding images found.".format(len(images_path)))
            print(images_path)
            # Store image encoding and names
            for img_path in images_path:
                # print(img_path)
                img = cv2.imread(img_path)
                rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                # Get the filename only from the initial file path.
                basename = os.path.basename(img_path)
                (filename, ext) = os.path.splitext(basename)
                # Get encoding
                # face_encoding returns the 128 measurement of face
                global img_encoding
                if len(face_recognition.face_encodings(rgb_img)) > 0:
                    img_encoding = face_recognition.face_encodings(rgb_img)[0]
                else:
                    continue
                # Store file name and file encoding and person profession
                self.known_face_encodings.append(img_encoding)

                lst_file_name_split = filename.split()
            
                # self.known_face_screen_names.append(lst_file_name_split[len(lst_file_name_split) - 1])

                lst_idx = len(lst_file_name_split)-1
                if lst_file_name_split[lst_idx].isnumeric():
                    lst_idx -= 1
                    self.known_face_professions.append(lst_file_name_split[lst_idx])
                else:
                    actor = extract_text(lst_file_name_split[lst_idx])
                    self.known_face_professions.append(actor)


                lst_file_name_split = lst_file_name_split[0:lst_idx]
                self.known_face_names.append(' '.join(lst_file_name_split))

            print('1.face_names : ', self.known_face_names)
            print('1.face_professions : ', self.known_face_professions)
            # print('1.face_screen_name : ', self.known_face_screen_names)
            print("Encoding images loaded")
            
            with open('encodings\\face_encoding_file', 'wb') as fp1, open('encodings\\face_name_file', 'wb') as fp2, open('encodings\\face_profession_file', 'wb') as fp3:
                pickle.dump(self.known_face_encodings, fp1)
                pickle.dump(self.known_face_names, fp2)
                pickle.dump(self.known_face_professions, fp3)
            return True
                
        except Exception as e:
            print(e)
            return False

    def load_old_data_from_file(self):
        try:
            with open('encodings\\face_encoding_file', 'rb') as fp1, open('encodings\\face_name_file', 'rb') as fp2, open('encodings\\face_profession_file', 'rb') as fp3:
                    self.known_face_encodings = pickle.load(fp1)
                    self.known_face_names = pickle.load(fp2)
                    self.known_face_professions = pickle.load(fp3)

        except Exception:
            traceback.print_exc()
            pass


    def load_encoding_images(self):
        """
        Load encoding images from path
        :param images_path:
        :return:
        """
        self.load_old_data_from_file()
        # print(len(self.known_face_names), self.known_face_names)
        # images_path = glob.glob(os.path.join(images_path, "*.*")) 
        # images_path.sort(key = os.path.getmtime)

        #If files are empty initial loading
        if len(self.known_face_encodings) == 0 and len(self.known_face_names) == 0 and len(self.known_face_professions) == 0:
            print('No Images')
            # self.write_data_file(images_path)
        # If no image is added or deleted
        # elif len(images_path) == len(self.known_face_encodings):
        #     print('Already known faces')
            # print('images path len : ' + str(len(images_path)))
            # print('2.face_names : ', self.known_face_names)
            # print('2.face_professions : ', self.known_face_professions)
            # print(len(self.known_face_encodings), len(self.known_face_names), len(self.known_face_professions))
            # print('2.images_path', images_path)
            # pass
        # If new image added or deleted
        # else:
        #     print('new image added or deleted')
            # print(images_path, len(images_path))
            # print('There is some changes in images')
            # print(len(self.known_face_names))
            # images_path = images_path[len(self.known_face_encodings):]
            # self.write_data_file(images_path)
    def delete_files_in_folder(self, folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            print(file_path)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")  
      
    def detect_known_faces(self, frame):

        # Find all the faces and face encodings in the current frame of video
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        # small_frame = frame
        # cv2.imshow('face',small_frame)
        # cv2.waitKey(0)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        # Here I am detecting face locations from an image
        face_locations = face_recognition.face_locations(rgb_small_frame)
        # print("face_locations : ", face_locations)
        # Here I am creating the encodings of the face
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        # print('face_encodings : ', face_encodings)
        face_names = []
        face_professions = []
        # face_screen_names = []
        for face_encoding in face_encodings:
            # print('in')
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            # print("matches : ", matches)
            name = "Unknown"
            profession = 'Unknown'
            # screen_name = 'Unknown'

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
                profession = self.known_face_professions[best_match_index]
                # screen_name = self.known_face_screen_names[best_match_index]
            face_names.append(name)
            face_professions.append(profession)
            # face_screen_names.append(screen_name)

        # Convert to numpy array to adjust coordinates with frame resizing quickly
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        print('2.face_names : ', face_names)
        print('2.face_professions : ', face_professions)
        return face_names, face_professions #, face_screen_names

# sfr = SimpleFacerec()
# sfr.load_encoding_images()
# frame = cv2.imread('static\img\img1.jpeg')
# sfr.detect_known_faces(frame)