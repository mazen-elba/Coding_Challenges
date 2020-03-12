# A* Algorithm - Path Finding/Motion Planning:
# 1. Initialize the open list
# 2. Initialize the closed list - put the starting node on the open list (can leave its "f" at 0)
# 3. While the open list is not empty
#	a. find the node with the least "f" on the open list - call it "q"
#	b. pop "q" off the open list
#	c. generate "q"s 8 successors and set their parents to "q"
#	d. for each successor
#		i. if successor is the goal, stop search
#			successor.g = q.g + distance between successir and q
#			successor.h = distance from goal to successor via Heuristics (Manhattan, Diagonal, Euclidean Distance)
#				(Manhattan) h = abs() + abs()
#				(Diagonal) h = max{abs(), abs()}
#				(Euclidean) h = sqrt((current_cell.x - goal.x)2 + (current_cell.y - goal.y)2)
#			successor.f = successor.g + successor.h
#		ii. if a node with the same position as successor is in the OPEN list (which has a lower "f" than succssor), skip this successor
#		iii. if a node with the same position as successor is in the CLOSED list (which has a lower "f" than successor), skip this successor; otherwise, add the node to the open list
# (end for loop)
#	e. push "q" on the closed list
# (end while loop)

# --- Algorithm Implementation
class Node():

	# constructor
	def __init__(self, parent=None, position=None):
		self.parent = parent
		self.position = position
		self.g = 0
		self.h = 0
		self.f = 0

	def __eq__(self, other):
		return self.position == other.position

# A-star Algorithm
def astar(maze, start, end):
    # create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # initialize both open and closed list
    open_list = []
    closed_list = []

    # add the start node
    open_list.append(start_node)

    # loop until you find the end
    while len(open_list) > 0:

        # get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # return reversed path

        # generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # create new node
            new_node = Node(current_node, node_position)

            # append
            children.append(new_node)

        # loop through children
        for child in children:
            # child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # add the child to the open list
            open_list.append(child)

# --- Driver Program to Test Algorithm
def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    print(path)

if __name__ == '__main__':
    main()

# --- Analysis
# Time Complexity: O(E) worst-case; E = number of edges
# Space Complexity: O(V) worst-case; V = total number of vertices
# Limitations: does not always produce shortest path; relies on heuristics/approximations to calculate "h"
# Implementation: dynamic programming, and use set data structure and boolean hash tables for a closed list
# NB: Dijkstra is a special case of A* Algorithm, where h = 0 for all nodes
# Manhattan Distance Heuristics (approximations to calculate "h"; less time-consuming)
#	- Sum of absolute values of differences in the goal's x-/y-coordinates, and current cell's x-/y-coordinates (respectively)
# 	- Used when allowed to move only in 4 directions (right, left, top, bottom)
# f = sum of two parameters ("g" + "h"); next cells picked with lowest "f"
# g = movement cost to move from starting point to a given square on the grid (following path generated to get there)
# h = estimated movement cost to move from given square on the grid to final destination (ie; heuristics)
# Diagonal Distance Heuristics
#	- Maximum of absolute values of difference in the goals' x-/y-coordinates, and current cell's x-/y-coordinates (respectively)
#	- Used when allowed to move in 8 directions only (ie; a King in Chess)#Euclidean Distance Heuristics
# 	- Distance between current cell and goal cell 
#	- Used when allowed to move in any direction