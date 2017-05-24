import networkx as nx
import matplotlib.pyplot as plt
import sys
import random


def build_DFA(G,alphabet):
	# add final state
	G.add_node('f')
	# construct DFA 
	for node in G.nodes():
		out_edges_symbol = set()
		if node != 'f': # if node is not final state
			for edge in G.edges(node): # add on the symbols to out_edges_symbol
				out_edges_symbol.add(G[edge[0]][edge[1]][0]['symbol'])
			new_edges = [] # add edges go to final state
			for symbol in alphabet.difference(out_edges_symbol):
				new_edges.append((node, 'f' ,{'symbol': symbol}))
			G.add_edges_from(new_edges)

	return G

def Hopcroft(DFA, alphabet):

	F = set('f')
	P = [F,set(DFA.nodes()).difference(F)] # init partition
	W = [] # init waiting list
	
	for a in alphabet:
		W.append(('f',a))

	while len(W) != 0:
		# choose and remove from waiting list
		(C, a) = W[0]
		W.remove(W[0])

		for B in P:
			# if (C, a) can split B
			Bp, Bpp = Split(B, C, a, DFA, P)
			if (len(Bp) == 0 or len(Bpp) == 0):
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
	return P
	

def Split(B, C, a, DFA, P): # return a dictionary
	#print "split"
	cSet = set()
	nonSet = set()
	setDict = {}

	# Track which set it goes
	track = {}
	# Check if B split by (C, a)
	for node in B:
		edge_list = DFA.edges(node, data=True)
		for edge in edge_list:
			if (edge[2]['symbol'] == a):
				if (edge[1] in C):
					cSet.add(node)
				else:
					nonSet.add(node)

	return nonSet, cSet

def main():
	
	f =  sys.argv[1]
	print "Input file:", f
	fin = open(f,'r')
	alphabet = []
	graph = []
	for line in fin: 
		entry = line.split()
		graph.append((entry[0],entry[1],{'symbol':int(entry[2])}))
		alphabet.append(int(entry[2]))
	fin.close()

	G = nx.MultiDiGraph()
	G.add_edges_from(graph)
	#strongly_connected_components return a generator
	components = list(nx.strongly_connected_components(G)) 
	print "SCC:", components
	isSink = [] # To track if the component is sink
	for comp in components:
		flag = 0
		for i in comp:
			for j in G.edges(i):
				if not j[1] in comp: # if the node goes to another component
					flag += 1
		isSink.append(flag)
	print "isSink:",isSink

	for comp in components: # if the component is sink, remove all its nodes
		if isSink[components.index(comp)] > 0:
			for i in comp:
				G.remove_node(i)


	alphabet = set(alphabet)
	print "Alphabet:",alphabet

	DFA = build_DFA(G, alphabet)
	partition = Hopcroft(DFA, alphabet)
	partition.remove(set(['f']))
	print "Partition:", partition
	fout = open("minimized_" + f, 'w')
	for p in partition:
		for q in partition:
			node1 = random.sample(p, 1)
			for g in graph:
				for h in q:
					if node1[0] == g[0] and h == g[1]:
						print p, q, g[2]
						a = p
						b = q
						a = list(a)
						b = list(b)
						aa = ''
						bb = ''
						for i in a:
							aa = aa + i
						for i in b:
							bb = bb + i
						line = aa + ' ' + bb + ' ' + str(g[2]['symbol']) + '\n'
						fout.write(line)
	fout.close()
	print "Done! See result in file: minimized_" + f

	
main()
#Contact GitHub API Training Shop Blog About
