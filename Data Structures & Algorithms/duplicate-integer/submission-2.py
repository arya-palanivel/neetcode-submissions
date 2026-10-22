class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tempSet = set()
        for i in nums:
            if i in tempSet:
                return True
            else:
                tempSet.add(i)
        return False