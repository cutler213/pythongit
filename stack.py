class stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items==[]

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def print_stack(self):
        print(self.items)


s=stack()
print(s.is_empty())
s.push(10)
s.push(20)
s.push(30)
s.print_stack()
s.pop()
s.print_stack()
print(s.peek())
print(s.is_empty())
