import csv
import pandas as pd
import random
import smtplib
import datetime
# 2. Check if today matches a birthday in the birthdays.csv
# with open("birthdays.csv") as f:
#     data = pd.read_csv(f)
#
# users = []
# print(data[data["name"] == "Hossein"].iloc[0])
import random
# 2. Check if today matches a birthday in the birthdays.csv
with open("birthdays.csv") as f:
    data = pd.read_csv(f)
dt = datetime.datetime.now()

user_birthday = data[data["month"] == 12]
for row in user_birthday.iterrows():
    print(row)