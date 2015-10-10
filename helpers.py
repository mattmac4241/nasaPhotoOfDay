'''Helper functions'''
#return a json of a page
import json
import urllib2


def get_page(url):
    try:
        data = json.load(urllib2.urlopen(url))
        return data
    except ValueError:
        return "ERROR"

#get key
def get_key():
    key = open('key.txt','r')
    key = key.read().split(' ')[0].replace('\n','')
    return key 

