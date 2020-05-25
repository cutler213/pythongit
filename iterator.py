class topten:
    def __init__(self):
        self.num=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val

        else:
            raise StopIteration

a1=topten()

print(next(a1))
print()
for i in a1:
    print(i)