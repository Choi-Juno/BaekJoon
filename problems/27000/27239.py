n = int(input())

# 열 (a~h)
col = chr(ord("a") + (n - 1) % 8)
# 행 (1~8)
row = (n - 1) // 8 + 1

print(f"{col}{row}")
