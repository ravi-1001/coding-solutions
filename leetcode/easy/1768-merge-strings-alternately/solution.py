class Solution:
    def mergeAlternately(ans, word1: str, word2: str) -> str:
        ans = ""

        i = 0
        j = 0

        while i < len(word1) or j < len(word2):

            if i < len(word1):
                ans += word1[i]
                i += 1
            if j < len(word2):
                ans += word2[j]
                j += 1 
        
        return ans

        