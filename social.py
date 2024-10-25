from Graph import Graph
import  pprint

matrix=[[0, 1, 0, 0, 1, 0, 0, 0, 0, 0],  # Friend 1 knows Friend 2 and Friend 5
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],  # Friend 2 knows Friend 1, 3, and 6
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],  # Friend 3 knows Friend 2, 4, and 7
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],  # Friend 4 knows Friend 3 and 8
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # Friend 5 knows Friend 1 and 6
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],  # Friend 6 knows Friend 2, 5, and 8
    [0, 0, 1, 0, 0, 0, 0, 1, 1, 0],  # Friend 7 knows Friend 3, 8, and 9
    [0, 0, 0, 1, 0, 1, 1, 0, 1, 0],  # Friend 8 knows Friend 4, 6, 7, and 9
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],  # Friend 9 knows Friend 7, 8, and 10
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # Friend 10 knows Friend 9
]

g=Graph(matrix)

friends=["Friend1", "Friend2", "Friend3", "Friend4", "Friend5",
           "Friend6", "Friend7", "Friend8", "Friend9", "Friend10"]
g.setLabels(friends)
print(g.findShortPath(0, 3))
# links=g.getNeighbors(7,3)
# pprint.pprint(links)
