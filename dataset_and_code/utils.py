def add_unique_student_id(df, col_name, prefix):
    """
    Generates and adds a column of unique, padded student IDs to a DataFrame.

    This function calculates the number of rows in the DataFrame and creates 
    a sequence of IDs starting from 1, padded with leading zeros to a 
    width of 3 (e.g., 'std001', 'std002').

    Args:
        df (pd.DataFrame): The DataFrame to which the IDs will be added.
        col_name (str): The name of the new column to be created.
        prefix (str): The string prefix to go before the numeric ID (e.g., 'std').

    Returns:
        pd.DataFrame: The modified DataFrame containing the new ID column.
    """
    unique_id = [f"{prefix}{i:03d}" for i in range(1, len(df)+1)]
    df[col_name] = unique_id
    return df

def move_std_id(df, col_name):
    move_column = df.pop(col_name)
    df.insert(0, col_name, move_column)
    return df

