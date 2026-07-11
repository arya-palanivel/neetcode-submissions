class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find row of value
        correct_row = 0
        for i in range(len(matrix)):
            if matrix[i][len(matrix[0])-1] > target:
                correct_row = i
                break
            elif matrix[i][len(matrix[0])-1] == target:
                return True
        l, r = 0, len(matrix[0])-1
        while r >=l:
            mid= (r+l)//2
            if matrix[correct_row][mid] > target:
                r = mid -1
            elif matrix[correct_row][mid] < target:
                l = mid+1
            else:
                return True
        return False        