class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        
        mult =1
        for i in range(1,len(nums)):
            mult *=nums[i-1]
            prefix[i] = mult
        
        mult =1
        for i in range(len(nums)-2,-1,-1):
            mult *=nums[i+1]
            postfix[i] = mult
        print(prefix)
        print(postfix)
        prefix[0] = 1
        postfix[-1] = 1
        res = [0] * len(nums)
        for i in range(len(prefix)):
            res[i] = prefix[i] * postfix[i]
        return res