t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    
    largest = -1
    second = -1
    
    for x in a:
        if x > largest:
            second = largest
            largest = x 
        elif x > second and x != largest:
            second = x 
            
    print(largest + second)
    
    t -= 1
    # Your code goes here
