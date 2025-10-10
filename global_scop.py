# testing changing a variable in function
may_var = 5

def changing_var():
    globals may_var
    may_var = 4
    return may_var

print(changing_var())
print(may_var)