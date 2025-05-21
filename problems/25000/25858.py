n, d = map(int, input().split())

questions = []
for _ in range(n):
    question = int(input())
    questions.append(question)

for question in questions:
    prize = d // sum(questions)
    print(prize * question)
