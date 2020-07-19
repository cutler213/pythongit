def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)



print(gcd(16,48))


print(48%16)