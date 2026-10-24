class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalDict = {}
        for each in strs:
            tempArr = [0] * 26
            for i in each:
                tempArr[ord(i)-ord('a')]+=1
            tempArr = tuple(tempArr)
            if(tempArr in finalDict):
                finalDict[tempArr].append(each)
            else:
                finalDict[tempArr] = [each]
        return list(finalDict.values())