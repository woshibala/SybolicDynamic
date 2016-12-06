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

def split(x, Ca, G):
    acc = []
    rej = []
    newX = dict()
    for p in P:
        for node in p:
            if (not(Ca in [symb[2]['symbol'] for symb in G.edges([node], data=True)])):
                #If the symbol exists in the edges coming from the node
                rej.append(node)
            else:
                #li is the node that is pointed to by 'node' on the symbol 'Ca'
                endPoint = [symb[1] for symb in G.edges([node], data=True) if symb[2]['symbol'] == Ca][0]
                #set that li belongs to, to see if it is different than the set of what 'node' belongs to
                setOfEndPoint = x[endPoint]

                #if the set that the node pointed to by node on the symbol Ca is differnt than the set that node belongs to
                if (setOfEndPoint != x[node]){
                    
                }



    return acc, rej


if __name__ == "__main__":
    G = makeGraph()
    language = [0,1]
    #Build dictionary of node->set relationships
    x = dict()
    for node in G.nodes():
        x[node] = G.nodes()

    P = [set(G.nodes()), []]
    W = []
    for sym in language:
        W.append(({'f'}, sym))

    while (W):
        Ca = W[0]
        W.remove(Ca)
        for each in P:
            print (each)
            B_v = split(x, Ca, G)
            print (B_v)
