import random

class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.right=right
        self.left=left
        self.id = random.choice([chr(i) for i in range(65, 90)]) + random.choice([chr(i) for i in range(65, 90)]) + \
                  str(int(random.random() * 1000))
        if value is None and (left is not None or right is not None):
            exit(-1)
    def __str__(self):
        return f"{self.value}:[{self.left},{self.right}]"

class Btree:
    def __init__(self,root=None):
        self.root=root

    def __str__(self):
        if self.root is not None:
            return str(self.root)

    def fromList(self,values):
        self.root=None
        for i in values:
            self.root=self.insert(self.root,i)

    def insert(self,root, key):
        if root is None:
            return Node(key)
        if key < root.value:
            root.left =self.insert(root.left, key)
        else:
            root.right=self.insert(root.right, key)
        return root

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)

    def preorder(self,root):
        if root:
            print(root.value, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value, end=" ")

    def listOrder(self):
        l=[self.root.value]
        def getchild(roots):
            allchild=[]
            for root in roots:
                if root is not None:
                    allchild.append(root.left)
                    allchild.append(root.right)
            return allchild

        child = getchild([self.root])
        while len(child)!=0:
            temp=[]
            for i in child:
                temp.append(i)
                if i is not None:
                    l.append(i.value)
                else:
                    l.append(i)
            child=getchild(temp)
        return l

    def search(self,root,key):
        if root is None:
            return False
        if key == root.value:
            return True
        if key<root.value:
            return self.search(root.left,key)
        else:
            return self.search(root.right,key)

    def sort(self):
        temp=[]
        [temp.append(i) if i is not None else None for i in self.listOrder()]
        self.fromList(sorted(temp))

    def delete(self,key=None,id=None):
        pass


btree=Btree()
btree.fromList([10,6,15,3,8,20])
print(btree.listOrder())