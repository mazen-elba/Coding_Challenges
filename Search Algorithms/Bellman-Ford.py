# --- Algorithm Implementation
from collections import defaultdict

# A class representing a graph
class Graph: 
	
	# constructor  
    def __init__(self, vertices): 
        self.V = vertices # Number of vertices 
        self.graph = [] # default dictionary to store graph 
   
    # function to add an edge to graph 
    def addEdge(self, u, v, w): 
        self.graph.append([u, v, w]) 
          
    # utility function to print the solution 
    def printArr(self, dist): 
        print("Vertex   Distance from Source") 
        for i in range(self.V): 
            print("% d \t\t % d" % (i, dist[i])) 
      
    # Bellman-Ford's Algorithm (finds shortest distances from src to; also detects negative weight cycle)
    def BellmanFord(self, src): 
  
        # (Step 1) initialize distances from src to all other vertices as INFINITE 
        dist = [float("Inf")] * self.V 
        dist[src] = 0 
  
        # (Step 2) relax all edges |V|-1 times (shortest path from src to any other vertex can have at-most |V|-1 edges) 
        # guarantees shortest distances if graph doesn't contain negative weight cycle
        for i in range(self.V - 1): 
            # update dist value and parent index of adjacent vertices of the picked vertex (consider only those vertices which are still in queue)
            for u, v, w in self.graph: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        dist[v] = dist[u] + w 
  
        # (Step 3) check for negative-weight cycles 
        #... if we get a shorter path, then there is a cycle. 
        for u, v, w in self.graph: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        print "Graph contains negative weight cycle"
                        return
                          
        # print all distances 
        self.printArr(dist) 

# --- Driver Program to Test Algorithm  
g = Graph(5) 
g.addEdge(0, 1, -1) 
g.addEdge(0, 2, 4) 
g.addEdge(1, 2, 3) 
g.addEdge(1, 3, 2) 
g.addEdge(1, 4, 2) 
g.addEdge(3, 2, 5) 
g.addEdge(3, 1, 1) 
g.addEdge(4, 3, -3) 
  
# print the solution 
g.BellmanFord(0) 

# Note
# 	- Negative weights are found in various applications of graphs
# 	- Bellman-Ford works better for distributed systems (edges are considered one by one)