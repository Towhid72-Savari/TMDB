import http.client

conn = http.client.HTTPSConnection("movie-database-imdb-alternative.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "bcbd1cbb97msh50e10d2766bb440p1fa7fbjsn7201f4fc297b"
    }

conn.request("GET", "/?page=1&r=json&s=Avengers%20Endgame", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))