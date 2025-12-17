from bs4 import BeautifulSoup
import requests
import pandas as pd
target_site = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(target_site.content, "html.parser")
items = soup.find_all("span", class_="titleline")
title_link = [item.find("a")["href"] for item in items]
title_text = [item.find("a").get_text() for item in items]

soup_votes = soup.find_all("span", class_="score")
title_score = [int(soup_vote.get_text().split()[0]) for soup_vote in soup_votes]

max_score_index = title_score.index(max(title_score))
print(title_text[max_score_index])
print(title_link[max_score_index])

print(len(title_text))
print(len(title_link))
print(len(title_score))
# data = pd.DataFrame(
#     {
#      "title": title_text,
#      "link": title_link,
#      "score": title_score
#     }
# )
# data.to_csv("data.csv", index=False)
# title_links = []
# title_vote = []
