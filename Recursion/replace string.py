def replaceChar(s,a,b):
    if len(s) == 0:
        return s
    
    smallString = replaceChar(s[1:],a,b)

    if s[0] == a:
        return b+smallString

    else :
        return s[0]+ smallString

print(replaceChar("amartya nambiar",'a','b'))