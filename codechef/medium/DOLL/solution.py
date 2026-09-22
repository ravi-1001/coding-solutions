# cook your dish here
T = int(input())

while T > 0:
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    
    ans = 0
    
    for height in H:
        if height > K:
            ans += 1
            
    print(ans)
    
    T -= 1