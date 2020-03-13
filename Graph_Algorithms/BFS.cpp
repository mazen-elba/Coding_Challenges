// Time Complexity: O(V+E), where V = number of vertices, and E = number of edges in graph 
// NB: 
//	- Traverses only on vertices reachable from a given source vertex
// 	- All vertices may not be reachable from a given vertex (ie; disconnected graph)
// 	- To print all vertices, modify function to do traversal starting from all nodes one-by-one
// 	- To avoid processing a node more than once, use a boolean visited array
// 	- For simplicity, assume all vertices are reachable from starting vertex

#include <iostream>
#include <list>

using namespace std;

// Class represting a directed graph (using adjacency list representation)
class Graph {
	// number of vertices
	int V;

	// pointer to an array containing adjacency lists
	list<int> *adj;

public:
	// constructor
	Graph(int V);

	// function to add an edge to graph
	void addEdge(int v, int w);

	// function to print BFS traversal from a given source "s"
	void BFS(int s); 
};

Graph::Graph(int V){
	this->V = V;
	adj = new list<int>[V];
}

void Graph::addEdge(int v, int w){
	// add weights to vertices' list
	adj[v].push_back(w);
}

// --- BFS Algorithm
void Graph::BFS(int s){
	// mark all vertices as not visited
	bool *visited = new bool[V];
	for (int i=0; i < V; i++){
		visited[i] = false;
	}

	// create a queue for BFS
	list<int> queue;

	// mark current node as visited & enqueue it
	visited[s] = true;
	queue.push_back(s);

	// "i" will be used to get all adjacent vertices of a vertex
	list<int>::iterator i;

	while (!queue.empty()){
		// dequeue a vertex from queue & print it
		s = queue.front();
		cout << s << " ";
		queue.pop_front();

		// get all adjacent vertices of dequeued vertex "s"
		// if an adjacent has not been visited, mark it visited & enqueue it
		for (i=adj[s].begin(); i != adj[s].end(); ++i){
			if (!visited[*i]){
				visited[*i] = true;
				queue.push_back(*i);
			}
		}
	}
}

// --- Driver Program to Test Functions
int main(){
	// create a graph
	Graph g(4);
	g.addEdge(0, 1);
	g.addEdge(0, 2);
	g.addEdge(1, 2);
	g.addEdge(2, 0);
	g.addEdge(2, 3);
	g.addEdge(3, 3);

	cout << "Following is Breadth-First Traversal " << "(starting from vertex 2) \n";
	g.BFS(2);

	return (0);
}