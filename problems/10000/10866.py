import sys

input = sys.stdin.readline


def queue_func(command, number=None, queue=[]):
    match command:
        case "push_front":
            queue.insert(0, number)
        case "push_back":
            queue.append(number)
        case "pop_front":
            if queue:
                print(queue.pop(0))
            else:
                print(-1)
        case "pop_back":
            if queue:
                print(queue.pop())
            else:
                print(-1)
        case "size":
            print(len(queue))
        case "empty":
            if queue:
                print(0)
            else:
                print(1)
        case "front":
            if queue:
                print(queue[0])
            else:
                print(-1)
        case "back":
            if queue:
                print(queue[-1])
            else:
                print(-1)


N = int(input())
queue = []

for _ in range(N):
    command = input().split()
    if len(command) == 1:
        result = queue_func(command[0], None, queue)
    else:
        result = queue_func(command[0], int(command[1]), queue)

    if result is not None:
        print(result)
