# Transformation functions below
# =============================================


# %% imports
import re

# %%
# DONE function that loops over a list ;noted_on:2022-10-10
#   includes progress bar
#   outputs list that then needs to be joined back into original df


def loop_over_list(index_list):
    output_list = []  # setup output list
    i = 0  # setup variable for looping progress bar
    for id in index_list:

        # logic for determining new values goes here

        output_list.append()  # append output list with new value

        # loop orchestration below
        i = i + 1  # iterate on integer
        progress_stat = str(round((i / index), 2)) + \
            ' / 1.0'  # calc for progress
        print(progress_stat, end='\r')  # print progress
    return output_list


# %%

def extract_date_from_string(input_string: str, date_format: str = '%Y-%m-%d') -> str:
    """
    Extracts a date string from an input string using a regular expression.

    The input string must contain a date in the format `YYYY-MM-DD`. By default, the date format of the extracted
    string is `%Y-%m-%d`, but it can be changed using the `date_format` argument.

    Args:
    - input_string (str): The input string from which to extract the date.
    - date_format (str, optional): The desired format of the extracted date string. Default is `%Y-%m-%d`.

    Returns:
    - str: The extracted date string, or `None` if the input string does not contain a date.
    """
    import re
    date_regex = r'\d{4}-\d{2}-\d{2}'
    date_match = re.search(date_regex, input_string)
    if date_match:
        date_string = date_match.group()
        return date_string
    return None
