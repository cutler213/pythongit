s1 = "a,b@#c"



def rever(s1):
    r = len(s1) - 1
    l = 0
    while l<r:
        s2=""
        if not s1[l].isalpha():
            l+=1
        elif not s1[r].isalpha():
            r-=1
        else:
            s1[l],s1[r]=s1[r],s1[l]
            l+=1
            r-=1
    return s1

print(s1)
print("".join(rever(list(s1))))