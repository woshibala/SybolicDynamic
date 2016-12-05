import networkx as nx
import matplotlib.pyplot as plt


def build_DFA(nodes,edges,alphabet):
	G=nx.DiGraph()
	G.add_node(0)#add accept node 0
	G.add_nodes_from(nodes)
	G.add_weighted_edges_from(edges)
	
	# Construct DFA
	for node in G.nodes():
		out_edges_label = set()
		if node != 0:
			for edge in G.successors(node):
				out_edges_label.add(G[node][edge]['weight'])
			new_edge = []
			for label in alphabet.difference(out_edges_label):
				new_edge.append((node,0,label))
			G.add_weighted_edges_from(new_edge)
	return G

def Hopcroft(DFA):
	state_sets = []
	acc_state = {0}
	normal_state = set(DFA.nodes()).difference(acc_state)
	state_sets.append(acc_state)
	state_sets.append(normal_state)
	for state in acc_state:
		DFA[state]['set'] = 0
	for state in normal_state:
		DFA[state]['set'] = 1

	label = 0
	for state in DFA.nodes():
		for i in DFA.successors(state):
			if DFA[i]['label'] == label:
				DFA[state]['out_state'] = DFA[i]['set']

	for state in DFA.nodes():
		print state,DFA[state]['out_state']




	'''label = 1
	DFA[1]['set'] = 123
	print DFA[1]['set']
	for state_set in state_sets:
		for state in state_set:
			for




	print acc_state
	print normal_state'''




	


	#print G.successors(1)
	#print G.nodes()
	#nx.draw(G)
	#plt.show()

def main(nodes,edges,alphabet):
	DFA = build_DFA(nodes,edges,alphabet)
	Hopcroft(DFA)

alphabet = set([0,1])
nodes = [1,2,3,4]
edges = [(1,2,0),(2,3,0),(3,4,0),(4,1,0),(1,1,1),(3,3,1)]
main(nodes,edges,alphabet)

