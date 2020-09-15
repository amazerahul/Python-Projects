import math
import string
def change(a):
    a=list(a)
    str=""
    for i in a:
        i=ord(i)
        i=i-10
        i=chr(i)
        str=str+i
    return str
    

def unchange(a):
    a=tuple(a)
    str=""
    for i in a:
        i=ord(i)
        i=i+10
        i=chr(i)
        str=str+i
    return str
        
print(unchange("bcd"))
