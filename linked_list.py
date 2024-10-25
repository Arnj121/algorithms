import random

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        self.id= random.choice([chr(i) for i in range(65,90)])+random.choice([chr(i) for i in range(65,90)])+\
                 str(int(random.random()*1000))

    def __str__(self):
        return f"val: {self.val}, id: {self.id}"

class LList:

    def __init__(self,head=None):
        self.head=head
        self.len=0
        self.tail=head
        self.cyclic=False
        if type(head) == type([]):
            self.makefromList(head)

    def makefromList(self,values):
        first = Node()
        head = first
        for i in values:
            head.val = i
            head.next = Node()
            self.tail = head
            head = head.next
            self.len+=1
        self.head=first
        self.tail.next=None
        return self

    def parse(self):
        if self.cyclic:
            fid=self.head.id
            temp=self.head
            values=[]
            while temp.next is not None and fid!=temp.next.id:
                if temp.val is not None:
                    values.append(temp.val)
                temp=temp.next
            if temp.val is not None:
                values.append(temp.val)
            return values
        else:
            values = []
            temp=self.head
            while temp.next is not None:
                if temp.val is not None:
                    values.append(temp.val)
                temp = temp.next
            if temp.val is not None:
                values.append(temp.val)
            return values

    def findKey(self,key):
        temp=self.head
        while temp.next is not None and temp.val !=key:
            temp=temp.next
        return temp.val==key

    def getInd(self,index):
        if index>self.len or type(index) != type(1):
            return
        temp=self.head
        ind=0
        while temp.next is not None and ind!=index:
            temp=temp.next
            ind+=1
        return temp.val

    def delInd(self,index):
        if index>self.len or type(index) != type(1):
            return
        temp=self.head
        ind=0
        prev=None
        while temp.next is not None and ind!=index:
            prev=temp
            temp=temp.next
            ind+=1
        if prev is None:
            self.head=temp.next
            return
        if ind==self.len-1:
            prev.next=None
            return
        prev.next=temp.next
        self.len-=1
        return self

    def delKey(self,key):
        temp=self.head
        prev=None
        while temp.next is not None and temp.val!=key:
            prev=temp
            temp=temp.next
        if prev is None:
            self.head=temp.next
            return
        if temp.next is None:
            prev.next = None
            return
        prev.next=temp.next
        self.len-=1
        return self

    def makeCyclic(self):
        self.tail.next=self.head
        self.cyclic=True
        return self

    def unCycle(self):
        self.tail.next=None
        self.cyclic=False
        return self

    def isCyclic(self):
        return self.cyclic

    def reverse(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        temp=self.head
        prev=None
        forw=self.head
        self.tail=self.head
        while temp is not None:
            temp=temp.next
            forw.next=prev
            prev=forw
            if temp is not None:
                forw=temp
        self.head=forw
        return self
