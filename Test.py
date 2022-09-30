'''def get_missing_letters(str):
    missing_str = ""

    for x in range(97, 123):
        if chr(x) not in str:
            missing_str += chr(x)
    
    return missing_str

print(get_missing_letters("abcdefgpqrstuvwxyz"))
print(get_missing_letters("zyxwvutsrq"))
print(get_missing_letters("abc"))
print(get_missing_letters("abcdefghijklmnopqrstuvwxyz"))'''


'''
binary = [1,0,0]

def convert(bin):
    # powers = [1,2,4,8,16,32,64,128,256]
    powers = [256,128,64,32,16,8,4,2,1]
    dec = 0

    for bit in range(len(bin)-1, -1, -1):
        dec = dec + bin[bit] * powers[len()]
    
    return dec

print(convert(binary))'''

from math import sqrt

def solutions(li):
    try:
        x1 = ((-1*li[1]) + sqrt((li[1]**2)-(4*li[0]*li[2]))) / (2 * li[0])
        x2 = ((-1*li[1]) - sqrt((li[1]**2)-(4*li[0]*li[2]))) / (2 * li[0])
    except ValueError:
        return 0

    if x1 == x2:
        return 1
    else:
        return 2

solutions([1,0,1])