t = int(input())

while t > 0:
    a, b, c = map(int, input().split())

    # A scalene triangle has all three sides different
    if a != b and b != c and a != c:
        print("YES")
    else:
        print("NO")

    t -= 1
    
    t=int(input())
    
    while t > 0:
        a , b , c = map(int, input().split())
        
        if a != b and b != c and a != c:
            print("YES")
        else:
            print("NO")
            
        t -=1    