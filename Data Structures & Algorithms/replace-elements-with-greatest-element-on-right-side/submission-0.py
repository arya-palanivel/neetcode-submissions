class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]: 
        moveIndex = len(arr)-2 
        greatest = arr[len(arr)-1]
        while(moveIndex>=0):
            if(arr[moveIndex] <= greatest):
                arr[moveIndex] = greatest
                moveIndex-=1
            else:
                temp = arr[moveIndex]
                arr[moveIndex] = greatest
                greatest = temp
                moveIndex-=1
        arr[-1] = -1
        return arr
