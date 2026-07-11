class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            target = -1 * nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                summer = nums[left] + nums[right]
                if (summer > target):
                    right -=1
                elif(summer < target):
                    left +=1
                else:
                    res.append([nums[left], nums[right], nums[i]])
                    left+=1
                    while nums[left] == nums[left-1] and left <right:
                        left +=1
        return res
        