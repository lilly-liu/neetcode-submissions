class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        return any([freq[k] > 1 for k in freq])
            