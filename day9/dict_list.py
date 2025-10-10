travel_log =[
    {
        "contry": "France",
        "visit": 12,
        "cities": ["Paris", "Little", "Dijon"]
    },
    {
        "contry": "Germany",
        "visit": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]
# travel_dict = {
#         "contry": "France",
#         "visit": 12,
#         "cities": ["Paris", "Little", "Dijon"]
#     }

def add_new_contry(contry, visits, cities):
    travel_log.append({"contry": contry, "visit": visits, "cities": cities}) 
    print(travel_log)


add_new_contry ("Russia", 2, ["Moscow", "Saint Petersburg"])