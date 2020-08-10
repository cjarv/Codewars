"""
Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

Example:

Input:

'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

Output:

'alpha beta gamma delta'
"""


def remove_duplicate_words(entry):
    """
    This will remove duplicate words from a string
    :param entry: string
    :return: string
    """
    # set will remove duplicates and " ".join will rejoin them
    clean_entry = list(set(entry.split()))
    return " ".join(clean_entry)

