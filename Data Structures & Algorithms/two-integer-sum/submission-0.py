class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        returnDict = {}
        for i in range(len(nums)):
            if(target - nums[i] in returnDict):
                return [ returnDict[target-nums[i]], i]
            returnDict[nums[i]] = i
        return []
            