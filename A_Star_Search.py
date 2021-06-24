from Board import goal, find_indexOf, find_possible_moves, success, move, print_board, underestimate_manhattan
import math
import copy
from copy import deepcopy
import time


# We use Manhattan distance for underestimating becuase it calculates the lowest estimate distance between two given states
# https://people.cs.clemson.edu/~goddard/texts/artIntGame/chapB2.pdf
# A good read can be found here
def A_Star_Search(board):
    
    # Copy start state
    starting_state = deepcopy(board)

    # LIST will act as our tree. LIST keeps all paths inside it.
    LIST = []

    # path is a tuple list containing all nodes in a path
    path = []

    # get score of start state
    starting_score = underestimate_manhattan(starting_state)
    path_add = (starting_state, starting_score,"start")

    # Success boolean
    success_bool = False

    # A small chance, the starting state might be equal to the goal
    if starting_state == goal:
        success_bool = True
        success(starting_state, path)
        
    # add the start state to path and add the path to LIST
    path.append(path_add)
    LIST.append(path)

    

    # While list is not empty and success has not been reached
    while ((LIST) or (not success_bool)):

        # Gets first element of path from the tree
        first_node = LIST.pop(0)

        # Gets last index of current path
        # Store last index of path's state and score
        current_state = first_node[-1][0]
        current_score = first_node[-1][1]
        
        # Find available moves
        available_moves = find_possible_moves(current_state)
        
        # For each move do these actions
        for action in available_moves:
            # This bool is kept for loop checking in a path
            loop_path = False

            # Keep current path stored as temp
            temp_path = deepcopy(first_node)

            # Store successor state by the action
            successor_state = move(current_state, action)

            # current node has a score of its own underestimate manhattan score + current path length
            # and the score of the node before it
            # in other words, path's last node's second index of tuple
            successor_score = underestimate_manhattan(successor_state) + current_score + 1
            
            # If goal is found return success using temp_path
            if successor_state == goal:
                success_bool = True
                successor_node = (successor_state,successor_score, action)
                temp_path.append(successor_node)
                success(successor_state, temp_path)
                break

            # For all states inside the current path check for loops
            for item in first_node:
                if (item[0] == successor_state):
                    loop_path = True

            # If we do not have a loop then we can proceed to adding the state to current path
            if (not loop_path):
                # Add the new node to the current path's last index
                successor_node = (successor_state,successor_score,action)
                temp_path.append(successor_node)

                # Now check for same state with lower score in the whole tree
                dynamic = False
                pop_index = 0
                # Checking all paths inside the tree
                for element in LIST:
                    # If a state has been seen before, check the scores
                    for item in element:
                        
                        if (item[0] == successor_state):
                            # If old node has worse score delete its path
                            if (item[1] > successor_score):
                                LIST.pop(pop_index)
                                # And also add the new path to tree list
                                LIST.append(temp_path)
                                dynamic = True

                                break
                            else:
                                dynamic = True
                                break
                    # Count integer keeps track of the path indexes in the tree
                    # if we ever need to delete a path, we use this index to delete an old path from the tree
                    pop_index += 1 
                    # If we deleted an old path it means dynamic bool is now true
                    # So when it is true break the nested outer loop 
                    if (dynamic):
                        break    
                # If we have traversed out of the dynamic check loop without dynamic being true then we do not
                #have to take further actions because the path will never be added to the tree
                if not dynamic:
                    LIST.append(temp_path)
                
                # After any additions we must sort the LIST / tree
                # accordingly by path length and lower estimate bound
                # DO SORTING HERE, by total heuristic score, from lowest to highest
                LIST = sorted(LIST, key=lambda x: x[-1][1])
        if success_bool:
            break
                

            







