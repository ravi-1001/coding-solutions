# FLOW006 - Rating 455

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Sum of Digits

You're given an integer  **N**. Write a program to calculate the sum of all the digits of  **N**.

### Input Format

The first line contains an integer  **T**, the total number of testcases. Then follow  **T**  lines, each line contains an integer  **N**.

### Output Format

For each test case, calculate the sum of digits of  **N**, and display it in a new line.

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000000$
### Sample 1:
Input
Output

```
3 
12345
31203
2123

```

```
15
9
8

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T05:08:03.441Z  

```py
# cook your dish here
t = int(input())

while t > 0:
    n = int(input())

    sum_digits = 0

    while n > 0:
        digit = n % 10          # Get last digit
        sum_digits += digit     # Add digit to sum
        n = n // 10             # Remove last digit

    print(sum_digits)

    t -= 1
```

---

[View on CodeChef](https://www.codechef.com/problems/FLOW006)