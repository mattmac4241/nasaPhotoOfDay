from helpers import get_key,get_page
import urllib

key = get_key() #key used for api

def get_photo_url():
    url = 'https://api.nasa.gov/planetary/apod?concept_tags=True&api_key=%s' % key
    data = get_page(url)
    return data['url']

def get_photo(url,name):
    fileName = 'photo/%s' % name
    f = open(fileName,'wb')
    f.write(urllib.urlopen(url).read())
    f.close()

def photo_name(url):
    photo = url.split('/')
    photoName = photo[len(photo)-1]
    return photoName



