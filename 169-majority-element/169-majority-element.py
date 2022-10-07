from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Boyer - Moore Voting Algorithm
        count=0
        
        for n in nums:
            if count==0:
                candidate = n
            count += (1 if n==candidate else -1)
            
            
        return candidate    
            