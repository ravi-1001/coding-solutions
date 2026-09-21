# OPMIN

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T17:53:12.505Z  

```py
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

```

---

[View on CodeChef](https://www.codechef.com/problems/OPMIN)