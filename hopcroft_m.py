import networkx as nx
import matplotlib.pyplot as plt


def build_DFA(G,alphabet):

	# add final state
	G.add_node('f')

	# Construct DFA
	for node in G.nodes():
		out_edges_symbol = set()
		if node != 'f': # if node is not final state

			for edge in G.edges(node): # add on the symbol to out_edges_symbol
				# G[edge[0]][edge[1]] = {0: {'symbol': 1}}
				#print G[edge[0]][edge[1]][0]['symbol']
				out_edges_symbol.add(G[edge[0]][edge[1]][0]['symbol'])

			new_edges = [] # add edge to final state
			for symbol in alphabet.difference(out_edges_symbol):
				new_edges.append((node, 'f' ,{'symbol': symbol}))
				#print(new_edges)
			G.add_edges_from(new_edges)
	return G

def Hopcroft(DFA, alphabet):

	F = set('f')
	Fc = set(DFA.nodes()).difference(F)
	P = [Fc,F]

	W = [] # waiting list
	for a in alphabet:
		W.append(('f',a))

	while len(W) != 0:
		print (len(W))
		# choose and remove
		(C, a) = W[0]
		W.remove(W[0])

		for B in P:
			# if (C, a) can split B
			Bp, Bpp = Split(B, C, a, DFA, P)
			if (len(Bp) == 0 or len(Bpp) == 0):
				print ('continue')
				continue
			# replace B by Bp and Bpp in P
			P.remove(B)
			P.append(Bp)
			P.append(Bpp)
			for b in alphabet:
				if ((B,b) in W):
					#replace (B, b) by (Bp, b) and (Bpp, b) in W
					W.remove((B, b))
					W.append((Bp, b))
					W.append((Bpp, b))
				else:
					if len(Bp) < len(Bpp):
						W.append((Bp, b))
					else:
						W.append((Bpp, b))

	print("Done!!!")
	print ("Partition:"),P

def Split(B, C, a, DFA, P): # return a dictionary
	cSet = set()
	nonSet = set()
	setDict = {}
	# pop(): remove and return an arbitrary element from s;
	"""
	for item in P:
		element = item.pop()
		item.update(element)
		setDict[element] = item
	"""
	#print "dictionary",setDict
	# Track which set it goes
	track = {}
	# Check if B split by (C, a)
	for node in B:
		edge_list = DFA.edges(node, data=True)
		for edge in edge_list:
			if (edge[2]['symbol'] == a):
				if (edge[1] == C):
					cSet.add(node)
				else:
					nonSet.add(node)

	return nonSet, cSet


def makeGraph():
	G = nx.MultiDiGraph()
	G.add_edges_from([('A','B',{'symbol': 0}), ('A', 'A', {'symbol':1}),('B', 'C', {'symbol':0}),('C', 'C', {'symbol':1}),('C', 'D', {'symbol':0}),
	('D', 'A', {'symbol':0})])
	return G

def main():
	alphabet = set([0,1])
	G = makeGraph()
	DFA = build_DFA(G, alphabet)
	#nx.draw(G)
	#plt.show()
	Hopcroft(DFA, alphabet)

'''alphabet = set([0,1])
nodes = [1,2,3,4]
edges = [(1,2,0),(2,3,0),(3,4,0),(4,1,0),(1,1,1),(3,3,1)]
'''
main()
