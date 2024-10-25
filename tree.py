class Tree:
    def __init__(self,data,root):
        self.data=data
        self.root=root

    def insert(self,node,key):
        if self.data.get(node):
            self.data[node].append(key)
            return
        self.data[node]=[key]
        return

    def search(self,key):
        def getchild(node):
            if self.data.get(node):
                return self.data[node]
            return []
        f=[False]
        trck=[]
        def find(node,tr):
            child=getchild(node)
            tr.append(node)
            if key in child:
                f[0]=True
                trck.append(tr)
                return
            for i in child:
                t=tr[:]
                find(i,t)

        find(self.root,[])
        return [f[0],trck[0]]

