from googleapiclient.discovery import build

class Youtube:
    def __init__(self, thumbnail_url, song_name, song_url):
        self.thumbnail_url = str(thumbnail_url)
        self.song_name = str(song_name)
        self.song_url = str(song_url) 
    def __repr__(self):
        return f'{self.thumbnail_url} -- {self.song_name}  -- {self.song_url}'

def get_yt_data(name, profession):
    try:
        name = name.lower()
        
        api_key = 'AIzaSyDMPqk6B7oTnwP0Og4JmUzMb5BSa_l-WAA'

        youtube = build('youtube', 'v3', developerKey=api_key)
        global request
        if profession == 'Actor' or profession == 'Actress' or profession == 'Singer':
            query = name + ' new songs'
            request = youtube.search().list(part='snippet', type='video', q=query, videoDuration='medium', maxResults=501)
        else:
            query = name + ' videos'
            request = youtube.search().list(part='snippet', type='video', q=name, videoDuration='medium', maxResults=501)

        response = request.execute()
        # print(response)
        base_video_url = 'https://www.youtube.com/watch?v='
        # for key,val in response.items():
        #     print(key, ":", val)
        #     print(type(key), ":", type(val))
            # if key == 'items':
            #     for item in val:
            #         print(item['snippet'])
            #         print('\n\n\n\n\n')
            #         # for ik, jv in item.items():
            #         #     print(ik ,':' ,jv)
            #         #     print(type(ik), ':', type(jv))
            #         #     print('\n\n\n')
        all_yt_songs = []

        for item in response['items']:

            thumbnail_url = item['snippet']['thumbnails']['high']['url']
            song_name = item['snippet']['title']
            song_url = base_video_url + item['id']['videoId']
            yt_obj = Youtube(thumbnail_url, song_name, song_url)
            all_yt_songs.append(yt_obj)

        # for i in all_yt_songs:
        #     print(i)
        #     print('\n\n\n\n')
        return all_yt_songs
    except Exception as e:
        print('Error in finding youtube data: ', e)
        return []
# l = get_yt_data('shahrukh khan')
# print(l)
