import example_board
import copy

class SudokuSolver:
    def __init__(self, board = example_board.board):
        self.board = board

    def solve(self):
        """Solves the sudoku puzzle recursively.

        Returns:
            bool: True if solvable, False if not
        """

        # Tuple containing co-ordinates of an empty cell
        find = self.find_empty() 

        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.validate_number(i, (row, col)):
                # Insert a number into cell if it does not break Sudoku rules
                self.board[row][col] = i

                # Recursively call function until no more empty cells found
                if self.solve():
                    return True
                
                # Reset the last cell to 0 as no solution found, then continue
                # loop to try with the next value
                self.board[row][col] = 0

        return False

    def validate_number(self, num, pos):
        """Validates whether a given number inserted into a cell in the board
        specified by a (row number, column number) co-ordinate. 

        3 checks required due to rules of Sudoku:
        - Each number only appears once in each row.
        - Each number only appears once in each column.
        - Each number only appears once in each sub-grid (3x3 cells).

        Returns:
            bool: True if all checks pass, False if any fail.
        """
        # Check row
        for i in range(len(self.board[0])):
            # Check each cell in a row for the number, except for in
            # the location where we are attempting to place it.
            if self.board[pos[0]][i] == num and i != pos[1]:
                return False
            
        # Check column
        for i in range(len(self.board)):
            if self.board[i][pos[1]] == num and i != pos[0]:
                return False
            
        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False
                
        # All checks passed
        return True
    
    def validate_starting_board(self):
        """
        Backtracking algorithm does not validate numbers that have already been placed
        in the board, therefore this function assesses that the starting board is valid
        before attempting to solve it.

        Returns:
        A tuple consisting of two elements -
            [0] - bool: True if valid, False if invalid.
            [1] - string: Contains the error message for why the board is invalid.
        """
        board = self.board
            
        # Validate row
        for row in range(len(board)):
            tracker = []
            for num in board[row]:
                if num in tracker and num != 0:
                    message = f"{num} appeared more than once in row {row+1}."
                    return (False, message)
                else:
                    tracker.append(num)

        # Validate column
        for col in range(len(board[0])):
            tracker = []

            for row in range(len(board)):
                num = board[row][col]

                if num in tracker and num != 0:
                    message = f"{num} appeared more than once in column {col+1}."
                    return (False, message)
                else:
                    tracker.append(num)

        # Validate box
        box_count = len(board) // 3

        # Get a coordinate (x,y) for top-left number in each sub box
        for x in range(box_count):
            for y in range(box_count):

                # Narrow down the rows contained in each box
                rows = board[x*3: x*3 + 3]

                # Iterate through those rows from starting y co-ord to final y co-ord
                val_store = []
                for row in rows:
                    vals = row[y*3: y*3 + 3]
                    val_store.append(vals)

                # Flatten the resulting list of lists
                box_values = []
                for val_list in val_store:
                    box_values.extend(val_list)

                # Check each box, represented by a single list
                tracker = []

                for val in box_values:
                    if val in tracker and val != 0:
                        message = f"{val} appeared more than once in box {(x, y)}."
                        return (False, message)
                    else:
                        tracker.append(val)

        # If all checks pass
        return (True, None)

    def print_board(self):
        """
        Utility function to display a board in the terminal.
        Not used in Streamlit application.
        """
        # Create copy of variable so don't change self.board itself
        temp_board = copy.deepcopy(self.board)
        board = self.convert_zeroes_to_blanks(temp_board)

        for i in range(len(board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")

            for j in range(len(board)):
                if j % 3 == 0 and j != 0:
                    print(" | ", end = "")

                if j == 8:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end = "")

    def find_empty(self):
        """Iterates through board to find an empty cell.
        
        Returns:
            tuple: i, j co-ordinates of the empty cell.
        """
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    return (i, j)

    def convert_zeroes_to_blanks(self):
        """Formats the board by substituting all the placeholder 0s with 
        blank spaces. When displaying the board to a user, want empty cells
        to be displayed."""
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    self.board[i][j] = ''

        return self.board
    
    def convert_blanks_to_zeroes(self):
        """Formats the board by substituting the blanks with placeholder 0s."""
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == '':
                    self.board[i][j] = 0

        return self.board
    
    def convert_to_str(self):
        """Ensures every number in the grid is converted to a string."""
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                self.board[i][j] = str(self.board[i][j])

        return self.board
    
    def convert_to_int(self):
        """Ensures every number in the grid is converted to an integer."""
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                self.board[i][j] = int(self.board[i][j])

        return self.board




