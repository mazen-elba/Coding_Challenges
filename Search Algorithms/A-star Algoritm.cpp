// A* Algorithm - Path Finding/Motion Planning
// 1. Initialize the open list
// 2. Initialize the closed list - put the starting node on the open list (can leave its "f" at 0)
// 3. While the open list is not empty
//	a. find the node with the least "f" on the open list - call it "q"
//	b. pop "q" off the open list
//	c. generate "q"s 8 successors and set their parents to "q"
//	d. for each successor
//		i. if successor is the goal, stop search
//			successor.g = q.g + distance between successir and q
//			successor.h = distance from goal to successor via Heuristics (Manhattan, Diagonal, Euclidean Distance)
//				(Manhattan) h = abs() + abs()
//				(Diagonal) h = max{abs(), abs()}
//				(Euclidean) h = sqrt((current_cell.x - goal.x)2 + (current_cell.y - goal.y)2)
//			successor.f = successor.g + successor.h
//		ii. if a node with the same position as successor is in the OPEN list (which has a lower "f" than succssor), skip this successor
//		iii. if a node with the same position as successor is in the CLOSED list (which has a lower "f" than successor), skip this successor; otherwise, add the node to the open list
// (end for loop)
//	e. push "q" on the closed list
// (end while loop)

// --- Algorithm Implementation 
#include <bits/stdc++.h>
using namespace std;

#define ROW 9
#define COL 10

// Creating a shortcut for int, int pair type
typedef pair<int, int> Pair;

// Creating a shortcut for pair<int, pair<int, int>> type
typedef pair<double, pair<int, int>> pPair;

// A structure to hold neccesary parameters
struct cell {
	// row and column index of its parent
	// NB: 0 <= i <= ROW-1 & 0 <= j <= COL-1
	int parent_i, parent_j;
	
	// f = g + h
	double f, g, h;
};

// A utility fx to check whether given cell (row, col) is a valid cell or not
bool isValid(int row, int col){
	// returns true if row number and column number is in range
	return (row >= 0) && (row < ROW) && (col >= 0) && (col < COL);
}

// A utility fx to check whether the given cell is blocked or not
bool isUnBlocked(int grid[][COL], int row, int col){
	// returns true if the cell is not blocked else false
	if (grid[row][col] == 1)
		return (true);
	else
		return (false);
}

// A utility fx to check whether destination cell has been reached or not
bool isDestination(int row, int col, Pair dest){
	if (row == dest.first && col == dest.second)
		return (true);
	else
		return (false);
}

// A utility fx to calculate the "h" heuristics
double calculateHValue(int row, int col, Pair dest){
	// return using the distance formular (Euclidean)
	return ((double)sqrt ((row-dest.first) * (row-dest.first) + (col-dest.second) * (col-dest.second)));
}

// A utility fx to trace the path from the source to destination
void tracePath(cell cellDetails[][COL], Pair dest){
	printf("\nThe Path is ");
	int row = dest.first;
	int col = dest.second;

	stack<Pair> Path;

	while (!(cellDetails[row][col].parent_i == row && cellDetails[row][col].parent_j == col)){
		Path.push (make_pair (row, col));	
		int temp_row = cellDetails[row][col].parent_i;
		int temp_col = cellDetails[row][col].parent_j;

		row = temp_row;
		col = temp_col;
	}

	Path.push (make_pair (row, col));
	while (!Path.empty()){
		pair<int, int> p = Path.top();
		Path.pop();
		printf("-> (%d,%d) ", p.first, p.second);
	}

	return;
}

// A function to find the shortest path between a given source cell to a destination cell
void aStarSearch(int grid[][COL], Pair src, Pair dest){
	// if source is out of range
	if (isValid (src.first, src.second) == false){
		printf("Source is invalid\n");
		return;
	}

	// if destination is out of range
	if (isValid (dest.first, dest.second) == false){
		printf("Destination is invalid\n");
		return;
	}

	// either source or destination is blocked
	if (isUnBlocked (grid, src.first, src.second) == false || isUnBlocked (grid, dest.first, dest.second) == false){
		printf("Source or Destination is blocked\n");
		return;
	}

	// if destination cell is same as source cell
	if (isDestination (src.first, src.second, dest) == true){
		printf("We are already at the destination\n");
		return;
	}

	// create a closed list and initialize it to false (meaning that no cell has been included yet) - closed list implemented as boolean 2D array
	bool closedList[ROW][COL];
	memset (closedList, false, sizeof(closedList));

	// declare a @d array of structure to hold details of that cell
	cell cellDetails[ROW][COL];

	int i, j;

	for (i=0; i<ROW; i++){
		for (j=0; j<COL; j++){
			cellDetails[i][j].f = FLT_MAX;
			cellDetails[i][j].g = FLT_MAX;
			cellDetails[i][j].h = FLT_MAX;
			cellDetails[i][j].parent_i = -1;
			cellDetails[i][j].parent_j = -1;
		}
	}

	// initializing parameters of the starting node
	i = src.first;
	j = src.second;

	cellDetails[i][j].f = 0.0;
	cellDetails[i][j].g = 0.0;
	cellDetails[i][j].h = 0.0;
	cellDetails[i][j].parent_i = i;
	cellDetails[i][j].parent_j = j;

	/* create an open list (implemented as set of pair-of-pair) having information as - <f, <i, j>>
	where f = g + h, and i, j are row and column index of that cell
	NB: 0 <= i <= ROW-1 & ) <= j <= COL-1.*/
	set<pPair> openList;

	// put starting cell on the open list and set its "f" as 0
	openList.insert(make_pair (0.0, make_pair(i, j)));

	// Set boolean value as false as initially destination is not reached
	bool foundDest = false;

	while (!openList.empty()){
		pPair p = *openList.begin();

		// remove this vertex from the open list
		openList.erase(openList.begin());

		// add this vertex to the closed list
		i = p.second.first;
		j = p.second.second;
		closedList[i][j] = true;

		/* generating all 8 successors of this cell
			
			N.W   N   N.E 
              \   |   / 
               \  |  / 
            W----Cell----E 
                 / | \ 
               /   |  \ 
            S.W    S   S.E 

		Cell-->Popped Cell (i, j) 
        N -->  North       (i-1, j) 
        S -->  South       (i+1, j) 
        E -->  East        (i, j+1) 
        W -->  West           (i, j-1) 
        N.E--> North-East  (i-1, j+1) 
        N.W--> North-West  (i-1, j-1) 
        S.E--> South-East  (i+1, j+1) 
        S.W--> South-West  (i+1, j-1)
		*/

		// to store "g", "h", "f" of the 8 successors
		double gNew, hNew, fNew;

		// --- 1st Successor (North)
		// only process this cell if this is a valid one
		if (isValid(i-1, j) == true){
			// if destination cell is same as current successor
			if (isDestination(i-1, j, dest) == true){
				// set the parent of destination cell
				cellDetails[i-1][j].parent_i = i;
				cellDetails[i-1][j].parent_j = j;
				printf("The destination cell is found\n");
				tracePath (cellDetails, dest);
				foundDest = true;
				return;
			// if successor is already on the closed list or if it is blocked, ignore; else do the following
			} else if (closedList[i-1][j] == false && isUnBlocked(grid, i-1, j) == true){
				gNew = cellDetails[i][j].g + 1.0;
				hNew = calculateHValue (i-1, j, dest);
				fNew = gNew + hNew;

				// if it is not on the open list, add it to open list
				// make current square the parent of this square
				// record "f", "g", "h" costs of the sequare cell
				// --- or
				// if it is on the open list, check to see if this path to that square is better
				// using "f" cost as the measure
				if (cellDetails[i-1][j].f == FLT_MAX || cellDetails[i-1][j].f > fNew){
					openList.insert(make_pair(fNew, make_pair(i-1, j)));
					// update details of this cell
					cellDetails[i-1][j].f = fNew;
					cellDetails[i-1][j].g = gNew;
					cellDetails[i-1][j].h = hNew;
					cellDetails[i-1][j].parent_i = i;
					cellDetails[i-1][j].parent_j = j;
				}
			}
		}

		// --- 2nd Successor (South)
		// only process this cell if this is a valid one
		if (isValid(i+1, j) == true){
			// if destination cell is same as current successor
			if (isDestination(i+1, j, dest) == true){
				// set the parent of destination cell
				cellDetails[i+1][j].parent_i = i;
				cellDetails[i+1][j].parent_j = j;
				printf("The destination cell is found\n");
				tracePath (cellDetails, dest);
				foundDest = true;
				return;
			// if successor is already on the closed list or if it is blocked, ignore; else do the following
			} else if (closedList[i+1][j] == false && isUnBlocked(grid, i+1, j) == true){
				gNew = cellDetails[i][j].g + 1.0;
				hNew = calculateHValue(i+1, j, dest);
				fNew = gNew + hNew;

				// if it is not on the open list, add it to open list
				// make current square the parent of this square
				// record "f", "g", "h" costs of the sequare cell
				// --- or
				// if it is on the open list, check to see if this path to that square is better
				// using "f" cost as the measure
				if (cellDetails[i+1][j].f == FLT_MAX || cellDetails[i+1][j].f > fNew){
					openList.insert(make_pair(fNew, make_pair(i+1, j)));
					// update details of this list
					cellDetails[i+1][j].f = fNew;
					cellDetails[i+1][j].g = gNew;
					cellDetails[i+1][j].h = hNew;
					cellDetails[i+1][j].parent_i = i;
					cellDetails[i+1][j].parent_j = j;
				}
			}
		}

		// --- 3rd Successor (East)
		// only process this cell if this is a valid one
		if (isValid (i, j+1) == true){
			// if destination cell is same as current processor
			if (isDestination (i, j+1, dest) == true){
				// set the parent of destination cell
				cellDetails[i][j+1].parent_i = i;
				cellDetails[i][j+1].parent_j = j;
				printf("The destination cell is found");
				tracePath(cellDetails, dest);
				foundDest = true;
				return;
			// if successor is already on the closed list or if it is blocked, ignore; else do the following
			} else if (closedList[i][j+1] == false && isUnBlocked (grid, i, j+1) == true){
				gNew = cellDetails[i][j].g + 1.0;
				hNew = calculateHValue(i, j+1, dest);
				fNew = gNew + hNew;

				// if it is not on the open list, add it to open list
				// make current square the parent of this square
				// record "f", "g", "h" costs of the sequare cell
				// --- or
				// if it is on the open list, check to see if this path to that square is better
				// using "f" cost as the measure
				if (cellDetails[i][j+1].f == FLT_MAX || cellDetails[i][j+1].f > fNew){
					openList.insert(make_pair(fNew, make_pair(i, j+1)));
					// update details of this cell
					cellDetails[i][j+1].f = fNew;
					cellDetails[i][j+1].g = gNew;
					cellDetails[i][j+1].h = hNew;
					cellDetails[i][j+1].parent_i = i;
					cellDetails[i][j+1].parent_j = j;
				}
			}
		}

		// --- 4th Successor (West)
		// only process this cell if this is a valid one
		if (isValid (i, j-1) == true){
			// if destination cell is same as current processor
			if (isDestination (i, j-1, dest) == true){
				// set the parent of destination cell
				cellDetails[i][j-1].parent_i = i;
				cellDetails[i][j-1].parent_j = j;
				printf("The destination cell is found");
				tracePath(cellDetails, dest);
				foundDest = true;
				return;
			// if successor is already on the closed list or if it is blocked, ignore; else do the following
			} else if (closedList[i][j-1] == false && isUnBlocked (grid, i, j-1) == true){
				gNew = cellDetails[i][j].g + 1.0;
				hNew = calculateHValue(i, j-1, dest);
				fNew = gNew + hNew;

				// if it is not on the open list, add it to open list
				// make current square the parent of this square
				// record "f", "g", "h" costs of the sequare cell
				// --- or
				// if it is on the open list, check to see if this path to that square is better
				// using "f" cost as the measure
				if (cellDetails[i][j-1].f == FLT_MAX || cellDetails[i][j-1].f > fNew){
					openList.insert(make_pair(fNew, make_pair(i, j-1)));
					// update details of this cell
					cellDetails[i][j-1].f = fNew;
					cellDetails[i][j-1].g = gNew;
					cellDetails[i][j-1].h = hNew;
					cellDetails[i][j-1].parent_i = i;
					cellDetails[i][j-1].parent_j = j;
				}
			}
		}

		// --- 5th Successor (North-East)
		// only process this cell if this is a valid one
		if (isValid (i-1, j+1) == true){
			// if destination cell is same as current processor
			if (isDestination (i-1, j+1, dest) == true){
				// set the parent of destination cell
				cellDetails[i-1][j+1].parent_i = i;
				cellDetails[i-1][j+1].parent_j = j;
				printf("The destination cell is found");
				tracePath(cellDetails, dest);
				foundDest = true;
				return;
			// if successor is already on the closed list or if it is blocked, ignore; else do the following
			} else if (closedList[i-1][j+1] == false && isUnBlocked (grid, i-1, j+1) == true){
				gNew = cellDetails[i][j].g + 1.414;
				hNew = calculateHValue(i-1, j+1, dest);
				fNew = gNew + hNew;

				// if it is not on the open list, add it to open list
				// make current square the parent of this square
				// record "f", "g", "h" costs of the sequare cell
				// --- or
				// if it is on the open list, check to see if this path to that square is better
				// using "f" cost as the measure
				if (cellDetails[i-1][j+1].f == FLT_MAX || cellDetails[i-1][j+1].f > fNew){
					openList.insert(make_pair(fNew, make_pair(i-1, j+1)));
					// update details of this cell
					cellDetails[i-1][j+1].f = fNew;
					cellDetails[i-1][j+1].g = gNew;
					cellDetails[i-1][j+1].h = hNew;
					cellDetails[i-1][j+1].parent_i = i;
					cellDetails[i-1][j+1].parent_j = j;
				}
			}
		}

		// --- 6th Successor (North-West)
		// only process this cell if this is a valid one
		if (isValid (i-1, j-1) == true){
			// if destination cell is same as current processor
			if (isDestination (i-1, j-1, dest) == true){
				// set the parent of destination cell
				cellDetails[i-1][j-1].parent_i = i;
				cellDetails[i-1][j-1].parent_j = j;
				printf("The destination cell is found");
				tracePath(cellDetails, dest);
				foundDest = true;
				return;
			// if successor is already on the closed list or if it is blocked, ignore; else do the following
			} else if (closedList[i-1][j-1] == false && isUnBlocked (grid, i-1, j-1) == true){
				gNew = cellDetails[i][j].g + 1.414;
				hNew = calculateHValue(i-1, j-1, dest);
				fNew = gNew + hNew;

				// if it is not on the open list, add it to open list
				// make current square the parent of this square
				// record "f", "g", "h" costs of the sequare cell
				// --- or
				// if it is on the open list, check to see if this path to that square is better
				// using "f" cost as the measure
				if (cellDetails[i-1][j-1].f == FLT_MAX || cellDetails[i-1][j-1].f > fNew){
					openList.insert(make_pair(fNew, make_pair(i-1, j-1)));
					// update details of this cell
					cellDetails[i-1][j-1].f = fNew;
					cellDetails[i-1][j-1].g = gNew;
					cellDetails[i-1][j-1].h = hNew;
					cellDetails[i-1][j-1].parent_i = i;
					cellDetails[i-1][j-1].parent_j = j;
				}
			}
		}

		// --- 7th Successor (South-East)
		// only process this cell if this is a valid one
		if (isValid (i+1, j+1) == true){
			// if destination cell is same as current processor
			if (isDestination (i+1, j+1, dest) == true){
				// set the parent of destination cell
				cellDetails[i+1][j+1].parent_i = i;
				cellDetails[i+1][j+1].parent_j = j;
				printf("The destination cell is found");
				tracePath(cellDetails, dest);
				foundDest = true;
				return;
			// if successor is already on the closed list or if it is blocked, ignore; else do the following
			} else if (closedList[i+1][j+1] == false && isUnBlocked (grid, i+1, j+1) == true){
				gNew = cellDetails[i][j].g + 1.414;
				hNew = calculateHValue(i+1, j+1, dest);
				fNew = gNew + hNew;

				// if it is not on the open list, add it to open list
				// make current square the parent of this square
				// record "f", "g", "h" costs of the sequare cell
				// --- or
				// if it is on the open list, check to see if this path to that square is better
				// using "f" cost as the measure
				if (cellDetails[i+1][j+1].f == FLT_MAX || cellDetails[i+1][j+1].f > fNew){
					openList.insert(make_pair(fNew, make_pair(i+1, j+1)));
					// update details of this cell
					cellDetails[i+1][j+1].f = fNew;
					cellDetails[i+1][j+1].g = gNew;
					cellDetails[i+1][j+1].h = hNew;
					cellDetails[i+1][j+1].parent_i = i;
					cellDetails[i+1][j+1].parent_j = j;
				}
			}
		}

		// --- 8th Successor (South-West)
		// only process this cell if this is a valid one
		if (isValid (i+1, j-1) == true){
			// if destination cell is same as current processor
			if (isDestination (i+1, j-1, dest) == true){
				// set the parent of destination cell
				cellDetails[i+1][j-1].parent_i = i;
				cellDetails[i+1][j-1].parent_j = j;
				printf("The destination cell is found");
				tracePath(cellDetails, dest);
				foundDest = true;
				return;
			// if successor is already on the closed list or if it is blocked, ignore; else do the following
			} else if (closedList[i+1][j-1] == false && isUnBlocked (grid, i+1, j-1) == true){
				gNew = cellDetails[i][j].g + 1.414;
				hNew = calculateHValue(i+1, j-1, dest);
				fNew = gNew + hNew;

				// if it is not on the open list, add it to open list
				// make current square the parent of this square
				// record "f", "g", "h" costs of the sequare cell
				// --- or
				// if it is on the open list, check to see if this path to that square is better
				// using "f" cost as the measure
				if (cellDetails[i+1][j-1].f == FLT_MAX || cellDetails[i+1][j-1].f > fNew){
					openList.insert(make_pair(fNew, make_pair(i+1, j-1)));
					// update details of this cell
					cellDetails[i+1][j-1].f = fNew;
					cellDetails[i+1][j-1].g = gNew;
					cellDetails[i+1][j-1].h = hNew;
					cellDetails[i+1][j-1].parent_i = i;
					cellDetails[i+1][j-1].parent_j = j;
				}
			}
		}
	}

	// when destination cell is not found and open list is empty, conclude we failed to reach destination cell
	// this may happen due to blockages
	if (foundDest == false){
		printf("Failed to find the Destination Cell\n");
	}

	return;
}

// --- Driver Program to Test Functions
int main(){
	/* description of grid
	1--> cell is not blocked
	0--> cell is blocked
	*/
	int grid[ROW][COL] = {
		{ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 }, 
        { 1, 1, 1, 0, 1, 1, 1, 0, 1, 1 }, 
        { 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 }, 
        { 0, 0, 1, 0, 1, 0, 0, 0, 0, 1 }, 
        { 1, 1, 1, 0, 1, 1, 1, 0, 1, 0 }, 
        { 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 }, 
        { 1, 0, 0, 0, 0, 1, 0, 0, 0, 1 }, 
        { 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 }, 
        { 1, 1, 1, 0, 0, 0, 1, 0, 0, 1 } 
	};

	// source is left-most bottom-most corner
	Pair src = make_pair(8, 0);

	// destination is left-most top-most corner
	Pair dest = make_pair(0, 0);

	aStarSearch(grid, src, dest);

	return(0);
}