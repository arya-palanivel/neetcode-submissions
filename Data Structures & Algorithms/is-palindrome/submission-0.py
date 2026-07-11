class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        edited_s = ""
        for i in s:
            if i.isalnum():
                edited_s+=i
        
        begin = 0
        end = len(edited_s)-1

        while begin < end:
            if edited_s[begin] == edited_s[end]:
                begin+=1
                end-=1
            else:
                return False
        return True