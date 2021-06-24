from Board import gen_board, print_board, moves_arr
from A_Star_Search import A_Star_Search
import time

# --------------------------------------------------------------
# Generating N  puzzles
# --------------------------------------------------------------
# This method keeps creating new boards until
# the list of puzzles reach a number of given count
def generate_n_puzzles(N):
    unique_puzzles = [] * N
    counter = 0
    temp = 1
    while temp > 0:
        board = gen_board()

        # Check if current created board is created 
        # and added to our list of boards before
        if board not in unique_puzzles:
            unique_puzzles.append(board)
            counter += 1
            if (counter == N):
                temp = -1

    return unique_puzzles

# --------------------------------------------------------------
# MAIN
# --------------------------------------------------------------
"""
    The program will solve 10 puzzles. The number of puzzles can be changed right under here. "N = 10"
    If a state takes too long to solve consider waiting for it for about a few minutes. All puzzles are solveable
    and 2 sample outputs are attached below this main class. 


    It iterates through the tree, finds all possible moves from the current node, and checks for loops,
    and same destinations dynamically. If the two states are equal with different costs, then it is considered 
    that one of them should be removed from the tree, regarding their costs. The one with the higher cost is not considered again.

    The heuristic estimates the distance left to the goal in an underestimated fashion, using Manhattan distance. The scores are added up from each previous node,
    and plus one meaning that we increase the path length by 1 with each increment. 


    Once a state has been added to the tree. We keep checking other nodes and kepe repeating until we have a big tree structure.
    The program always finds the most efficient path to solution.

    When the puzzle has been solved we print the 2 first puzzles' sequence both in text and graphical puzzles, and print the rest
    in text sequence. 

    After successfully solving all puzzles, A simple "graph" is printed out. Since we had to print the graph in the output prompt,
    we print using simple texts, The x axis is for states such as; S1, S2, etc... And Y axis is considered the number of moves for each puzzle
"""


# define a number of unique puzzles wanted
N = 10

# Now create them and add them into boards_arr
boards_arr = generate_n_puzzles(N)

# print all the boards
for i in range (N):
    print("Board S{:d}: \n".format(i+1))
    print_board(boards_arr[i])
    print("\n\n")

# Solution lengths for each puzzle
# Define an array of size N
sol_data = [1]*N

# Loop search a* lowerestimeate
for k in range (N):
    print("For board S{:d}: \n".format(k+1))
    A_Star_Search(boards_arr[k])
    
    print("\n\n\n")

sum = 0
for i in range (N):
    sum = sum + moves_arr[i] - 1

# This calculation divides total moves to puzzle size and rounds it to
# 3 decimal places. If the result has 2 decimal places that is because
# the division is perfect to 2 decimals
avg = float("{0:.3f}".format(sum / N))

# Print "graph"
# x axis is state names
# y axis number of moves
for i in range(N):
    print("\t",moves_arr[i]-1,end="")
print("\t",avg,end="\n")
print("|")
print("|")
print("|")
print("|")
print("|___________________________________________________________________________________________________________")
for i in range (N):
    print("\tS{:d}".format(i+1),end="")

# lastly add average to the end state name
print("\tAvg",end="")
print()






# EXAMPLE OUTPUT 
# -------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------
"""
Board S1: 

 1   2   3   4  
 5   6  15   7  
 9  10   _   8  
13  14  12  11  



Board S2:       

 1   2   3   4  
 5   7  10   8  
 9   6  11   _  
13  14  15  12  



Board S3:       

 1   2   3   4
 5   6   7   8
 _  10  15  11
 9  13  14  12



Board S4:

 1   2   3   4
 _   5   6   7
 9  11  12   8
13  10  14  15



Board S5:

 1   2   3   4
 5   6   7   8
 9  10   _  11
13  14  15  12



Board S6:

 2   _   3   4
 1   6   7   8
 5  14  10  11
 9  13  15  12



Board S7:

 2   6   5   4
 1   _   3   7
 9  10  12   8
13  14  11  15



Board S8:

 5   6   1   4
 2  10   3   8
 _   9   7  12  
13  14  11  15



Board S9:

 1   2   7   3
 5   6   4   8
 9  10  15  11
13  14  12   _



Board S10:

 1   2   4   8
 _   5   6  11
 9  14   3  10
13   7  15  12



For board S1:

 1   2   3   4  
 5   6  15   7
 9  10   _   8
13  14  12  11
Move:  0
Action:  start


 1   2   3   4
 5   6   _   7
 9  10  15   8
13  14  12  11
Move:  1
Action:  up


 1   2   3   4  
 5   6   7   _
 9  10  15   8
13  14  12  11
Move:  2
Action:  right


 1   2   3   4
 5   6   7   8
 9  10  15   _
13  14  12  11
Move:  3
Action:  down


 1   2   3   4
 5   6   7   8
 9  10  15  11
13  14  12   _
Move:  4
Action:  down


 1   2   3   4
 5   6   7   8
 9  10  15  11
13  14   _  12  
Move:  5
Action:  left


 1   2   3   4
 5   6   7   8
 9  10   _  11
13  14  15  12
Move:  6
Action:  up


 1   2   3   4
 5   6   7   8
 9  10  11   _
13  14  15  12
Move:  7
Action:  right


 1   2   3   4
 5   6   7   8
 9  10  11  12
13  14  15   _  
Move:  8
Action:  down






For board S2:

 1   2   3   4  
 5   7  10   8  
 9   6  11   _
13  14  15  12
Move:  0
Action:  start


 1   2   3   4
 5   7  10   8
 9   6   _  11
13  14  15  12
Move:  1
Action:  left


 1   2   3   4
 5   7   _   8
 9   6  10  11
13  14  15  12
Move:  2
Action:  up


 1   2   3   4
 5   _   7   8
 9   6  10  11
13  14  15  12
Move:  3
Action:  left


 1   2   3   4
 5   6   7   8
 9   _  10  11
13  14  15  12
Move:  4
Action:  down


 1   2   3   4
 5   6   7   8
 9  10   _  11
13  14  15  12
Move:  5
Action:  right


 1   2   3   4
 5   6   7   8  
 9  10  11   _
13  14  15  12
Move:  6
Action:  right


 1   2   3   4
 5   6   7   8
 9  10  11  12
13  14  15   _
Move:  7
Action:  down






For board S3:

Move :  0
Action:  start
Move :  1
Action:  down
Move :  2
Action:  right
Move :  3
Action:  right
Move :  4
Action:  up
Move :  5
Action:  right
Move :  6
Action:  down




For board S4:

Move :  0
Action:  start
Move :  1
Action:  right
Move :  2
Action:  right
Move :  3
Action:  right
Move :  4
Action:  down
Move :  5
Action:  left
Move :  6
Action:  left
Move :  7
Action:  down
Move :  8
Action:  right
Move :  9
Action:  right




For board S5:

Move :  0
Action:  start
Move :  1
Action:  right
Move :  2
Action:  down




For board S6:

Move :  0
Action:  start
Move :  1
Action:  left
Move :  2
Action:  down
Move :  3
Action:  down
Move :  4
Action:  down
Move :  5
Action:  right
Move :  6
Action:  up
Move :  7
Action:  right
Move :  8
Action:  right
Move :  9
Action:  down




For board S7:

Move :  0
Action:  start
Move :  1
Action:  up
Move :  2
Action:  right
Move :  3
Action:  down
Move :  4
Action:  left
Move :  5
Action:  up
Move :  6
Action:  left
Move :  7
Action:  down
Move :  8
Action:  right
Move :  9
Action:  right
Move :  10
Action:  right
Move :  11
Action:  down
Move :  12
Action:  left
Move :  13
Action:  down
Move :  14
Action:  right




For board S8:

Move :  0
Action:  start
Move :  1
Action:  right
Move :  2
Action:  up
Move :  3
Action:  up
Move :  4
Action:  right
Move :  5
Action:  down
Move :  6
Action:  left
Move :  7
Action:  left
Move :  8
Action:  up
Move :  9
Action:  right
Move :  10
Action:  down
Move :  11
Action:  right
Move :  12
Action:  down
Move :  13
Action:  down
Move :  14
Action:  right




For board S9:

Move :  0
Action:  start
Move :  1
Action:  left
Move :  2
Action:  up
Move :  3
Action:  right
Move :  4
Action:  up
Move :  5
Action:  left
Move :  6
Action:  up
Move :  7
Action:  right
Move :  8
Action:  down
Move :  9
Action:  down
Move :  10
Action:  down




For board S10:

Move :  0
Action:  start
Move :  1
Action:  right
Move :  2
Action:  right
Move :  3
Action:  down
Move :  4
Action:  right
Move :  5
Action:  down
Move :  6
Action:  left
Move :  7
Action:  left
Move :  8
Action:  up
Move :  9
Action:  right
Move :  10
Action:  down
Move :  11
Action:  right
Move :  12
Action:  up
Move :  13
Action:  up
Move :  14
Action:  up
Move :  15
Action:  left
Move :  16
Action:  down
Move :  17
Action:  down
Move :  18
Action:  right
Move :  19
Action:  down




         8       7       6       9       2       9       14      14      10      19      9.8
|
|
|
|
|___________________________________________________________________________________________________________
        S1      S2      S3      S4      S5      S6      S7      S8      S9      S10     Avg


"""