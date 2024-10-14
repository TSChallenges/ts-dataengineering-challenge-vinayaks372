# data_engineering/load.py

import sqlite3
import pandas as pd

def load_data(df, db_name, table_name):
    """
    Loads transformed data into a SQLite database.

    Parameters:
    - df (pd.DataFrame): Transformed data.
    - db_name (str): Name of the SQLite database file.
    - table_name (str): Name of the table to insert data into.

    Returns:
    - None
    """
    if df.empty:
        print("Empty DataFrame received. No data to load.")
        return

    try:
        # Connect to SQLite database (creates the database if it doesn't exist)
               #TODO

        # Create a table if it doesn't exist
               #TODO

        # Insert data into the table
               #TODO

        # Commit and close the connection
              #
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
   


