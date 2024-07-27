import streamlit as st
import pandas as pd
import sudoku 
from example_board import board

# board = su.board
# print(board)

df = pd.DataFrame(board)

edited_df = st.data_editor(df, 
                           hide_index=True)

print(edited_df)

# if st.button("Solve"):
#     st.write("Solving...")

#     su = sudoku.SudokuSolver(edited_df)
#     su.solve()

#     solved_board = su.board

#     st.table(solved_board)