import glob
import time
from pathlib import Path
# from util.sources import Sources

import requests

from media.util.sources import Sources

LOCATION = rf'D:\Code\github\couchranking\json_data\*.json'
BASE_URL = 'http://127.0.0.1:8000/media'
BASE_LOAD_URL = 'http://127.0.0.1:8000/media/load'
BASE_SOURCE_ADD_URL = BASE_URL + '/source'

source_list = {'Breaking Bad': Sources.Netflix,
               'Almost Famous': Sources.Amazon,
               'Prey': Sources.Hulu,
               'Bad Education': Sources.HBO,
               'The Nice Guys': Sources.Netflix,
               'Bullet Train': Sources.Theater,
               'The Orville': Sources.Hulu,
               'The Orville: New Horizons': Sources.Hulu }

filelist = glob.glob(LOCATION)

for full_filename in filelist:
    base = Path(full_filename).stem
    print(f'base: {base}')
    url = BASE_LOAD_URL + "/" + base
    print(f'url: {url}')
    start = time.time()
    requests.get(url)
    end = time.time()
    elapsed = end - start
    print(f'url took {elapsed}   {end} {start}')

headers = {'content-type': 'application/json'}

media_items = requests.get(BASE_URL, headers=headers)

for media in media_items.json():
    title = media.get("title")
    if title in source_list:
        id = media.get("id")
        # print(f'id: {id}')
        source = source_list.get(title)
        # print(f'source: {source.value}')
        url = f'{BASE_SOURCE_ADD_URL}/{id}/{source.value}'
        print(f'url: {url}')
        requests.put(url, headers=headers)
        # if title in Sources:
        #     print("YES")
        # source = Sources(title)
        #

        # print(f'updating: {media.title}')
    # jsonw = media.json()
    # # print(json.dumps(media.json(), indent=2))
    # print(jsonw)