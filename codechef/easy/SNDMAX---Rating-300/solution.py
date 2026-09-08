N = int(input())

for _ in range(N):
    a, b, c = map(int, input().split())

    numbers = [a, b, c]
    numbers.sort()

    print(numbers[1])