ISBN = input()

check_sign = int(ISBN[-1])
sum_without_missing = 0
missing_weight = 0

for number, weight in zip(ISBN[:-1], [1, 3] * 6):
    if number == "*":
        missing_weight = weight
        continue
    sum_without_missing += int(number) * weight

for unknown in range(10):
    rest = (sum_without_missing + (unknown * missing_weight) + check_sign) % 10

    if rest == 0:
        print(unknown)
        break
