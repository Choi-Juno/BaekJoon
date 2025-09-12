N, M = map(int, input().split())

name_to_num = {}  # 이름 -> 번호
num_to_name = {}  # 번호 -> 이름

for i in range(N):
    name = input()
    name_to_num[name] = i + 1
    num_to_name[i + 1] = name

for i in range(M):
    question = input()
    if question.isdigit():
        print(num_to_name[int(question)])
    else:
        print(name_to_num[question])
