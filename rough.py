class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None

    def insert(self,key):
        if self.root is None:
            self.root = node(key)
        else:
            self._insert(key,self.root)

    def _insert(self,data,cur_node):
        if data<cur_node.data:
            if cur_node.left is None:
                cur_node.left=node(data)
            else:
                self._insert(data,cur_node.left)
        elif data>cur_node.data:
            if cur_node.right is None:
                cur_node.right=node(data)
            else:
                self._insert(data,cur_node.right)
        else:
            print("value ",data,"already present in tree")

    def print_tree(self,trav_type):
        if trav_type=="size":
            tmp=[]
            return self.size(self.root,tmp)

    def size(self,root,temp):
        if root:
            temp.append(root.data)
            temp = self.preorder(root.left,temp)
            temp = self.preorder(root.right,temp)
        return temp

b1=tree()
b1.insert(100)
b1.insert(20)
b1.insert(300)
b1.insert(15)
b1.insert(25)
print("size",b1.print_tree("size"))