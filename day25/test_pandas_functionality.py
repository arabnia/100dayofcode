import csv
# tempreture = []
# with open("weather_data.csv", "r") as f:
#     data = csv.reader(f)
#     # next(data)
#     for temp in data:
#         if temp[1] != "temp":
#             tempreture.append(int(temp[1]))
#
# print(tempreture)

import pandas as pd
data = pd.read_csv("weather_data.csv")
#
# def c_to_f(celsius):
#     # return int(celsius.iloc[0] * (9 / 5) + 32)
#     return int(celsius * (9 / 5) + 32)
#
# # print(c_to_f(data[data.day == "Monday"].temp))
#
print(data[data.day.str.lower() == "tuesday"].empty)

# print(data[data.temp == data.temp.max()].day)

# generate csv file
# my_dict = {
#     "name": ["hossein", "ali", "farhad"],
#     "age": [28, 32, 65]
# }
#
# data = pd.DataFrame(my_dict)
# data.to_csv("data.csv", index=False)


