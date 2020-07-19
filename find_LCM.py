n1=int(input("enter 1st num"))
n2=int(input("enter 2nd num"))

if n1>n2:
    higher = n1
else:
    higher=n2

i=1
while True:
    temp = higher*i
    if temp%n1==0 and temp%n2==0:
        print("LCM is", temp)
        break

    i+=1




