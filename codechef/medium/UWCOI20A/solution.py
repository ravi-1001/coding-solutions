# cook your dish here
t = int(input())

while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(max(arr))
    
    t -= 1