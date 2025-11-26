instagram_posts = [
    {"likes": 10, "comments": 5},
    {"likes": 23, "comments": 5, "share": 10},
    {"likes": 5, "comments": 52, "share": 5},
    {"likes": 7, "comments": 1},
    {"comments": 5, "share": 1},
    {"likes": 9, "comments": 4},
    {"likes": 11, "comments": 2}
]
total_likes = 0
for post in instagram_posts:
    try:
        total_likes += post["likes"]
    except KeyError:
        pass

print(total_likes)