# 회전 명령에 따른 방향 변화 처리
directions = ["N", "E", "S", "W"]
current_dir = 0

# 각 명령어에 대한 방향 변화량 매핑
rotations = {
    "1": 1,  # 시계 방향으로 90도 회전
    "2": 2,  # 시계 방향으로 180도 회전
    "3": -1,  # 반시계 방향으로 90도 회전
}

for _ in range(10):
    command = input()
    current_dir = (current_dir + rotations.get(command, 0)) % 4

print(directions[current_dir])
