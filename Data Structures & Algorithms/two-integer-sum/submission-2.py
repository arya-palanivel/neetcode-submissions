class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumDict = {}

        for i in range(len(nums)):
            if target - nums[i] in sumDict.keys():
                return  [sumDict[target-nums[i]], i]
            else:
                sumDict[nums[i]] = i
        return [0,0]