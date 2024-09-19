import pytest
import sudoku
import logging
import example_boards as ex
import time

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler that overwrites
file_handler = logging.FileHandler('tests/test_sudoku.log', mode='w')
file_handler.setLevel(logging.INFO)

# Add handler to the logger
logger.addHandler(file_handler)

# Set up object instances to be inherited by each testing class
@pytest.fixture(scope='function')
def solvable():
    # A valid, solvable board
    obj = sudoku.SudokuSolver(ex.board)
    logger.info(f'Creating solvable instance @ {time.time()}: {obj.board}')
    yield obj
    logger.info(f'Tearing down solvable instance @ {time.time()}: {obj.board}')
    del obj

@pytest.fixture(scope='function')
def unsolvable():
    # A valid starting board that cannot be solved
    return sudoku.SudokuSolver(ex.unsolvable_board)

@pytest.fixture(scope='function')
def incorrect():
    # An invalid starting board, breaks sudoku rules
    return sudoku.SudokuSolver(ex.incorrect_board)

@pytest.fixture(scope='function')
def solved():
    # An already solved board
    return sudoku.SudokuSolver(ex.solved_board)

# @pytest.mark.usefixtures("solvable","unsolvable")
class TestSolvable:
    def test_solvable(self, solvable):
        res = solvable.solve()
        logger.info(f'{self.__class__.__name__}:\n{solvable.board}')

        assert res == True

    def test_unsolvable(self, unsolvable):
        res = unsolvable.solve()

        assert res == False

# @pytest.mark.usefixtures("solvable")
class TestValidateNumber:
    def test_valid_row_insertion(self, solvable):
        num = 5
        pos = (0, 2)

        res = solvable.validate_number(num, pos)

        assert res == True

    def test_valid_column_insertion(self, solvable):
        num = 4
        pos = (2, 0)
        res = solvable.validate_number(num, pos)

        assert res == True

    def test_valid_box_insertion(self, solvable):
        num = 1
        pos = (8, 4)
        res = solvable.validate_number(num, pos)

        assert res == True

    def test_invalid_row_insertion(self, solvable):
        num = 5
        pos = (4, 0)

        res = solvable.validate_number(num, pos)

        assert res == False

    def test_invalid_column_insertion(self, solvable):
        num = 2
        pos = (5, 7)
        res = solvable.validate_number(num, pos)

        assert res == False

    def test_invalid_box_insertion(self, solvable):
        num = 8
        pos = (1, 2)
        res = solvable.validate_number(num, pos)

        assert res == False

# @pytest.mark.usefixtures("solvable","incorrect")
class TestValidateStartingBoard:
    def test_correct_starting_board(self, solvable):
        res = solvable.validate_starting_board()

        assert res[0] == True

    def test_incorrect_starting_board(self, incorrect):
        res = incorrect.validate_starting_board()

        assert res[0] == False

# @pytest.mark.usefixtures("solvable","unsolvable","solved")
class TestFindEmpty:
    def test_find_empty_1(self, solvable):
        res = solvable.find_empty()
        logger.info(f'{self.__class__.__name__}:\n{solvable.board}')

        assert res == (0, 2)

    def test_find_empty_2(self, unsolvable):
        res = unsolvable.find_empty()

        assert res == (1, 1)

    def test_find_no_empty(self, solved):
        res = solved.find_empty()

        assert res is None
