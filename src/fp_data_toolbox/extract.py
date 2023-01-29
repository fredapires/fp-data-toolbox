###
import pandas as pd


def ingest_excel_data(file_path: str, sheet_name: str, start_cell: str) -> pd.DataFrame:
    """
    Ingest data from a specified sheet of an Excel file.

    Parameters
    ----------
    file_path : str
        The path to the excel file to be ingested.
    sheet_name : str
        The name of the sheet within the excel file that contains the data to be ingested.
    start_cell : str
        The upper-leftmost cell of the table to be ingested, represented as an Excel cell reference (e.g. "A1", "B2", etc.).

    Returns
    -------
    pd.DataFrame
        A pandas dataframe containing the ingested data.

    """
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
    start_row, start_col = pd.util.excel._column_index_from_string(start_cell)
    df = df.iloc[start_row:, start_col:]
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    return df
