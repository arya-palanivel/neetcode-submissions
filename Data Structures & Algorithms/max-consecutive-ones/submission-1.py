class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxOne = 0
        for i in nums:
            if i==1:
                print(i)
                counter +=1
            else:
                maxOne = max(counter, maxOne)
                counter =0
        maxOne = max(counter, maxOne)
        return maxOne