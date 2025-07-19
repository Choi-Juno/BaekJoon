N, M = map(int, input().split())

no_listen = set()
no_see = set()

for _ in range(N):
    no_listen.add(input())

for _ in range(M):
    no_see.add(input())

result = sorted(list(no_listen & no_see))

print(len(result))
print("\n".join(result))
