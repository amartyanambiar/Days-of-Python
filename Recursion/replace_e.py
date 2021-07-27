def replace_e(s):
    if len(s) == 0:
        return s
    
    if s[0] == 'e':
        smallString = replace_e(s[1:])
        return '2.71'+smallString

    else:
        smallString = replace_e(s[1:])
        return s[0] + smallString

print(replace_e('hello'))