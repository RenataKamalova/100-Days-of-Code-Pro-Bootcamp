student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

sum_number = 0
counter = 0

for height in range(0, len(student_heights)):
    sum_number += student_heights[height]
    counter += 1

average_number = round(sum_number / counter)
print(average_number)
