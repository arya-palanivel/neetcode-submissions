class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = dict()
        for i in strs:
            temp = [0] * 26
            for j in i:
                temp[ord(j) - ord('a')] +=1
            if tuple(temp) not in grouped.keys():
                grouped[tuple(temp)] = [i]
            else:
                grouped[tuple(temp)].append(i)
        return list(grouped.values())