# Print Function

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

<sup>`*`This section assumes that you understand the basics discussed in __HTML Parser - Part 1__</sup>


[*.handle\_comment(data)*](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_comment)  
This method is called when a comment is encountered (e.g. &lt;!--comment-->).  
The *data* argument is the content inside the comment tag:

	from html.parser import HTMLParserr

	class MyHTMLParser(HTMLParser):
    	def handle_comment(self, data):
    	  	  print("Comment  :", data)
<br>

[*.handle\_data(data)*](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_data)  
This method is called to process arbitrary data (e.g. text nodes and the content of &lt;script>...&lt;/script> and &lt;style>...&lt;/style>).  
The *data* argument is the text content of HTML.

	from html.parser import HTMLParserr

	class MyHTMLParser(HTMLParser):
        def handle_data(self, data):
        	print("Data     :", data)
            
---
__Task__

You are given an *HTML* code snippet of $N$ lines.  
Your task is to print the *single-line comments, multi-line comments* and the *data*. 

Print the result in the following format:

	>>> Single-line Comment  
    Comment
    >>> Data                 
    My Data
    >>> Multi-line Comment  
    Comment_multiline[0]
    Comment_multiline[1]
    >>> Data
    My Data
    >>> Single-line Comment:  
    
    
**Note**: Do not print *data* if `data == '\n'`.  

**Input Format**

The first line contains integer $N$, the number of lines in the *HTML* code snippet.  
The next $N$ lines contain *HTML* code.

__Constraints__

$0 < N < 100$

**Constraints**

 

**Output Format**

 Print the *single-line comments, multi-line comments* and the *data* in order of their occurrence from top to bottom in the snippet.<br>

Format the answers as explained in the problem statement.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-27T14:22:46.732Z  

```py
if __name__ == '__main__':
    n = int(input())
    
    # for i in range(1, n+1):
    #     print(i, end="")
    
    print(*range(1, n + 1), sep="")
    

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/html-parser-part-2/problem)