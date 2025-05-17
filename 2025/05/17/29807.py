T = int(input())

subject = list(map(int, input().split())) + [0] * (5 - T)

studentNumber = 0

if subject[0] > subject[2]:
    studentNumber += abs(subject[0] - subject[2]) * 508
else:
    studentNumber += abs(subject[0] - subject[2]) * 108

if subject[1] > subject[3]:
    studentNumber += abs(subject[1] - subject[3]) * 212
else:
    studentNumber += abs(subject[1] - subject[3]) * 305

if subject[4]:
    studentNumber += subject[4] * 707

studentNumber = studentNumber * 4763

print(studentNumber)
