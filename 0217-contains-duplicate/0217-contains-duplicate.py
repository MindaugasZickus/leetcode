
import collections
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        
        track = set()
        
        for n in nums:
            if n in track:
                return True
            track.add(n)
            
        return False
             