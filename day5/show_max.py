# this app is for show max without use max function
use_in = input("plz input all number space sepereted: ").split()
maxx = 0
for n in range(0, len(use_in)):
    use_in[n] = int(use_in[n])

for i in use_in:
    if i > maxx:
        maxx = i

print(maxx)