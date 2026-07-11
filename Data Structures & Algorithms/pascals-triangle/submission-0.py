class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]

        for i in range(1, numRows):
            newList = []
            for j in range(len(output[i-1])):
                if(j+1 < len(output[i-1])):
                    newList.append(output[i-1][j]+output[i-1][j+1])
            newList.insert(0, 1)
            newList.append(1)
            output.append(newList)
        return output