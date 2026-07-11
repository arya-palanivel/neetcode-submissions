class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights)-1
        total = 0

        while end > start:
            total= max(total, (end - start) * min(heights[end], heights[start]))
            if(heights[end] > heights[start]):
                start+=1
            else:
                end-=1

        return total
