t = int(input())

while t > 0:
    x, y, z = map(int, input().split())
    
    chocolates = (x * 5 + y * 10) // z
    
    print(chocolates)
    
    t -= 1