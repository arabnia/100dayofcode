import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251116.csv")

output = (data["Primary Fur Color"].value_counts(dropna=False))
# output_frame = output.to_frame()
# print(type(output_frame))
print(output)
output.to_csv("output.csv")
