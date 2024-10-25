class Graph:

    def __init__(self,matrix,nodeLabels=None):
        self.matrix=matrix
        if nodeLabels is None:
            nodeLabels={}
        self.nodeLabels=nodeLabels

    def findPath(self,st,dt):
        paths=[]
        def find(st, dt, vis, trck):
            if st != dt:
                if not vis[dt]:
                    if sum(self.matrix[dt]):
                        pths = [False if i == 0 else True for i in self.matrix[dt]]
                        for i in range(len(pths)):
                            if pths[i]:
                                temp = vis[:]
                                temp[dt] = True
                                t = trck[:]
                                t.append(dt)
                                find(st, i, temp, t)
            else:
                trck.append(dt)
                paths.append(trck)
        try:
            find(st,dt,[False] * len(self.matrix),[])
        except IndexError:
            return False
        return paths

    def findShortPath(self,st,dt):
        paths={}
        def find(st, dt, vis, cst, trck):
            if st != dt:
                if not vis[dt]:
                    if sum(self.matrix[dt]):
                        pths = [False if i == 0 else True for i in self.matrix[dt]]
                        for i in range(len(pths)):
                            if pths[i]:
                                temp = vis[:]
                                temp[dt] = True
                                t = trck[:]
                                t.append(dt)
                                find(st, i, temp, cst + self.matrix[dt][i], t)
            else:
                trck.append(dt)
                paths[str(trck)] = cst + self.matrix[dt][st]
        try:
            find(st,dt,[False] * len(self.matrix),0,[])
        except IndexError:
            return False
        return [list(paths.keys())[list(paths.values()).index(min(paths.values()))],min(paths.values())]

    def traverseAll(self):
        paths={}
        def find(st, vis, trck):
            if not all(vis):
                if not vis[st]:
                    if sum(self.matrix[st]) > 0:
                        pths = [False if i == 0 else True for i in self.matrix[st]]
                        for i in range(len(pths)):
                            if pths[i]:
                                temp = vis[:]
                                temp[st] = True
                                t = trck[:]
                                t.append(st)
                                find(i, temp, t)
            else:
                paths[str(trck)] = 0
                for i in range(len(trck) - 1):
                    paths[str(trck)] += self.matrix[trck[i]][trck[i + 1]]

        for i in range(len(self.matrix)):
            find(i, [False] * len(self.matrix), [])
        return [list(paths.keys())[list(paths.values()).index(min(list(paths.values())))],min(list(paths.values()))]

    def isConnected(self):
        for i in self.matrix[0]:
            if sum(i)==0:
                return False
        return True

    def setLabels(self,names):
        if len(names) != len(self.matrix):
            return
        self.nodeLabels = {i:names[i] for i in range(len(names))}

    def getNeighbors(self,node,degree=1):
        if node >= len(self.matrix):
            return
        vis=[]
        def getn(n):
            l=[]
            [l.append(i) if self.matrix[n][i]!=0 and n!= i and i not in vis else None for i in range(len(self.matrix[n]))]
            return l
        links = {}
        d=1
        q=[[node]]
        while d<=degree and len(q):
            t=[]
            for n in q[d-1]:
                nb = getn(n)
                vis.append(n)
                [t.append(ll) for ll in nb]
                for i in nb:
                    if i!=node:
                        if not links.get(str((node,i))):
                            links[str((node, i))] = d
            q.append(t)
            d+=1
        return links

    def getLabel(self,node):
        return self.nodeLabels[node]
