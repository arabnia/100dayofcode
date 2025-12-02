##################### Extra Hard Starting Project ######################
import csv
import pandas as pd
import random
import smtplib
import datetime
# 2. Check if today matches a birthday in the birthdays.csv
with open("birthdays.csv") as f:
    data = pd.read_csv(f)
dt = datetime.datetime.now()

user_birthday = data[(data["month"] == dt.month) & (data["day"] == dt.day)]
# print(user_birthday)

for (index, row) in user_birthday.iterrows():
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as template:
        text = template.read()
    text = text.replace("[NAME]", row["name"])
    print(text)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.



