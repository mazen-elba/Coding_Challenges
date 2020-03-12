# Number of vertices in graph
V = 4

# Infinite value for vertices not connected to each other
INF = 99999

# Floyd-Warshall Algorithm (solves all-pairs shortest path)


def floydWarshall(graph):

    # initialize values of shortest distances based on shortest paths considering no intermediate vertex
    dist = map(lambda i: map(lambda j: j, i), graph)

    # add all vertices one-by-one to set of intermediate vertices
    # ... before iteration starts, we have shortest distances between all pairs of vertices
    # ... after iteration ends, vertex "k" is added to set of intermediate vertices
    for k in range(V):
        # pick all vertices as source one-by-one
        for i in range(V):
            # pick all vertices as destination for above picked source
            for j in range(V):
                # if vertex k is on shortest path from i to j, update dist[i][j] value
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    printSolution(dist)

# Utility function to print the solution


def printSolution(dist):
    print("Fllowing matrix shows the shortest distances between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if (dist[i][j] == INF):
                print("%7s" % ("INF"))
            else:
                print("%7d\t" % (dist[i][j]))

            if j == V-1:
                print("")


# --- Driver Program to Test Algorithm
# Create the following weighted graph
""" 
            10 
       (0)------->(3) 
        |         /|\ 
      5 |          | 
        |          | 1 
       \|/         | 
       (1)------->(2) 
            3           """

graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]]

# Print solution
floydWarshall(graph)
