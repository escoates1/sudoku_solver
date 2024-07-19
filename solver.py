import example_board

class Solver:
    def __init__(self, board = example_board.board):
        self.board = board

    def convert_zeroes_to_blanks(self):
        """
        Formats a board by substituting all the placeholder 0s with blank spaces
        """

        

    def print_board(self):
        """

        """
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")

            for j in range(len(self.board)):
                if j % 3 == 0 and j != 0:
                    print(" | ", end = "")

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end = "")

    def find_empty(self):
        """

        """
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    return (i, j)

if __name__ == '__main__':
    su = Solver()
    su.print_board()




