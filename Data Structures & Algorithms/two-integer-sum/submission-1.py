class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_indices = {}   
        for i, num in enumerate(nums):
            complement = target - num  
            if complement in seen_indices:
                return [seen_indices[complement], i]
            seen_indices[num] = i
            
        return [0,0]