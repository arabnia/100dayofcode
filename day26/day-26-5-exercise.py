weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

weather_f = {day:round(temp*1.8+32, 2) for day,temp in weather_c.items()}
# Write your code 👇 below:



print(weather_f)