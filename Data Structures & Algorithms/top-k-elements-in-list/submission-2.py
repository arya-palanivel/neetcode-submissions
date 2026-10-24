import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num]  = 1 + count.get(num,0)
        heap = []

        for key, value in count.items():
            heapq.heappush(heap,(value, key))
            if(len(heap) > k):
                heapq.heappop(heap)
        returnLst = []
        for i in range(k):
            returnLst.append(heapq.heappop(heap)[1])
        return returnLst
