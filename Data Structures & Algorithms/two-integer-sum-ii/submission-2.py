class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = 0
        l = len(numbers) -1

        while r<l:
            sumer =  numbers[r]+ numbers[l]
            if sumer > target:
                l-=1
            elif sumer < target:
                r+=1
            else:
                return [r+1, l+1]
        return [0,0]