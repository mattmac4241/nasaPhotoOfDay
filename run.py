from nasa import get_photo_url, get_photo, photo_name
from setPhoto import set_wallpaper
import os

url = get_photo_url()
name = photo_name(url)
get_photo(url,name)
wd = os.getcwd()

photoPlace = '%s/photo/%s' % (wd,name)
set_wallpaper(photoPlace)
