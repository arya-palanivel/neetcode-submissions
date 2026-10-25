class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for num in numset:
            if num-1 not in numset:
                largest = 1
                while num+largest in numset:
                    largest+=1
                res = max(largest, res)
        return res