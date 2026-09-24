t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    
    possible = True
    
    for i in range(1, n):
        if d[i] < d[i-1]:
            possible = False
            break
        
    if possible:
        print("Yes")
    else:
        print("No")
    # Your code goes here
    t -= 1
