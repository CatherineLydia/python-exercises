total = 0
number_of_students=0
student_heights = input("Input a list of student heights ").split()

# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#   total = total+int(student_heights[n])

for height in student_heights:
    total+=int(height)
    number_of_students +=1
average= round(total/number_of_students)

# total=sum(student_heights)
# average = round(total/len(student_heights))

print(average)
