from bs4 import BeautifulSoup
import requests
url = "https://www.empireonline.com/movies/features/best-movies-of-all-time-us/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/122.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
}
target_site = requests.get(url, headers=headers, timeout=10)

target_soup = BeautifulSoup(target_site.content, "html.parser")

items = target_soup.select("h2 strong")
movie_title = [ item.get_text() for item in items]
with open("movie_title.txt", "w") as f:
    f.write("\n".join(movie_title))
