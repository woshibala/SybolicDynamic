import networkx as nx



"""
Start: put all nodes in the same set
Iterate: Go throught the language as inputs, and if that input is an edge out of the node, do not
change the set, if it does not exsist, put that node into a 'reject' set
Stop: once the sets are static
"""

"""
G.edges(data=True) -> A list of edges, in the form of tuples (Node, Neighbor, Data)
"""

def makeGraph():
    G = nx.MultiDiGraph()
    G.add_edges_from([('A','B',{'symbol': 0}), ('A', 'A', {'symbol':1}),('B', 'C', {'symbol':0}),('C', 'C', {'symbol':1}),('C', 'D', {'symbol':0}),
    ('D', 'A', {'symbol':0})])
    return G

def split(P, Ca, G):
    acc = []
    rej = []
    for p in P:
        for node in p:
            if (Ca in [symb[2]['symbol'] for symb in G.edges([node], data=True)]):
                #If the symbol exists in the edges coming from the node
                acc.append(node)
            else:
                rej.append(node)

    return acc, rej


if __name__ == "__main__":
    G = makeGraph()
    #TODO: Make language modular for the graph
    language = [0,1]

    P = [set(G.nodes())]
    W = []
    for sym in language:
        W.append(sym)

    while (W):
        Ca = W[0]
        W.remove(Ca)
        for each in P:
            print (each)
            B_v = split(P, Ca, G)
            print (B_v)
