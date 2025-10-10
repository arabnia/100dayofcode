# this app is for calculate student's height average!
student_height = input ("plz input all student height with space seperated!: ").split()

for i in range(0, len(student_height)):
    student_height[i] = int(student_height[i])

print(round((sum(student_height)) / len(student_height)))
