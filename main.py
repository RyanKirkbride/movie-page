import media
import fresh_tomatoes
import api


# create a list of movie objects
movies = api.get_upcoming()
# create and open an HTML page displaying movie information
fresh_tomatoes.open_movies_page(movies)
