import sys

input = sys.stdin.readline

N, M = map(int, input().split())

account = {}

for _ in range(N):
    site, password = input().split()
    account[site] = password

for _ in range(M):
    site = input().strip()
    print(account[site])
