# UWCOI20A

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Find maximum in an Array

Given a list of $N$ integers, representing height of mountains. Find the height of the tallest mountain.

### Input:
- First line will contain $T$, number of testcases. Then the testcases follow.
- The first line in each testcase contains one integer, $N$.
- The following line contains $N$ space separated integers: the height of each mountains.
### Output:

For each testcase, output one line with one integer: the height of the tallest mountain for that test case.

### Constraints
- $1 \leq T \leq 10$
- $1 \leq N \leq 100000$
- $0 \leq$ height of each mountain $\leq 10^9$
### Sample 1:
Input
Output

```
1
5
4 7 6 3 1
```

```
7
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T17:44:35.524Z  

```py
# cook your dish here
t = int(input())

while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(max(arr))
    
    t -= 1
```

---

[View on CodeChef](https://www.codechef.com/problems/UWCOI20A)