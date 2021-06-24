import random
import copy
from copy import deepcopy

MAX_PRINT = 2
CUR_PRINT = 0
MAX_COLUMN = 4
MAX_ROW = 4
moves_arr = []
solution_length_from_board = 0
cur_print = 0


goal = [[" 1", " 2", " 3"," 4"],
        [" 5", " 6", " 7"," 8"],
        [" 9", "10", "11","12"],
        ["13", "14", "15"," _"]]

# Rather than normal copying we use deepcopy to avoid creating a pointer
# deepcopy recursively copies the whole list array
board = deepcopy(goal)
emptyLoc = [MAX_ROW-1, MAX_COLUMN-1] # store empty square position
# --------------------------------------------------------------

# --------------------------------------------------------------
# Print a board method
def print_board(board):
    for i in range(MAX_ROW):
        for j in range(MAX_COLUMN):
            print (board[i][j],end="  ")
        print()
    # function must return something so we return blank    
    return ""

# --------------------------------------------------------------

# --------------------------------------------------------------
# Generating random boards
# We generate a board by getting a random move count between 5 and 10
# Then we use garble method to do that number of random moves
def gen_board():
    move_count = random.randint(20,30)
    rand_board = copy.deepcopy(board)
    i = 0

    while (i != move_count):
        rand_board = garble(rand_board)
        i += 1

    return rand_board
# --------------------------------------------------------------

# --------------------------------------------------------------
# Find index of value
def find_indexOf(board, value):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == value:
                return (i, j)
    return None
# --------------------------------------------------------------

# --------------------------------------------------------------
# Now to find legal moves e.g. not out of bounds
# This method ifnds all the possible moves for the
# blank cell's current location. Menaing that
# they update with each move
# This method gets all possible moves of the empty cell
# and stores them in an array
def find_possible_moves(board):

    # Location of empty slot
    (i, j) = find_indexOf(board, ' _')

    # Possible moves array
    moves = []

    # Left
    if j > 0 :
        moves.append('left')

    # Right
    if j < MAX_COLUMN - 1 :
        moves.append('right')

    # Down
    if i < MAX_ROW - 1 :
        moves.append('down')

    # Up
    if i > 0:
        moves.append('up')

    return moves

# --------------------------------------------------------------

# --------------------------------------------------------------
# After getting all possible moves in an array
# this method picks one move randomly and executes
# it by calling the move method
def garble(board):
    # Possible moves
    moves = find_possible_moves(board)

    # Choose one move from the possible moves options randomly
    choice = moves[random.randint(0, len(moves) - 1)]

    # Moving the tile according to random choice
    return move(board, choice)
# --------------------------------------------------------------

# --------------------------------------------------------------
# Move a cell of given board to a given direction
def move(board, direction):
    # Location of Empty slot
    (ci, cj) = find_indexOf(board, ' _')

    board_dup = copy.deepcopy(board)

    # Apply move
    if direction == 'up':
        # print("moving up")
        cell_to_move = board_dup[ci-1][cj]
        board_dup[ci][cj] = cell_to_move
        board_dup[ci-1][cj] = " _"
    elif direction == 'down':
        # print("moving down")
        cell_to_move = board_dup[ci+1][cj]
        board_dup[ci][cj] = cell_to_move
        board_dup[ci+1][cj] = " _"
    elif direction =='right':
        # print("moving right")
        cell_to_move = board_dup[ci][cj+1]
        board_dup[ci][cj] = cell_to_move
        board_dup[ci][cj+1] = " _"
    elif direction == 'left':
        # print("moving left")
        cell_to_move = board_dup[ci][cj-1]
        board_dup[ci][cj] = cell_to_move
        board_dup[ci][cj-1] = " _"

    return board_dup


# --------------------------------------------------------------




# --------------------------------------------------------------



# --------------------------------------------------------------
def underestimate_manhattan(state):
    # Calculates and return the h2 heuristic for a given state
    # H2 calculates the sum of the Manhattan distances of all the tiles for the puzzle
    # Manhattan distance is the sum of the absolute value of the x and y difference of the current tile position from its goal state position

    state_dict = {}
    goal_dict = {}
    heuristic = 0
    
    # Create dictionaries of the current state and goal state
    for row_index, row in enumerate(state):
        for col_index, element in enumerate(row):
            state_dict[element] = (row_index, col_index)
    
    for row_index, row in enumerate(goal):
        for col_index, element in enumerate(row):
            goal_dict[element] = (row_index, col_index)
            
    for tile, position in state_dict.items():
        # Do not count the distance of the blank 
        if tile == " _":
            pass
        else:
            # Calculate heuristic as the Manhattan distance
            goal_position = goal_dict[tile]
            heuristic += (abs(position[0] - goal_position[0]) + abs(position[1] - goal_position[1]))

    return heuristic

# --------------------------------------------------------------
def success(board, path):
    count = 0
    global cur_print
    if (cur_print < 2):
        for item in path:
            print_board(item[0])
            print("Move: ",count)
            print("Action: ",item[2])
            count+=1
            print("\n")
    

    elif (cur_print >= 2):
        for item in path:
            print("Move : ",count)
            print("Action: ",item[2])
            count+=1
    cur_print += 1
    moves_arr.append(count)
    return


# --------------------------------------------------------------




def get_Sol_Len():
    return solution_length_from_board

