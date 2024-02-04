import requests
from dotenv import load_dotenv
import os
load_dotenv()
def get_images(name): 
    try: 
        name += ' face'
        url = "https://real-time-image-search.p.rapidapi.com/search"
        querystring = {"query":name,"region":"in"}
        headers = {
            "X-RapidAPI-Key": os.environ['API_KEY'],
            "X-RapidAPI-Host": "real-time-image-search.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring).json()
        if response is not None and 'data' in  response and response['data'] is not None:
            images_response = response['data']
            images = []
            i = 0
            if len(images_response) > 0:
                for image in images_response:
                    if i == 5:
                        break
                    images.append(image['thumbnail_url'])
                    i += 1
            return images
        else:
            raise Exception("Could not find any images with that name.")
    except Exception as e:
        print('Error in getting images from google: ', e)
        return []