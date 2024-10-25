from data import matrix
paths = []

def find(st, vis, trck):
    if not all(vis):
        if not vis[st]:
            if sum(matrix[st]) > 0:
                pths = [False if i == 0 else True for i in matrix[st]]
                for i in range(len(pths)):
                    if pths[i]:
                        temp = vis[:]
                        temp[st] = True
                        t = trck[:]
                        t.append(st)
                        find(i, temp, t)
    elif trck not in paths:
        paths.append(trck)

for i in range(len(matrix)):
    find(i, [False] * len(matrix), [])
print(paths)
