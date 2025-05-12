n = int(input())

for _ in range(n):
    products = int(input())
    total = 0
    for _ in range(products):
        goods = input().split()
        total += float(goods[1]) * float(goods[2])
    print(f"${total:.2f}")
