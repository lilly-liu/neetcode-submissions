class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i, currDiff):
            if i >= len(nums):
                return
            if currDiff < 0:
                return
            if currDiff == 0:
                res.append(subset.copy())
                return
            # use nums[i]
            subset.append(nums[i])
            dfs(i, currDiff - nums[i])

            # don't use nums[i]
            subset.pop()
            dfs(i+1, currDiff)
        dfs(0, target) 
        return res  