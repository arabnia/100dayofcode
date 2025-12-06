import random
import datetime

with open("motivational_qoutes.txt") as f:
    motivational_qoutes = f.read().splitlines()

dt = datetime.datetime.now()
if dt.weekday() == 1:
    print(random.choice(motivational_qoutes))