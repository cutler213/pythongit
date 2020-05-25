row=int(input("enter number of rows"))
col=int(input("enter number of columns"))

print("enter matrix m1 values")

m1=[[int(input()) for i in range(col)] for j in range(row)]

print(("matrix m1 is : "))

for i in range(row):
    for j in range(col):
        print(format(m1[i][j],"<3"),end=" ")
    print()

print("enter matrix m2 values")

m2=[[int(input()) for i in range(col)] for j in range(row)]

print(("matrix m2 is : "))

for i in range(row):
    for j in range(col):
        print(format(m2[i][j],"<3"),end=" ")
    print()

re=[[0 for i in range(col)] for j in range(row)]

for i in range(row):
    for j in range(col):
        re[i][j]=m1[i][j] + m2[i][j]
print("resultant matrix is : ")
for i in range(row):
    for j in range(col):
        print(format(re[i][j],"<3"),end=" ")
    print()

print("num of cols :")
print(len(re[0]))