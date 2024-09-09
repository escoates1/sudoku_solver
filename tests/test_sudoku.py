import pytest
import sudoku
import example_boards as ex

@pytest.fixture(autouse=True, scope='class')
def solvable_sudoku(self):
    _solvable = sudoku.SudokuSolver(ex.board)

@pytest.fixture(autouse=True, scope='class')
def unsolvable_sudoku(self):
    _unsolvable = sudoku.SudokuSolver(ex.unsolvable_board)

# class TestSolvable:
#     def setup_method(self, solvable_sudoku, unsolvable_sudoku):
#         self.solvable = solvable_sudoku()
#         self.unsolvable = unsolvable_sudoku()

#     def test_solve_solvable(solvable):
#         res = solvable.solve()

#         assert res == True

#     def test_solve_unsolvable(unsolvable):
#         res = unsolvable.solve()

#         assert res == False

# @pytest.mark.usefixtures("solvable_sudoku","unsolvable_sudoku")
class TestValidateNumber:

    def test_valid_row_insertion(self):
        num = 5
        pos = (0, 2)
        res = self._solvable.validate_number(num, pos)

        assert res == True

# def test_validate_number_correct(solvable_sudoku):
#     num = 5
#     pos = (0, 2)
#     res = solvable_sudoku.validate_number(num, pos)

#     assert res == True

# def test_validate_number_incorrect(solvable_sudoku):
#     num = 8
#     pos = (0, 2)
#     res = solvable_sudoku.validate_number(num, pos)

#     assert res == False
