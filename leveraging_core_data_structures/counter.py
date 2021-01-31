from collections import defaultdict, Counter

def top_three_letters(string):
    '''
    Given a string find the top three most frequent letters. This method 
    should return a list of tuples, where the tuple contains 
    the character and count.

    >>> top_three_letters("abbccc")
    [('c, 3), ('b', 2), ('a', 1)]
    >>> top_three_letters("aabbccd")
    [('a', 2), ('b, 2), ('c', 2)]
    '''

    """
    1) Loop through the string and store the count for each letter.
    2) Sort the dictionary by the count and find the top three most
    frequent letters.
    3) Return a formatted list to match the output.
    """

    # counter = defaultdict(int)
    # for c in string:
    #     counter[c] += 1
    # top_three_letters = sorted(
    #     counter, key=lambda k: counter[k], reverse=True)[:3]
    # return [(c, counter[c]) for c in top_three_letters]

    def top_three_letters_better(string):
        return Counter(string).most_common(3)
