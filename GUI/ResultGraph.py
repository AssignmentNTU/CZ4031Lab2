import networkx as nx
import matplotlib.pyplot as plt

def get_graph_of(result_dict):
	graph = nx.Graph()
	author_list = []

	# Iterate through all publication to get list of author involved
	for key in result_dict.keys():
		#Create list of author involved
		involved_author = result_dict[key]
		for author in involved_author:
			if author not in author_list:
				author_list.append(author)

	#Create graph nodes, one node for each author
	#Also label each node with author name accordingly
	for i in range(len(author_list)):
		graph.add_node(i,name=author_list[i])

	#Create graph edge, one edge for each connectivity between author
	# Also label each edge with publication key accordingly
	for key in result_dict.keys():
		pubkey = key
		for i in range (len(result_dict[key])):
			involved_author = result_dict[key]
			author1 = involved_author[i]
			for j in range(i+1, len(involved_author)):
				author2 = involved_author[j]
				'''
				if graph.has_edge(author_list.index(author1), author_list.index(author2)):
					#Append the next pubkey to the current pubkey
					current_pubkey = graph[author_list.index(author1)][author_list.index(author2)]['pubkey']
					new_pubkey = current_pubkey + ', ' + pubkey
					graph[author_list.index(author1)][author_list.index(author2)]['pubkey'] = new_pubkey
				else:
					#Add new edge
					graph.add_edge(author_list.index(author1), author_list.index(author2), pubkey=pubkey)
				'''
				if graph.has_edge(author_list.index(author1), author_list.index(author2)):
					# Append the next pubkey to the current pubkey
					current_no_of_publication = int(graph[author_list.index(author1)][author_list.index(author2)]['no_of_publication'])
					new_no_of_publication = current_no_of_publication + 1
					graph[author_list.index(author1)][author_list.index(author2)]['no_of_publication'] = new_no_of_publication
				else:
					# Add new edge
					graph.add_edge(author_list.index(author1), author_list.index(author2), no_of_publication=1)

	return graph

def get_drawing_of(graph):
	#Source: http://stackoverflow.com/a/20382152
	pos = nx.circular_layout(graph)

	nx.draw(graph, pos)
	#Add node attribute
	node_labels = nx.get_node_attributes(graph, 'name')
	nx.draw_networkx_labels(graph, pos, labels=node_labels)
	#Add edge attribute
	edge_labels = nx.get_edge_attributes(graph, 'title')
	nx.draw_networkx_edge_labels(graph, pos, labels=edge_labels)

	#Display result
	#plt.show()

	#Also, save drawing
	plt.savefig('diagram.png')