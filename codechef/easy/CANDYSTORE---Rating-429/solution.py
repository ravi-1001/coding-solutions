t = int(input())

while t > 0:
    x, y = map(int, input().split())

    if y <= x:
        print(y)
    else:
        extra = y - x
        money = x + (extra * 2)
        print(money)

    t -= 1