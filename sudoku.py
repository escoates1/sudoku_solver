import example_board
import copy

class SudokuSolver:
    def __init__(self, board = example_board.board):
        self.board = board

    def solve(self):
        """

        """
        find = self.find_empty() 

        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.validate(i, (row, col)):
                self.board[row][col] = i

                if self.solve():
                    return True
                
                self.board[row][col] = 0

        return False

    def validate(self, num, pos):
        """
        
        """
        # Check row
        for i in range(len(self.board[0])):
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

    def print_board(self):
        """

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
        """

        """
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    return (i, j)

    def convert_zeroes_to_blanks(self, board):
        """
        Formats a board by substituting all the placeholder 0s with blank spaces
        """
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 0:
                    board[i][j] = ' '

        return board
    
if __name__ == '__main__':
    su = Solver()
    su.print_board()
    print('\n')
    su.solve()
    su.print_board()




