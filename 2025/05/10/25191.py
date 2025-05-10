N = int(input())
Cola, Beer = map(int, input().split())
chicken = 0

chicken += Cola // 2
chicken += Beer

print(chicken if chicken <= N else N)
