class Solution:
    def reverseWords(self, s: str) -> str:
        lis = [] 
        curr = ""
        for ch in s:
            if ch == " " :
                if curr == "" :
                    continue 
                else :
                    lis.append(curr) 
                    curr = ""
            else : 
                curr += ch
        if curr != "" :
            lis.append(curr) 
        lis = lis[::-1] 
        return " ".join(lis)