# Dijkstra's Algorith - shortest path from all vertices
# 1. Create a set "sptSet" (shortest path tree set) that keeps track of vertices included in shortest path tree
# 2. Assign a distance value to all vertices in the graph
# 		- Initialize all distance values as infinite
#		- Assign distance value as 0 for source vertex (so it is picked up first)
# 3. While "sptSet" does not include all vertices
#		- Pick a vertex "u" which is not in "sptSet" and has minimum distance value
#		- Include "u" to "sptSet"
# 		- Update distance value to all adjacent vertices of "u" (to update distance values, iterate through all adjacent vertices)
#			- For every adjacent vertext "v", if (sum of distance value of "u" (source) & weight of edge "u-v") < distance value of "v", tupdate distance value of "v"

# Dependency for INT_MAX
import sys

class Graph():

	# constructor
	def __init__(self, vertices):
		self.V = vertices
		self.graph  = [[0 for column in range(vertices)]
						for row in range(vertices)]

	def printSolution(self, dist):
		print("Vertex \tDistance from Source")
		for node in range(self.V):
			print(node, "\t", dist[node])

	# A utility fx to find vertex with minimum distance value (from set of vertices not yet included in shortest path tree)
	def minDistance(self, dist, sptSet):
		# initialize minimum distance for next node
		min = sys.maxint 

		# search nearest vertex not in shortest path tree
		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v

		return min_index

	# Dijsktra's Algorithm
	def dijkstra(self, src):
		dist = [sys.maxint] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):
			# pick minimum distance vertex from set of vertices not yet processed (u always equals to src in first iteration)
			u = self.minDistance(dist, sptSet)

			# put minimum distance vertex in shortest path tree
			sptSet[u] = True

			# update dist value of adjacent vertices of picked vertex only if current distance > new distance
			#... and vertex is not in shortest path tree
			for v in range(self.V):
				if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
					dist[v] = dist[u] = self.graph[u][v]

		self.printSolution(dist)

# --- Driver Program to Test Algorithm
g = Graph(9)

g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
           [0, 0, 2, 0, 0, 0, 6, 7, 0]]

g.dijkstra(0)

# Time Complexity: O(V^2)
#	- If graph is represented using adjacency list, time complexity can be reduced to O(E log V) with binary heap
# NB:
#	- Algorithm calculates shortest distance, not path information
# 	- Code is for undirected graph, but can be implemented on direct graphs
# 	- Code finds shortest distance from source to all vertices
#		- For shortest distance from source to a single target, break the for loop when the picked minimum distance vertext = target
# 	- Algorithm does not work for graphs with negative weight edges
#		- For graphs with negative weight edge use Bellman-Ford algorithm #