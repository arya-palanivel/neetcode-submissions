class Solution:
    def maxArea(self, heights: List[int]) -> int:
        highest = 0
        l, r = 0, len(heights)-1

        while l < r:
            total = (r-l) * min(heights[l], heights[r])
            highest = max(highest, total)

            if(min(heights[l], heights[r]) == heights[l]):
                l+=1
            else:
                r-=1
        return highest