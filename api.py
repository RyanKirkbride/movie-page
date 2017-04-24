import requests
import media


headers = {
  'Accept': 'application/json'
}

url = "http://api.themoviedb.org/3/movie/"
key = "api_key=663f7e83cb86f2ccf02490456cdd6c3e"

youtube_url = "https://www.googleapis.com/youtube/v3/search?type=video&part=snippet&"
youtube_key = "key=AIzaSyDDySozvf5K3VAIfIU5wh_TvH-9y3LdRNI"

# request upcoming movies from themoviedb.org
def get_upcoming():
    get = requests.get(url+"upcoming?"+key,
                       headers=headers)
    results = get.json()['results']

    return parse(results)

# parse the movie information retrieved from themoviedb.org into movie objects             
def parse(r):
    movie_list = []
    i = 0
    while(i < len(r)):
        q = r[i]['title'].replace(" ", "+") + "+trailer"
        get = requests.get(youtube_url+youtube_key+"&q="+q)
        try:
            search = get.json()['items'][0]['id']['videoId']
            trailer = "https://www.youtube.com/watch?v="+search
        except IndexError:
            trailer = "https://www.youtube.com/watch?v=ieQH6X_XBJo"
        title = r[i]['title']
        overview = r[i]['overview']
        try:
            poster = "https://image.tmdb.org/t/p/w300_and_h450_bestv2/"+r[i]['poster_path']
        except TypeError:
            poster = "https://placehold.it/220x342"

        movie = media.Movie(title,
                     overview,
                     poster,
                     trailer)

        movie_list.append(movie)
        i = i + 1

    
    return movie_list
   








    
