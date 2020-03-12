# Time Complexity: O(V+E), where V = number of vertices, and E = number of edges in graph 
# NB: 
#	- Traverses only on vertices reachable from a given source vertex
# 	- All vertices may not be reachable from a given vertex (ie; disconnected graph)
# 	- To print all vertices, modify function to do traversal starting from all nodes one-by-one
# 	- To avoid processing a node more than once, use a boolean visited array
# 	- For simplicity, assume all vertices are reachable from starting vertex

# --- Algorithm Implementation
from collections import defaultdict

# A directed graph (using adjacency list representation)
class Graph:

	# constructor
	def __init__(self):
		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# BFS Algorithm
	def BFS(self, s):
		# mark all vertices as not visited
		visited = [False] * (len(self.graph))

		# create a queue for BFS
		queue = []

		# mark source node as visited & enqueue it
		queue.append(s)
		visited[s] = True 

		while queue:
			# dequeue a vertex from queue & print it
			s = queue.pop(0)
			print(s)

			# get all adjacent vertices of dequeued vertex "s"
			# if an adjacent has not been visited, mark it visited & enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True 

# --- Driver Program to Test Algorithm
# create a graph
g = Graph()

g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)

print("Following is Breadth-First Traversal (starting from vertext 2")
g.BFS(2)
