import random
student_name = ["ali","hossein","farhad","mojgan","marjan","zeinab",]
student_with_score={name:random.randint(1,100) for name in student_name}
print(student_with_score.items())
passed_student = {name:score for (name,score) in student_with_score.items() if score >=60 }
print(passed_student)
