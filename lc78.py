class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #決定要加
            subset.append(nums[i])
            dfs(i + 1)

            #決定不加，pop掉
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
