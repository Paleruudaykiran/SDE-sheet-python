def areAnagram(str1, str2):
    chars = [0]*256 
    for ch in str1 :
        chars[ord(ch)] += 1 
    for ch in str2 :
        chars[ord(ch)] -= 1 
    for x in chars :
        if x != 0 :
            return 0 
    return 1