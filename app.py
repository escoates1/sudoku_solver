import streamlit as st
import pandas as pd
import sudoku
import example_board
from app_funcs import display_data_editor, check_grid_solvable

su = sudoku.SudokuSolver()
board = su.board
board = su.convert_zeroes_to_blanks()
board = su.convert_to_str()

# Dataframe populated with example board, used for resets
ex_df = pd.DataFrame(example_board.board)

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

# Initialise the session states
if "clear_grid" not in st.session_state:
    st.session_state.clear_grid = False

if "solve_grid" not in st.session_state:
    st.session_state.solve_grid = False

if "grid" not in st.session_state:
    st.session_state.grid = ex_df

# Buttons
if left.button("Solve"):
    edited_df = st.session_state.grid
    edited_board = edited_df.values.tolist()
    st.write('solving...')

    # Check is the grid can actually be solved before attempting
    if check_grid_solvable(edited_board):
        su.board = edited_board
        su.convert_blanks_to_zeroes()
        su.convert_to_int()

        if su.solve():
            su.convert_to_str()
            solved_df = pd.DataFrame(su.board)
        else:
            bottom.write('No valid solution found.')
    else:
        bottom.write('Sudoku cannot be solved with less than 17 numbers provided.')

    # Update session state for displaying the grid later
    st.session_state.grid = solved_df

if middle.button("Clear"):
    st.session_state.grid = empty_df
    st.rerun()

if right.button('Reset'):
    st.session_state.grid = ex_df
    st.rerun()

# Display the board currently stored as a session state var
edited_df = display_data_editor(st.session_state.grid, top)

# Update the session state var with any changes to the data editor
st.session_state.grid = edited_df

# st.data_editor(data_df)

# # Change the displayed grid
# if st.session_state.clear_grid == False:

#     # Reset the grid 
#     if st.session_state.solve_grid == False:
#         st.write('trying to reset the grid')
#         edited_df = display_data_editor(ex_df, top)
#         st.session_state.grid = ex_df

#     # Solve the grid
#     else:
#         edited_df = st.session_state.grid
#         edited_board = edited_df.values.tolist()

#         # Check is the grid can actually be solved before attempting
#         if check_grid_solvable(edited_board):

#             su.board = edited_board
#             su.convert_blanks_to_zeroes()
#             su.convert_to_int()
#             if su.solve():
#                 su.convert_to_str()
#                 solved_df = pd.DataFrame(su.board)
#                 edited_df = display_data_editor(solved_df, top)
#             else:
#                 bottom.write('No valid solution found.')
#                 edited_df = display_data_editor(df, top)

#         else:
#             edited_df = display_data_editor(empty_df, top)
#             bottom.write('Sudoku cannot be solved with less than 17 numbers provided.')

#         st.session_state.grid = edited_df
# else:
#     # Clear the grid
#     st.session_state['grid'] = empty_df

#     edited_df = display_data_editor(empty_df, top)
#     st.session_state.grid = edited_df
    
# # Buttons
# if left.button("Solve"):
#     st.session_state['clear_grid'] = False
#     st.session_state['solve_grid'] = True
#     st.rerun()

# if middle.button("Clear"):
#     st.session_state['clear_grid'] = True
#     st.session_state['solve_grid'] = False
#     st.rerun()

# if right.button('Reset'):
#     st.session_state['clear_grid'] = False
#     st.session_state['solve_grid'] = False
#     st.session_state['grid'] = ex_df
#     st.rerun()

if st.button('Refresh page'):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.cache_data.clear()
    st.rerun()

# for key in st.session_state.keys():
#     st.write(key, st.session_state[key])

st.write(st.session_state)