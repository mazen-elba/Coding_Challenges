// Dijkstra's Algorith - shortest path from all vertices
// 1. Create a set "sptSet" (shortest path tree set) that keeps track of vertices included in shortest path tree
// 2. Assign a distance value to all vertices in the graph
// 		- Initialize all distance values as infinite
//		- Assign distance value as 0 for source vertex (so it is picked up first)
// 3. While "sptSet" does not include all vertices
//		- Pick a vertex "u" which is not in "sptSet" and has minimum distance value
//		- Include "u" to "sptSet"
// 		- Update distance value to all adjacent vertices of "u" (to update distance values, iterate through all adjacent vertices)
//			- For every adjacent vertext "v", if (sum of distance value of "u" (source) & weight of edge "u-v") < distance value of "v", tupdate distance value of "v"

// # --- Algorithm Implementation
#include <limits.h>
#include <stdio.h>

// Number of vertices in graph
#define V 9

// A utility fx to find vertex with minimum distance value (from set of vertices not yet included in shortest path tree)
int minDistance(int dist[], bool sptSet[]){
	// initialize min value
	int min = INT_MAX, min_index;

	for (int v = 0; v < V; v++){
		if (sptSet[v] == false && dist[v] <= min){
			min = dist[v], min_index = v;
		}
	}

	return min_index;
}

// A utility fx to print the constructed distance array
int printSolution(int dist[]){
	printf("Vertex \t\t Distance from Source\n");
	for (int i = 0; i < V; i++){
		printf("%d \t\t %d\n", i, dist[i]);
	}
}

// Dijsktra's Algorithm
void dijkstra(int graph[V][V], int src){
	// output array (dist[i] will hold shortest distance from src to i)
	int dist[V];

	// sptSet[i] will be true if vertex i is included in shortest path tree or shortest distance from src to i is finalized
	bool sptSet[V];

	// initialize all distances as INFINITE and sptSet as false
	for (int i = 0; i < V; i++){
		dist[i] = INT_MAX, sptSet[i] = false;
	}

	// distance of source vertext from itself is always 0
	dist[src] = 0;

	// find shortest path for all vertices
	for (int count = 0; count < V-1; count++){
		// pick minimum distance from set of vertices not yet processed (u always equals to src in first iteration)
		int u = minDistance(dist, sptSet);

		// mark the picked vertex as processed
		sptSet[u] = true;

		// update dist value of adjacent vertices of picked vertex
		for (int v = 0; v < V; v++){
			// update dist[v] only if not in sptSet
			//... there is an edge from u to v 
			//... and total weight of path from src to v (through u) is smaller than current value of dist[v]
			if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v]){
				dist[v] = dist[u] = graph[u][v];
			}
		}
	}

	// print constructed distance array
	printSolution(dist);
}

// --- Driver Program to Test Algorithm
int main(){
	// example graph
	int graph[V][V] = {
		{ 0, 4, 0, 0, 0, 0, 0, 8, 0 }, 
        { 4, 0, 8, 0, 0, 0, 0, 11, 0 }, 
        { 0, 8, 0, 7, 0, 4, 0, 0, 2 }, 
        { 0, 0, 7, 0, 9, 14, 0, 0, 0 }, 
        { 0, 0, 0, 9, 0, 10, 0, 0, 0 }, 
        { 0, 0, 4, 14, 10, 0, 2, 0, 0 }, 
        { 0, 0, 0, 0, 0, 2, 0, 1, 6 }, 
        { 8, 11, 0, 0, 0, 0, 1, 0, 7 }, 
        { 0, 0, 2, 0, 0, 0, 6, 7, 0 }
	};

	dijkstra(graph, 0);

	return (0);
}

// Time Complexity: O(V^2)
//	- If graph is represented using adjacency list, time complexity can be reduced to O(E log V) with binary heap
// NB:
//	- Algorithm calculates shortest distance, not path information
// 	- Code is for undirected graph, but can be implemented on direct graphs
// 	- Code finds shortest distance from source to all vertices
//		- For shortest distance from source to a single target, break the for loop when the picked minimum distance vertext = target
// 	- Algorithm does not work for graphs with negative weight edges
//		- For graphs with negative weight edge use Bellman-Ford algorithm 