def genSentence(i,curr,s,sentence,dic):
    if i > len(s) : 
        return
    if i == len(s) : 
        print(" ".join(sentence))
        return 
    for ind in range(i,len(s)) : 
        if s[i:ind+1] in dic : 
            sentence.append(s[i:ind+1]) 
            genSentence(ind+1,curr,s,sentence,dic) 
            sentence.pop()
        

def wordBreak(s, dictionary):
    sentence = []
    genSentence(0,"",s,sentence,dictionary)
    return []

s = "godisnowherenowhere"
dic = ["god",'is','now','no','where','here']

print(wordBreak(s,dic))
