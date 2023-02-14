# 15-Puzzle-A-Star-Search
This project generates a solveable 15 puzzle (see https://en.wikipedia.org/wiki/15_puzzle) by randomly changing the positions of any piece. Depending on the number of changes the puzzle's difficulty increases.

The example output shows 10 generated puzzles and how they were solved. The first 3 puzzles are drawn at each step from the start state. For the rest of the puzzles only the executed moves are printed out without drawing.

Then a primitive graph is printed out showing each board(puzzle)'s number of moves taken to solve and an average is taken.

------------------------
The solving algorithm is dynamic A-Star search algorithm using scoring system while avoiding re-using previously used paths. More info is in related py file.

