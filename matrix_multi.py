p=int(input("enter number of rows for m1"))
n=int(input("enter number of columns for m1 or no. or rows of m2"))
q=int(input("enter number of column of m2"))

print("enter matrix m1 values")

m1=[[int(input()) for i in range(n)] for j in range(p)]

print(("matrix m1 is : "))

for i in range(p):
    for j in range(n):
        print(format(m1[i][j],"<3"),end=" ")
    print()

print("enter matrix m2 values")

m2=[[int(input()) for i in range(q)] for j in range(n)]

print(("matrix m2 is : "))

for i in range(n):
    for j in range(q):
        print(format(m2[i][j],"<3"),end=" ")
    print()

re=[[0 for i in range(q)] for j in range(p)]

for i in range(p):
    for j in range(q):
        for k in range(n):
            re[i][j]+=m1[i][k]*m2[k][j]

print("resultant matrix is : ")
for i in range(p):
    for j in range(q):
        print(format(re[i][j],"<3"),end=" ")
    print()