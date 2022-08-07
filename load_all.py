import glob
from pathlib import Path

import requests

LOCATION = rf'D:\Code\github\couchranking\json_data\*.json'
BASE_URL = 'http://localhost:8000/media/load/'

filelist = glob.glob(LOCATION)

for full_filename in filelist:
    base = Path(full_filename).stem
    print(f'base: {base}')
    url = BASE_URL + base
    print(f'url: {url}')
    requests.get(url)