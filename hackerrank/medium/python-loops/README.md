# Python: Division

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

<sub>Check [Tutorial](https://www.hackerrank.com/challenges/python-loops/tutorial) tab to know how to to solve.</sub>  

**Task**  
The provided code stub reads an integer, $n$, from STDIN. For all non-negative integers $i \lt n$, print $i^2$.  

**Example**  
$n = 3$  

The list of non-negative integers that are less than $n = 3$ is $[0, 1, 2]$.  Print the square of each number on a separate line.

<pre>
0
1
4
</pre>




**Input Format**

The first and only line contains the integer, $n$. 

**Constraints**

$1 \le n \le 20$  

**Output Format**

Print $n$ lines, one corresponding to each $i$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-23T05:41:36.416Z  

```py
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-loops/problem)