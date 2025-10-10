student_score = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "neville":62,
}

def con_sc_gr(dictionary):
    student_grade = {}
    for name in dictionary:
        if dictionary[name] > 90:
            student_grade[name] = "Outstanding"
        elif dictionary[name] > 80:
            student_grade[name] = "Exceeds expectation"
        elif dictionary[name] > 70:
            student_grade[name] = "Acceptable"
        elif dictionary[name] < 71:
            student_grade[name] = "Fail"
    print(student_grade)    

con_sc_gr(student_score)

# Outstanding
# Exceeds expectation
# Acceptable
# Fail