N = int(input())

coordinates = list(map(int, input().split()))

# 중복 제거하고 정렬된 고유 값들
unique_sorted = sorted(set(coordinates))

# 각 고유 값의 인덱스(순위)를 딕셔너리로 저장
rank_dict = {value: index for index, value in enumerate(unique_sorted)}

# 각 좌표의 압축된 값 출력
for coordinate in coordinates:
    print(rank_dict[coordinate], end=" ")
