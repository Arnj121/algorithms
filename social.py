from Graph2 import Graph2
import  pprint
import random
from tree import Tree

def generateFriends(n,c):
    adjacency_list = {i: set() for i in range(n)}
    for friend in range(n):
        tc=random.randint(int(c/2),c)
        while len(adjacency_list[friend]) < tc:
            connect_friend = random.randint(0, n - 1)
            if connect_friend != friend and connect_friend not in adjacency_list[friend]:
                adjacency_list[friend].add(connect_friend)
                adjacency_list[connect_friend].add(friend)

    adjacency_list = {friend: list(connections) for friend, connections in adjacency_list.items()}
    pprint.pprint(adjacency_list)
    return adjacency_list

# alist=generateFriends(10,3)

# def datasource(args):
#     return alist[args]

l={
    0:[1,2,3],
    1:[4,5],
    2:[6,7],
    3:[8,9,10],
    4:[11],
    6:[12,13],
    8:[14,15],
    10:[16,17],
}

tree=Tree(l,0)
tree.insert(6,18)
print(tree.search(9))
