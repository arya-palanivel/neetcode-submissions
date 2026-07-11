class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res=[]
        movePtr = 0
        while movePtr < len(nums):
            if (nums[movePtr]>0):
                break
            
            if movePtr > 0 and nums[movePtr] == nums[movePtr - 1]:
                movePtr+=1
                continue

            l, r = movePtr+1, len(nums)-1
            while l < r:
                currtotal = nums[l] + nums[r]
                if (currtotal > -1 * nums[movePtr]):
                    r-=1
                elif (currtotal < -1 * nums[movePtr]):
                    l+=1
                else:
                    res.append([nums[movePtr], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[ l- 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
            movePtr+=1
        return res
            
        
