# UWCOI20A - Rating 600

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-18T16:26:58.786Z  

```c_cpp
string solve(int N, int X, const vector<int>& A) {
    
    for (int i = 0; i < N; i++) {
        if (A[i] == X) {
            return "YES";
        }
    }

    return "NO";
}
```

---

[View on CodeChef](https://www.codechef.com/problems/UWCOI20A)