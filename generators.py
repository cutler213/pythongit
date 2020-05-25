def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1

vals=topten()

print(vals.__next__())
print(next(vals))

print()
## or ##

for i in vals:
    print(i)