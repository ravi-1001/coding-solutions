class Solution:
    def count_non_minimum(self, nums):
        minimum = min(nums)
        cout = 0 
        
        for x in nums:
            if x > minimum:
                cout += 1
        return cout
        # write your code here
        
