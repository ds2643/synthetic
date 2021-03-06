import numpy as np
''' note: graph represented natively as an adj matrix, but for large sets of data not strongly connected, adj list may be more economic in memory use. However, '''

class Graph:
	''' graph object '''
	def __init__(self, label, weight=False, directed=True):
		''' internal rep as adjacency matrix regardless of density'''
		self.label = label
		self.weight = weight
		self.directed = directed
		self.t = np.float64 if weight else np.bool
		self.adj_mat = np.zeros((0,0),dtype=self.t)
		self.meta = []
	def __repr__(self):
		return self.label 
	def add_node(self,val):
		''' insert new node into graph-- pass if label already in use '''
		if (not self.meta.__contains__(val)):
			self.meta.append(val)
			self.adj_mat = np.resize(self.adj_mat,(len(self.meta),len(self.meta)))
	def edge(self,n1,n2,w=1):
		''' specify value for edge... defaults to True/1 '''
		try: n1 in self.meta and n2 in self.meta
		except ValueError: "must add edges individually before setting edge"
		i = self.meta.index(n1)
		j = self.meta.index(n1)
		self.adj_mat[i][j] = w
		if (not self.directed):
			self.adj_mat[j][i] = w
	def del_edge(self,x,y):
		''' remove edge by setting to default value of 0 weight or False '''
		i = self.meta.index(x)
		j = self.meta.index(y)
		self.adjMat[i][j] = 0
		if (not isDirected()):
			self.adjMat[j][i] = 0
	def adj_list(self):
		''' print an eqv adj list representation '''
		adj_list = dict()
		for i,x in enumerate(self.meta):
			adj_set = set()
			for j,y in enumerate(self.adj_mat[i]):
				if y != 0:
					adj_set.add(self.meta[j])
				else: pass
			adj_list[x] = list(adj_set)
		return adj_list
	def adj_nodes(self,node):
		''' outputs list of adjacent vertices to node '''
		return self.adj_list()[node]
	def get_edge(self,x,y):
		''' what's the value of edge between x and y nodes '''
		i = self.meta.index(x)
		j = self.meta.index(y)
		if (self.meta.__contains__(x) and self.meta.__contains__(y)):
			return self.adj_mat[i,j]
	def audit(self): #add metadata labels for rows
		''' intended to print out graph along with meta data, but not programmed to show row data, even though row and column data are always the same '''
		print self.meta
		print self.adj_mat
	def is_weighted(self):
		''' returns True if graph is weighted '''
		return self.weight
	def is_directed(self):
		''' returns True if graph is directed '''
		return self.directed
	def is_connected(self):
		''' for all nodes in the graph, can any node be reached from any other node? '''
		pass
	def is_tree(self):
		''' is the graph connected and acyclic? '''
		pass
