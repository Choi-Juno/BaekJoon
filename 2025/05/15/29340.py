a = input().strip()
b = input().strip()

result = ""
for i in range(4):
    result += str(max(a[i], b[i]))

print(result)
