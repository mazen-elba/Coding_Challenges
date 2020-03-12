#include <bits/stdc++.h>

using namespace std;

// Number of vertices in graph
#define V 4

// Infinite value for vertices not connected to each other
#define INF 99999

// Function to print the solution matrix
void printSolution(int dist[][V]);

// Floyd-Warshall Algorithm (solves all-pairs shortest path)
void floydWarshall(int graph[][V])
{
    // output matrix for shortest distances between every pair of vertices
    int dist[V][V], i, j, k;

    // initialize values of shortest distances based on shortest paths considering no intermediate vertex
    for (i = 0; i < V; i++)
    {
        for (j = 0; j < V; j++)
        {
            dist[i][j] = graph[i][j];
        }
    }

    // add all vertices one-by-one to set of intermediate vertices
    //... before iteration starts, we have shortest distances between all pairs of vertices
    //... after iteration ends, vertex "k" is added to set of intermediate vertices
    for (k = 0; k < V; k++)
    {
        // pick all vertices as source one-by-one
        for (i = 0; i < V; i++)
        {
            // pick all vertices as destination for above picked source
            for (j = 0; j < V; j++)
            {
                // if vertex "k" is on shortest path from "i" to "j", update dist[i][j] value
                if (dist[i][k] + dist[k][j] < dist[i][j])
                {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }

    // print shortest distance matrix
    printSolution(dist);
}

// Utility function to print solution
void printSolution(int dist[][V])
{
    cout << "The following matrix shows the shortest distances between every pair of vertices \n";
    for (int i = 0; i < V; i++)
    {
        for (int j = 0; j < V; j++)
        {
            if (dist[i][j] == INF)
            {
                cout << "INF"
                     << "   ";
            }
            else
            {
                cout << dist[i][j] << "    ";
            }
        }
        cout << endl;
    }
}

// --- Driver Program to Test Algorithm
int main()
{
    /* Let us create the following weighted graph  
            10  
    (0)------->(3)  
        |     /|\  
    5 |     |  
        |     | 1  
    \|/     |  
    (1)------->(2)  
            3     */

    int graph[V][V] = {{0, 5, INF, 10},
                       {INF, 0, 3, INF},
                       {INF, INF, 0, 1},
                       {INF, INF, INF, 0}};

    // print solution
    floydWarshall(graph);

    return 0;
}