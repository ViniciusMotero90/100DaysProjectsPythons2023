import bs4
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
best_movies = response.text
soup = bs4.BeautifulSoup(best_movies, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movies_titles = [movie.getText() for movie in all_movies]
movies = movies_titles[::-1]

with open("movie.txt", mode='w') as file:
    for movie in movies:
        file.write(f"{movie}\n")
