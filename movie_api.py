import http.client


def main():
    print("hello")
    conn = http.client.HTTPSConnection("movie-database-alternative.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "9eda0fab15msha6330d5e7e30c9bp1d30e1jsnf5fcce07e2b9",
        'X-RapidAPI-Host': "movie-database-alternative.p.rapidapi.com"
    }

    conn.request("GET", "/?s=Breaking%20Bad&r=json&page=1", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))



if __name__ == '__main__':
    main()