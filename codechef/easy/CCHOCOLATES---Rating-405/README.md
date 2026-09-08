# CCHOCOLATES - Rating 405

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef and Chocolates

Chef has $X$ `5` rupee coins and $Y$ `10` rupee coins. Chef goes to a shop to buy chocolates for Chefina where each chocolate costs $Z$ rupees. Find the maximum number of chocolates that Chef can buy for Chefina.

### Input Format
- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains three integers $X$, $Y$ and $Z$ — the number of 5 rupee coins, the number of 10 rupee coins and the cost of each chocolate.
### Output Format

For each test case, output the maximum number of chocolates that Chef can buy for Chefina.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X,Y,Z \leq 1000$
### Sample 1:
Input
Output

```
4
10 10 10
3 1 8
8 1 3
4 4 1000
```

```
15
3
16
0

```

### Explanation:

 **Test case $1$:**  Chef has $10 \cdot 5 + 10 \cdot 10 = 150$ rupees in total. Since each chocolate costs $10$ rupees, Chef can spend all $150$ rupees and buy $15$ chocolates for Chefina.

 **Test case $2$:**  Chef has $3 \cdot 5 + 1 \cdot 10 = 25$ rupees in total. Since each chocolate costs $8$ rupees, Chef can buy a maximum of $3$ chocolates for Chefina, leaving him with $1$ rupee.

 **Test case $3$:**  Chef has $8 \cdot 5 + 1 \cdot 10 = 50$ rupees in total. Since each chocolate costs $3$ rupees, Chef can buy a maximum of $16$ chocolates for Chefina, leaving him with $2$ rupee.

 **Test case $4$:**  Chef has $4 \cdot 5 + 4 \cdot 10 = 60$ rupees in total. Since each chocolate costs $1000$ rupees, Chef can buy no chocolate for Chefina, leaving him with $60$ rupees.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T03:04:10.384Z  

```py
t = int(input())

while t > 0:
    x, y, z = map(int, input().split())
    
    chocolates = (x * 5 + y * 10) // z
    
    print(chocolates)
    
    t -= 1
```

---

[View on CodeChef](https://www.codechef.com/problems/CCHOCOLATES)