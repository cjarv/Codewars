"""
Pirates have notorious difficulty with enunciating. They tend to blur all the letters together and scream at people.

At long last, we need a way to unscramble what these pirates are saying.

Write a function that will accept a jumble of letters as well as a dictionary, and output a list of words that the pirate might have meant.

For example:

grabscrab( "ortsp", ["sport", "parrot", "ports", "matey"] )
Should return ["sport", "ports"].

Return matches in the same order as in the dictionary. Return an empty array if there are no matches.
"""



def grabscrab(jumble="", possible=[]):
    """
    This will accept a scramble of letters as well as a list of possible matches Was unsure of the directions as it contradicts their example
    :param jumble: str
    :param possible: list
    :return: list
    """
    matches = []
    # sort a list to check against
    sorted_jumble = sorted(list(jumble))
    for each in possible:
        # sort each as list to compare against jumble
        if sorted(list(each)) == sorted_jumble:
            matches.append(each)

    return matches


