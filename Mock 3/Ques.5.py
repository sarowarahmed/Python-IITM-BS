mark = int(input())
options = int(input())
correct_options = input().split(',')
student_options = input().split(',')

per_quesyion_mark = mark/len(correct_options)
count = 0

for i in student_options:
    if i in correct_options:
        count += 1
    else:
        count = 0
        break

print(count*per_quesyion_mark)                  