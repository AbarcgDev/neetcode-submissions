class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1;
        
        scored = [(value, key) for key, value in frequencies.items()]

        top_pk = heapq.nlargest(k, scored)

        return [item[1] for item in top_pk]