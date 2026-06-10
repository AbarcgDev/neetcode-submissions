class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, -1) + 1
            if seen[num] != 0: 
                return True;
        
        return False