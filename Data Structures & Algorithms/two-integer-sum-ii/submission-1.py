class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            for x in range(i, len(numbers)):
                if numbers[x] + numbers[i] == target:
                    return [i+1 , x+1]
