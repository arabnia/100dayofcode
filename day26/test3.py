with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    list1 = f1.read().splitlines()
    list2 = f2.read().splitlines()

list_final = [ n for n in list1 if n in list2
               ]
print(list_final)

