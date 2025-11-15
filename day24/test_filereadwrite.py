with open("output.txt", "w") as f:
    f.write("Hossein is the writer!")

with open("append.txt", mode="a") as f:
    f.write("\nHossein is the appender!")

with open("input.txt", "r") as f:
    print(f.read())

