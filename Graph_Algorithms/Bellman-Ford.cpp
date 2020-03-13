// Bellman-Ford's Algorithm (calculate shortest paths in bottom-up manner)
// 1. Initialize distances from source to all vertices as infinite and distance to source itself as 0
// 	- Create an array dist[] of size |V| with all values as infinite except dist[src] where src is source vertex
// 2. Calculate shortest distances. Do the following for each edge (u-v)
// 	- If dist[v] > dist[u] + weight of edge uv, then update dist[v]
// 		- dist[v] = dist[u] + weight of edge uv
// 3. Report if there is a negative weight cycle in graph. Do the followingfor each edge (u-v)
// 	- If dist[v] > dist[u] + weight of edge uv
// 		- then “Graph contains negative weight cycle”

// --- Algorithm Implementation
#include <bits/stdc++.h>

// A structure to represent a weighted edge in graph
struct Edge {
	int src, dest, weight;
};

// A structure to represent a connected, directed and weighted graph
struct Graph {
	// V = number of vertices; E = number of edges
	int V, E;

	// graph represented as an array of edges
	struct Edge* edge;
};

// Create a graph with vertices (V) and edge (E)
struct Graph* createGraph(int V, int E){
	struct Graph* graph = new Graph;
	
	graph->V = V;
	graph->E = E;
	graph->edge = new Edge[E];

	return graph;
}

// A utility function used to print solution
void printArr(int dist[], int n){
	printf("Vertex Distance from Source\n");
	for (int i = 0; i < n; ++i){
		printf("%d \t\t %d\n", i, dist[i]);
	}
}

// Bellman-Ford Algorithm
void BellmanFord(struct Graph* graph, int src){
	int V = graph->V;
	int E = graph->E;
	int dist[V];

	// (Step 1) initialize distances from src to all other vertices as INFINITE
	for (int i = 0; i < V; i++){
		dist[i] = INT_MAX;
	} 

	dist[src] = 0;

	// (Step 2) relax all edges |V|-1 times (shortest path from src to any other vertex can have at-most |V|-1 edges)
	//... guarantees shortest distances if graph does not contain negative weight cycle
	for (int i = 1; i<= V-1; i++){
		for (int j = 0; j < E; j++){
			int u = graph->edge[j].src;
			int v = graph->edge[j].dest;
			int weight = graph->edge[j].weight;
			if (dist[u] != INT_MAX && dist[u] + weight < dist[v]){
				dist[v] = dist[u] + weight;
			}
		}
	}

	// (Step 3) check for negative-weight cycles
	//... if there is a shorter path, there is a cycle
	for (int i = 0; i < E; i++){
		int u = graph->edge[i].src;
		int v = graph->edge[i].dest;
		int weight = graph->edge[i].weight;
		if (dist[u] != INT_MAX && dist[u] + weight < dist[v]){
			printf("Graph contains negative weight cycle\n");
			return;  // if negative cycle is detected, return
		}
	}

	printArr(dist, V);

	return;
}

// --- Driver Program to Test Algorithm
int main(){
	int V = 5;
    int E = 8; 
    struct Graph* graph = createGraph(V, E); 
  
    // add edge 0-1 (or A-B in above figure) 
    graph->edge[0].src = 0; 
    graph->edge[0].dest = 1; 
    graph->edge[0].weight = -1; 
  
    // add edge 0-2 (or A-C in above figure) 
    graph->edge[1].src = 0; 
    graph->edge[1].dest = 2; 
    graph->edge[1].weight = 4; 
  
    // add edge 1-2 (or B-C in above figure) 
    graph->edge[2].src = 1; 
    graph->edge[2].dest = 2; 
    graph->edge[2].weight = 3; 
  
    // add edge 1-3 (or B-D in above figure) 
    graph->edge[3].src = 1; 
    graph->edge[3].dest = 3; 
    graph->edge[3].weight = 2; 
  
    // add edge 1-4 (or A-E in above figure) 
    graph->edge[4].src = 1; 
    graph->edge[4].dest = 4; 
    graph->edge[4].weight = 2; 
  
    // add edge 3-2 (or D-C in above figure) 
    graph->edge[5].src = 3; 
    graph->edge[5].dest = 2; 
    graph->edge[5].weight = 5; 
  
    // add edge 3-1 (or D-B in above figure) 
    graph->edge[6].src = 3; 
    graph->edge[6].dest = 1; 
    graph->edge[6].weight = 1; 
  
    // add edge 4-3 (or E-D in above figure) 
    graph->edge[7].src = 4; 
    graph->edge[7].dest = 3; 
    graph->edge[7].weight = -3; 
  
    BellmanFord(graph, 0); 
  
    return (0); 
}

// Note
// 	- Negative weights are found in various applications of graphs
// 	- Bellman-Ford works better for distributed systems (edges are considered one by one)