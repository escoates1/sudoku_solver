import streamlit as st
import uuid

column_options = st.column_config.TextColumn(max_chars=1,
                                             label = "",
                                             validate="^[1-9]*$")

column_config = {str(k): column_options for k in range(0, 9)}

def display_data_editor(data, st_obj):

    edited_df = st_obj.data_editor(data, 
                                   num_rows='fixed',
                                   hide_index=True,
                                   column_config=column_config,
                                   key=st.session_state.grid_widget,
                                   use_container_width=False
                                   )
    
    return edited_df

# def change_data_editor(test_string):
    
#     # edited_rows = st.session_state['grid_widget']['edited_rows']
#     st.session_state.test = test_string
    
    # for row in edited_rows.keys():
    #     for col, val in edited_rows[row].items():
    #         grid.loc[row][col] = val

    # st.session_state.test = grid

    # st.session_state.test = f'[{row}][{col}] = {val}'

def update_grid_widget_key():
    """
    Located on top of the data editor.
    """
    st.session_state.grid_widget = str(uuid.uuid4())

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

    if non_empty_count < 17:
        return False
    else:
        return True
    