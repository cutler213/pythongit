class A:
    def __init__(self):
        print("in init A")

    def f1(self):
        print("in f1")

class B(A):
    def __init__(self):

        print("in int B")
        super().__init__()

    def f2(self):
        print("in f2")



b1=B()

