import cv2
import os
from algorithm.simple_facerec import SimpleFacerec

def main_fun(img_name):
    sfr = SimpleFacerec()
    sfr.load_encoding_images()
    # print(img_name)
    # cap = cv2.VideoCapture(0)
    # frame = cv2.imread('images/Sundar Pichai.jpg')
    # frame = cv2.imread("images/Elon Musk.jpg")
    cwd = os.getcwd()
    read_image_path = os.path.join(cwd, 'static', 'img', img_name)
    # frame = cv2.imread('C:\\Users\\anant\\OneDrive\\Desktop\\se.jpg')

    # Returns the numpy array of image pixel intensity
    frame = cv2.imread(read_image_path)
    # while True:
        # ret, frame = cap.read()
        
    face_names, face_professions = sfr.detect_known_faces(frame)
    return face_names, face_professions
    #h = left, x = top, y = right, w = bottom


    # for face_loc, name, profession in zip(face_locations, face_names, face_professions):
    #     x, y, w, h = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
    #     cv2.putText(frame, name, (h, x-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 243), 2)
    #     # cv2.putText(frame, name, (y, w), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 243), 2)

    #     #hme hmesha top-left se bottom-right  pr rectangle draw krna hota h
    #     cv2.rectangle(frame, (h, x), (y, w), (0, 0, 200), 4) 

    # resized = cv2.resize(frame, (int(frame.shape[1]/2), int(frame.shape[0]/2)))
    # cv2.imshow('Mera', resized)
    # key = cv2.waitKey(0)

    # if key == 13:
    #     break

    # cap.release()
    # cv2.destroyAllWindows()

# if __name__ == '__main__':
#     main_fun("img1.jpeg")

