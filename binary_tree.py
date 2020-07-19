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

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class queue:
    def __init__(self):
        self.items=[]


    def enqueue(self,val):
        self.items.insert(0,val)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items)==0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def print_queue(self):
        print(self.items)

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

    def find(self,data):
        if self.root is None:
            print("tree is empty")
        else:
            is_found=self._find(data,self.root)
            return is_found

    def _find(self,data,cur_node):
        if data<cur_node.data and cur_node.left:
            return self._find(data,cur_node.left)
        elif data > cur_node.data and cur_node.right:
            return self._find(data,cur_node.right)
        elif data==cur_node.data:
            return True
        else:
            return False

    def inorder(self):
        if self.root is None:
            return
        self._inorder(self.root)
    def _inorder(self,cur_node):
        if cur_node is None:
            return
        self._inorder(cur_node.left)
        print(cur_node.data)
        self._inorder(cur_node.right)

    def remove(self,data):
        if self.root is None:
            return
        self._remove(data,self.root)

    def _remove(self,data,cur_node):
        if cur_node is None:
            return None
        elif cur_node.data < data:
            cur_node.right = self._remove(data,cur_node.right)
        elif cur_node.data > data:
            cur_node.left = self._remove(data, cur_node.left)
        else:
            if cur_node.left is None and cur_node.right is None:
                return None
            elif cur_node.left is None:
                temp = cur_node.right
                return temp
            elif cur_node.right is None:
                temp = cur_node.left
                return temp
            else:
                rmin = self.rightmin(cur_node.right)
                cur_node.data = rmin
                cur_node.right = self._remove(rmin,cur_node.right)

        return cur_node

    def rightmin(self,root):
        temp = root
        while temp.left:
            temp = temp.left
        return temp.data


    def print_tree(self,trav_type):
        if trav_type=="preorder":
            return self.preorder(self.root,"")
        elif trav_type=="inorder":
            return self.inorder_print(self.root,"")

        elif trav_type=="postorder":
            return self.post_order(self.root,"")

        elif trav_type=="levelorder":
            return self.level_order(self.root)

        elif trav_type=="reverselevelorder":
            return self.rev_level_order(self.root)

        elif trav_type=="ht":
            return self.height(self.root)

        elif trav_type=="size":
            return self.size(self.root)
        elif trav_type=="size_rec":
            return self.size_rec(self.root)

        else:
            print("invalid type")


    def preorder(self,root,trav):
        if root:
            trav+= str(root.data) +"-"
            trav = self.preorder(root.left,trav)
            trav = self.preorder(root.right, trav)
        return trav

    def inorder_print(self,root,trav):
        if root:
            trav = self.inorder_print(root.left,trav)
            trav += str(root.data) + "-"
            trav = self.inorder_print(root.right,trav)
        return trav

    def post_order(self,root,trav):
        if root:
            trav = self.post_order(root.left,trav)
            trav = self.post_order(root.right, trav)
            trav += str(root.data) + "-"

        return trav

    def level_order(self,root):
        if root is None:
            return
        q1=queue()
        q1.enqueue(root)
        trav=""
        while len(q1)>0:
            trav += str(q1.peek().data) +"-"

            node = q1.dequeue()
            if node.left:
                q1.enqueue(node.left)
            if node.right:
                q1.enqueue(node.right)
        return trav

    def rev_level_order(self,root):
        if root is None:
            return
        q1=queue()
        s1=stack()
        q1.enqueue(root)
        trav=""
        while len(q1)>0:
            node=q1.dequeue()
            s1.push(node)
            if node.right:
                q1.enqueue(node.right)
            if node.left:
                q1.enqueue(node.left)
        while len(s1)>0:
            trav+=str(s1.pop().data)+"-"
        return trav

    def height(self,node):
        if node is None:
            return -1
        left = self.height(node.left)
        right = self.height(node.right)
        return 1+max(left,right)

    def size(self,root):
        if root is None:
            return 0
        n=1
        s1 = stack()
        s1.push(root)
        while s1:
            node = s1.pop()
            if node.left:
                s1.push(node.left)
                n+=1
            if node.right:
                s1.push(node.right)
                n+=1
        return n

    def size_rec(self,root):
        if root is None:
            return 0
        return 1+self.size_rec(root.left)+self.size_rec(root.right)
















b1=tree()
b1.insert(100)
b1.insert(20)
b1.insert(300)
b1.insert(15)
b1.insert(25)

#b1.remove(200)

print("preorder",b1.print_tree("preorder"))
print("inorder",b1.print_tree("inorder"))
print("postorder",b1.print_tree("postorder"))
print("levelorder",b1.print_tree("levelorder"))
print("reverselevelorder",b1.print_tree("reverselevelorder"))

print("height",b1.print_tree("ht"))
print("size",b1.print_tree("size"))
print("size_rec",b1.print_tree("size_rec"))

#b1.inorder()

