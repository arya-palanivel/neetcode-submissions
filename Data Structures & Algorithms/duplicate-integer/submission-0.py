class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_array = []
        for i in nums:
            if(i in temp_array):
                 return True
            temp_array.append(i)
        return False