import json
import sys


def get_movie_details(title):
    filename = rf'D:\Code\github\couchranking\json_data\{title}.json'
    print(f"opening: {filename}")
    with open(filename, encoding="utf-8") as f:
        data = json.load(f)
    # dump_data(data)

    return data


def dump_data(data):
    print(f'{data.get("Title")}')
    print(f'{data.get("Year")}')
    print(f'{data.get("Rated")}')
    print(f'{data.get("Released")}')
    print(f'{data.get("Runtime")}')
    print(f'{data.get("Genre")}')
    print(f'{data.get("Director")}')
    print(f'{data.get("Writer")}')
    print(f'{data.get("Actors")}')
    print(f'{data.get("Plot")}')
    print(f'{data.get("Language")}')
    print(f'{data.get("Country")}')
    print(f'{data.get("Awards")}')
    print(f'{data.get("Poster")}')
    print(f'ratings: {data.get("Ratings")}')
    # print(f'{data.get("Ratings").get(0).get("Source")}')
    print(f'{data.get("Metascore")}')
    print(f'{data.get("imdbRating")}')
    print(f'{data.get("imdbVotes")}')
    print(f'{data.get("imdbID")}')
    print(f'{data.get("Type")}')
    print(f'{data.get("DVD")}')
    print(f'{data.get("BoxOffice")}')
    print(f'{data.get("Production")}')
    print(f'{data.get("Website")}')
