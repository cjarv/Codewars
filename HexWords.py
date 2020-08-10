"""
As hex values can include letters A through to F, certain English words can be spelled out, such as CAFE, BEEF, or FACADE. This vocabulary can be extended by using numbers to represent other letters, such as 5EAF00D, or DEC0DE5.

Given a string, your task is to return the decimal sum of all words in the string that can be interpreted as such hex values.

Example
Working with the string BAG OF BEES:

BAG ==> 0 as it is not a valid hex value
OF ==> 0F ==> 15
BEES ==> BEE5 ==> 48869
So hex_word_sum('BAG OF BEES') returns the sum of these, 48884.

Notes
Inputs are all uppercase and contain no punctuation
0 can be substituted for O
5 can be substituted for S
"""

import re


def hex_word_sum(words):
    """
    This will convert a string to a hexidecimal value
    :param words: str
    :return: hexidecimal
    """
    # replace each S and 0 before splitting for time
    cleanwords = re.sub("S", "5", re.sub("O", "0", words))
    words = cleanwords.split(" ")

    vals = []
    #test each word for hex value and add it to a list
    for word in words:
        try:
            val = int(word, 16)
            vals.append(val)
        except:
            pass

    # total the hex value
    return sum(vals)

