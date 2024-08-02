# Change the displayed grid
if st.session_state.clear_grid == False:

    if st.session_state.solve_grid == False:
        edited_df = display_data_editor(df, top)
        st.session_state.grid = edited_df

    else:
        edited_df = st.session_state.grid
        edited_board = edited_df.values.tolist()

        # Check is the grid can actually be solved before attempting
        if check_grid_solvable(edited_board):

            su.board = edited_board
            su.convert_blanks_to_zeroes()
            su.convert_to_int()
            if su.solve():
                su.convert_to_str()
                solved_df = pd.DataFrame(su.board)
                edited_df = display_data_editor(solved_df, top)
            else:
                bottom.write('No valid solution found.')
                edited_df = display_data_editor(df, top)

        else:
            edited_df = display_data_editor(empty_df, top)
            bottom.write('Sudoku cannot be solved with less than 17 numbers provided.')

        st.session_state.grid = edited_df
else:
    st.session_state['grid'] = empty_df

    edited_df = display_data_editor(empty_df, top)
    st.session_state.grid = edited_df