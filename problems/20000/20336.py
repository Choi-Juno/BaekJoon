n = int(input())

menu_list = [input().split() for _ in range(n)]

for menu in menu_list[0]:
    print(menu)
