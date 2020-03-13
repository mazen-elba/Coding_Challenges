# Johnson's Algorithm(all-pairs shortest path)
# 1. Add a new vertex "s" to the graph
# Add edges from new vertext to all vertices
# - G' = modified graph
# 2. Run Bellman-Ford algorithm on G' with "s" as source
# - Let distances calculated be h[0], ..h[V-1]
# - If we find a negative weight cycle, return
# - Negative weight cycles cannot be created by new vertex "s" (there is no edge to "s"
#                                                               all edges are from "s")
# 3. Re-weight edges of original graph
# - For each edge(u, v) assign the new weight as "original weight + h[u] - h[v]"
# 4. Remove added vertex "s" & run Dijkstra's algorithm for every vertex

# Time Complexity: O(V^3 + V * E); Dijstra's algorithm takes O(n^2) for adjacency matrix
#   - Algorithm can be made more efficient by using adjacency list to represent graph (instead of adjacency matrix)

# --- Algorithm Implementation
from collections import defaultdict

MAX_INT = float("Inf")

# Utility function to return vertex with minimum distance from the source


def minDistance(dist, visited):
    (minimum, minVertex) = (MAX_INT, 0)
    for vertex in range(len(dist)):
        if minimum > dist[vertex] and visited[vertex] == False:
            (minimum, minVertex) = (dist[vertex], vertex)

    return minVertex

# Dijkstra's Algorithm (modified by removing negative weights)


def Dijkstra(graph, modifiedGraph, src):
    num_vertices = len(graph)
    # dictionary to check if given vertex is already included in shortest path tree
    sptSet = defaultdict(lambda: False)

    # shortest distance of all vertices from the source
    dist = [MAX_INT] * num_vertices
    dist[src] = 0

    for count in range(num_vertices):
        # current vertex which is at minDistance from source & not yet included in shortest path tree
        curVertex = minDistance(dist, sptSet)
        sptSet[curVertex] = True

        for vertex in range(num_vertices):
            if ((sptSet[vertex] == False)
                    and (dist[vertex] > (dist[curVertex] + modifiedGraph[curVertex][vertex]))
                    and (graph[curVertex][vertex] != 0)):
                dist[vertex] = (dist[curVertex] +
                                modifiedGraph[curVertex][vertex])

    # print shortest distance from the source
    for vertex in range(num_vertices):
        print("Vertex " + str(vertex) + ": " + str(dist[vertex]))

# Bellman-Ford Algorithm to calculate shortest distance from source to all other vertices


def BellmanFord(edges, graph, num_vertices):
    # add a source "s" & calculate its minDistance from every other node
    dist = [MAX_INT] * (num_vertices + 1)
    dist[num_vertices] = 0

    for i in range(num_vertices):
        edges.append([num_vertices, i, 0])

    for i in range(num_vertices):
        for (src, des, weight) in edges:
            if ((dist[src] != MAX_INT) and (dist[src] + weight < dist[des])):
                dist[des] = dist[src] + weight

    # do not send the value for the source added
    return dist[0:num_vertices]

# Johnson's Algorithm


def JohnsonAlgorithm(graph):
    edges = []

    # create a list of edges for Bellman-Ford algorithm
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                edges.append([i, j, graph[i][j]])

    # weights used to modify original weights
    modifyWeights = BellmanFord(edges, graph, len(graph))
    modifiedGraph = [[0 for x in range(len(graph))] for y in range(len(graph))]

    # modify weights to get rid of negative weights
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                modifiedGraph[i][j] = (
                    graph[i][j] + modifyWeights[i] - modifyWeights[j])

    print("Modified Graph: " + str(modifiedGraph))

    # run Dijkstra for every vertex as source one-by-one
    for src in range(len(graph)):
        print("\nShortest Distance with vertex " +
              str(src) + " as the source:\n")
        Dijkstra(graph, modifiedGraph, src)


# --- Driver Program to Test Algorithm
graph = [[0, -5, 2, 3],
         [0, 0, 4, 0],
         [0, 0, 0, 1],
         [0, 0, 0, 0]]

JohnsonAlgorithm(graph)
