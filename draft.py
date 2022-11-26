

def convert(s):
    listed = []
    tupled = ()
    num = ""
    if s[0].isalpha() and s[1:].isdigit():
        for  i in range(1,len(s)):
            #print(i)
            num += s[i]
        tupled=(*tupled,str(ord(s[0].upper())-65),num)
        listed.append(tupled)
        #print(num)
    return listed
c=input("Enter seat number")
print(convert(c))
print(len(convert(c)))