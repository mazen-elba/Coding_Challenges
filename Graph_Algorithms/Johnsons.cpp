// Johnson's Algorithm(all-pairs shortest path) 1. Add a new vertex "s" to the graph
//         Add edges from new vertext to all vertices -
//     G' = modified graph 2. Run Bellman - Ford algorithm on G' with "s" as source - Let distances calculated be h[0],
//     ..h[V - 1] - If we find a negative weight cycle, return -Negative weight cycles cannot be created by new vertex "s"(there is no edge to "s" all edges are from "s")3. Re - weight edges of original graph - For each edge(u, v) assign the new weight as "original weight + h[u] - h[v]" 4. Remove added vertex "s" & run Dijkstra's algorithm for every vertex

//                                                             Time Complexity : O(V ^ 3 + V * E);
// Dijstra's algorithm takes O(n^2) for adjacency matrix - Algorithm can be made more efficient by using adjacency list to represent graph(instead of adjacency matrix)

// --- Algorithm Implementation
#include <iostream>
#define INF 999

using namespace std;

int min(int a, int b);
int cost[10][10], adj[10][10];

inline int min(int a, int b)
{
    return (a < b) ? a : b;
}

int main()
{
    int vert, edge, i, j, k, c;
    cout << "Enter number of vertices: ";
    cin >> vert;
    cout << "Enter number of edges: ";
    cin >> edge;
    cout << "Enter the Edge Costs:\n";

    // store input into "adj" & "cost" matrix
    for (k = 1; k <= edge; k++)
    {
        cin >> i >> j >> c;
        adj[i][j] = cost[i][j] = c;
    }

    for (i = 1; i <= vert; i++)
    {
        for (j = 1; j <= vert; j++)
        {
            if (adj[i][j] == 0 && i != j)
            {
                // if there is no edge, store infinity
                adj[i][j] = INF;
            }
        }
    }

    for (k = 1; k <= vert; k++)
    {
        for (i = 1; i <= vert; i++)
        {
            for (j = 1; j <= vert; j++)
            {
                // find minimum path from i to j (through k)
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j]);
            }
        }
    }

    cout << "Resultant adjacent matrix\n";

    for (i = 1; i <= vert; i++)
    {
        for (j = 1; j <= vert; j++)
        {
            if (adj[i][j] != INF)
            {
                cout << adj[i][j] << " ";
            }
        }
        cout << "\n";
    }
}