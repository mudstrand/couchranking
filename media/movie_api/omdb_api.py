import json
import sys


def get_movie_details(title):
    filename = rf'D:\Code\github\couchranking\json_data\{title}.json'
    print(f"opening: {filename}")
    with open(filename) as f:
        data = json.load(f)
    # dump_data(data)

    return data


def dump_data(data):
    print(f'{data["Title"]}')
    print(f'{data["Year"]}')
    print(f'{data["Rated"]}')
    print(f'{data["Released"]}')
    print(f'{data["Runtime"]}')
    print(f'{data["Genre"]}')
    print(f'{data["Director"]}')
    print(f'{data["Writer"]}')
    print(f'{data["Actors"]}')
    print(f'{data["Plot"]}')
    print(f'{data["Language"]}')
    print(f'{data["Country"]}')
    print(f'{data["Awards"]}')
    print(f'{data["Poster"]}')
    print(f'ratings: {data["Ratings"]}')
    print(f'{data["Ratings"][0]["Source"]}')
    print(f'{data["Metascore"]}')
    print(f'{data["imdbRating"]}')
    print(f'{data["imdbVotes"]}')
    print(f'{data["imdbID"]}')
    print(f'{data["Type"]}')
    print(f'{data["DVD"]}')
    print(f'{data["BoxOffice"]}')
    print(f'{data["Production"]}')
    print(f'{data["Website"]}')
