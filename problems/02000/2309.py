height_list = []

for i in range(9):
    height_list.append(int(input()))

height_list.sort()
sum_height = sum(height_list)

for i in range(len(height_list)):
    for j in range(i + 1, len(height_list)):
        if sum_height - height_list[i] - height_list[j] == 100:
            for k in range(len(height_list)):
                if k != i and k != j:
                    print(height_list[k])
                else:
                    pass
            exit()
