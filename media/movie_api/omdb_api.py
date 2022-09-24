import json
import requests

DATA = "http://www.omdbapi.com/?apikey=[yourkey]&"
POSTER = "http://img.omdbapi.com/?apikey=[yourkey]&"
SAMPLE = "http://www.omdbapi.com/?i=tt3896198&apikey=3fc3dbe7"
SAMPLE_2 = "http://www.omdbapi.com/?t=Breaking&apikey=3fc3dbe7"
SEARCH_URL_BASE = "http://www.omdbapi.com/?"

def read_key():
    filename = r'D:\Code\github\couchranking\omdb_key.txt'
    with open(filename) as f:
        data = f.readline()

    return data

KEY = read_key()
# page -> items to return
# s -> search term
# type -> movie, series, episode

def omdb_search(title):
    url = get_name_search_url(title, KEY)
    r = requests.get(url)
    print(json.dumps(r.json(), indent=2))
    return r.json()


def get_name_locate_url(name, key):
    url = ("%st=%s&apikey=%s" % (SEARCH_URL_BASE, name, key))
    return url


def get_name_search_url(name, key):
    url = ("%ss=%s&apikey=%s" % (SEARCH_URL_BASE, name, key))
    return url


def get_name_search_by_type_url(name, type, key):
    url = ("%ss=%s&type=%s&apikey=%s" % (SEARCH_URL_BASE, name, type, key))
    return url


def get_id_search_url(id, key):
    url = ("%si=%s&apikey=%s" % (SEARCH_URL_BASE, id, key))
    return url




