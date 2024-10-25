class Graph2:
    def __init__(self,connections,datasource,id):
        self.connections=connections
        self.datasource=datasource
        self.id=id
    def findPath(self,st,dt):
        paths=[]
        def find(st, dt, vis, trck):
            if st != dt:
                if not vis[dt]:
                    d=self.datasource(dt)
                    if sum(d):
                        pths = [False if i == 0 else True for i in d]
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
            find(st,dt,[False] * len(self.datasource(dt)),[])
        except IndexError:
            return False
        return paths

    def findShortPath(self,st,dt):
        paths={}
        def find(st, dt, vis, cst, trck):
            d = self.datasource(dt)
            if st != dt:
                if not vis[dt]:
                    if sum(d):
                        pths = [False if i == 0 else True for i in d]
                        for i in range(len(pths)):
                            if pths[i]:
                                temp = vis[:]
                                temp[dt] = True
                                t = trck[:]
                                t.append(dt)
                                find(st, i, temp, cst + d[i], t)
            else:
                trck.append(dt)
                paths[str(trck)] = cst + d[st]
        try:
            find(st,dt,[False] * len(self.datasource(dt)),0,[])
        except IndexError:
            return False
        return [list(paths.keys())[list(paths.values()).index(min(paths.values()))],min(paths.values())]


    def getNeighbors(self,degree=1):
        vis=[]
        def getn(n):
            l=[]
            [l.append(i) if i not in vis else None for i in self.datasource(n)]
            return l
        links = {}
        d=1
        q=[[self.id]]
        while d<=degree and len(q):
            t=[]
            for n in q[d-1]:
                vis.append(n)
                nb = getn(n)
                [t.append(ll) for ll in nb]
                for i in nb:
                    if not links.get(str((self.id,i))):
                        links[str((self.id, i))] = d
            q.append(t)
            d+=1
        return links