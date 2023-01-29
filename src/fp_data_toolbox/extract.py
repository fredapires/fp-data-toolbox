###
import pandas as pd


def extract_excel_data(file_path, sheet_name, start_cell):
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
    start_row, start_col = pd.util.excel._column_index_from_string(start_cell)
    df = df.iloc[start_row:, start_col:]
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    return df
