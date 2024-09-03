import streamlit as st
import uuid

# Config for data editor columns
column_options = st.column_config.TextColumn(max_chars=1,
                                             label = "",
                                             validate="^[1-9]*$")

column_config = {str(k): column_options for k in range(0, 9)}

def display_data_editor(data, st_obj):
    """Creates a data editor widget in a specified part of the page with the provided
    data set with a standardized configuration.

    Args:
        data (DataFrame): Data to be converted into data editor
        st_obj (DeltaGenerator): Streamlit object that determines where editor is placed

    Returns:
        st.data_editor: Widget that allows you to edit dataframes
    """

    edited_df = st_obj.data_editor(data, 
                                   num_rows='fixed',
                                   hide_index=True,
                                   column_config=column_config,
                                   key=st.session_state.grid_widget,
                                   use_container_width=False
                                   )
    
    return edited_df

def update_grid_widget_key():
    """
    Generates a unique ID used to update the grid widget key.
    """
    st.session_state.grid_widget = str(uuid.uuid4())

def check_grid_solvable(board):
    """
    Check to see if the grid can be solved. By deduction, a Sudoku requires
    a minimum of 17 numbers in order to be solved. The backtracking algorithm
    could find a working solution with any numbers of starting numbers > 0 but 
    this functionality is undesired.
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
    