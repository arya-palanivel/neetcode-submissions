class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wIndex = abbrIndex = 0
        number = ""
        while abbrIndex< len(abbr):
            if (number != "" and not abbr[abbrIndex].isdigit()):
                wIndex += int(number)
                if wIndex > len(word):
                    return False
                number = ""
            if( wIndex < len(word) and word[wIndex] == abbr[abbrIndex]):
                wIndex +=1
                abbrIndex +=1
            elif (abbr[abbrIndex].isdigit()):
                if(number == "" and int(abbr[abbrIndex]) == 0):
                    return False
                number += abbr[abbrIndex]
                abbrIndex+=1
            else: 
                return False
        if(number != ""):
            wIndex += int(number)
            if wIndex > len(word):
                return False
        return wIndex == len(word)
        
            