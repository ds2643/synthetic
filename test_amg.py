import amg as g

'''directed unweighted graph DUG'''
print('\n'+"directed unweighted:")
DUG = g.Graph("DUG",False,True)
DUG.add_node('a')
DUG.add_node('b')
DUG.add_node('c')
DUG.add_node('d')
DUG.edge('a','b',1)
DUG.edge('a','c',1)
DUG.edge('a','d',1)
DUG.edge('b','c',1)
print('internal matrix representation:')
DUG.audit()
print("as an adjacency list:")
print str(DUG.adj_list())
print("other tests:")
print ("weighted? " + str(DUG.is_weighted()))
print("directed? " + str(DUG.is_directed()))

''' directed weighted graph DWG '''
print('\n'+"directed weighted:")
DWG = g.Graph("DWG",True,True)
DWG.add_node('a')
DWG.add_node('b')
DWG.add_node('c')
DWG.add_node('d')
DWG.edge('a','b',10)
DWG.edge('a','c',100)
DWG.edge('a','d',1000)
DWG.edge('b','c',10000)
print("internal matrix representation:")
DWG.audit()
print("as an adjacency list:")
print str(DWG.adj_list())
print("other tests:")
print ("weighted? " + str(DWG.is_weighted()))
print("directed? " + str(DWG.is_directed()))

''' undirected unweighted UDUG '''
print('\n'+"undirected unweighted:")
UDUG = g.Graph("UDUG",False,False)
UDUG.add_node('a')
UDUG.add_node('b')
UDUG.add_node('c')
UDUG.add_node('d')
UDUG.edge('a','b',1)
UDUG.edge('a','c',1)
UDUG.edge('a','d',1)
UDUG.edge('b','c',1)
print("internal matrix representation:")
UDUG.audit()
print("adjacency matrix")
print str(UDUG.adj_list())
print("other tests:")
print ("weighted? " + str(UDUG.is_weighted()))
print("directed? " + str(UDUG.is_directed()))

''' undirected weighted UDWG '''
print('\n'+"undirected weighted:")
UDWG = g.Graph("UDWG",True,False)
UDWG.add_node('a')
UDWG.add_node('b')
UDWG.add_node('c')
UDWG.add_node('d')
UDWG.edge('a','b',10)
UDWG.edge('a','c',100)
UDWG.edge('a','d',1000)
UDWG.edge('b','c',10000)
print("internal matrix representation:")
UDWG.audit()
print("adjacency matrix:")
print str(UDWG.adj_list())
print("other tests:")
print ("weighted? " + str(UDWG.is_weighted()))
print("directed? " + str(UDWG.is_directed()))
