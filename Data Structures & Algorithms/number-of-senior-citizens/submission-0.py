class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(age[11:13])> 60 for age in details)