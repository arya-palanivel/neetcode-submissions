class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        post = [1] * len(nums)
        prefmult = 1
        for i in range(1,len(nums)):
            pref[i] = prefmult * nums[i-1]
            prefmult = pref[i]
        postmult = 1
        for i in range(len(nums)-2,-1,-1):
            post[i] = postmult * nums[i+1]
            postmult = post[i]

        for i in range(len(nums)):
            nums[i] = post[i]* pref[i]
        return nums