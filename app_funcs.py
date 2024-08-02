import streamlit as st

column_options = st.column_config.TextColumn(label = "",
                                             max_chars=1,
                                             validate="^[1-9]*$")

column_config = {str(k): column_options for k in range(0, 9)}

def display_data_editor(data, st_obj):

    edited_df = st_obj.data_editor(data, 
                                   num_rows='fixed',
                                   hide_index=True,
                                   column_config=column_config,
                                #    key='grid',
                                   use_container_width=False
                                   )
    
    return edited_df

def check_grid_solvable(board):
    """
    Check to see if the grid can be solved. A Sudoku requires
    a minimum of 17 numbers in order to be solved.

    """
    non_empty_count = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != '':
                non_empty_count += 1

    print(non_empty_count)

    if non_empty_count < 17:
        return False
    else:
        return True
    