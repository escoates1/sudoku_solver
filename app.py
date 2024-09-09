import streamlit as st
import pandas as pd
import sudoku
import example_boards
import uuid
from app_funcs import display_data_editor, check_grid_solvable, update_grid_widget_key

su = sudoku.SudokuSolver()
board = su.board
board = su.convert_zeroes_to_blanks()
board = su.convert_to_str()

# Dataframe populated with example board, used for resets
ex_df = pd.DataFrame(example_boards.board)

# Dataframe holding current status of edited df
df = pd.DataFrame(board)

# Empty dataframe for users to insert puzzles into
empty_df = pd.DataFrame([['' for i in range(9)] for j in range(9)])

# Configuring page layout
top = st.container(height = 375, border=False)
bottom = st.container(height = 100, border=False)

cols = bottom.columns(5,
                      gap='small',
                      vertical_alignment='top')

left = cols[0]
middle = cols[1]
right = cols[2]

# Initialise session state var
if "grid" not in st.session_state:
    st.session_state.grid = ex_df

if "grid_widget" not in st.session_state:
    st.session_state.grid_widget = str(uuid.uuid4())

if "edited_grid" not in st.session_state:
    st.session_state.edited_grid = None

# Buttons
if left.button("Solve", on_click=update_grid_widget_key):
    edited_df = st.session_state.edited_grid
    edited_board = edited_df.values.tolist()

    # Checks the grid has the minimum amount of starting letters to be solved
    # Note this is for a deductive solution, rather than a brute force one
    if check_grid_solvable(edited_board):
        su.board = edited_board
        su.convert_blanks_to_zeroes()
        su.convert_to_int()

        # Check that the starting board is valid before solving 
        solvable, invalid_message = su.validate_starting_board()

        if solvable:
            if su.solve():
                su.convert_to_str()
                edited_df = pd.DataFrame(su.board)
                bottom.write('Solved.')
            else:
                bottom.write('No valid solution found.')
        else:
            bottom.write(invalid_message)
    else:
        bottom.write('Sudoku cannot be solved with less than 17 numbers provided.')

    # Update session state for displaying the grid later
    st.session_state.grid = edited_df

if middle.button("Clear", on_click=update_grid_widget_key):
    st.session_state.grid = empty_df

if right.button('Reset', on_click=update_grid_widget_key):
    st.session_state.grid = ex_df

# Display the board currently stored as a session state var
edited_df = display_data_editor(st.session_state.grid, top)
st.session_state.edited_grid = edited_df