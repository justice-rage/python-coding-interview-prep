def count_unique(seen):
    '''
    Count number of unique characters in s
    >>> count_unique("aabb")
    2
    >>> count_unique("abcdef")
    6
    '''
    # seen_characters = [] # O(1)
    # # 0 + 1 + 2 + 3 + 4 + ... + n - 1 ~= n^2
    # for c in s: # O(n)
    #     if c not in seen_characters: # O(n)
    #         seen_characters.append(c) # O(n)
    # return len(seen_characters) # O(n^2)

    # seen_characters = set() # O(1)
    # for character in seen: # O(n)
    #     if character not in seen_characters: # O(1)
    #         seen_characters.add(character) O(1)
    # return len(seen_characters) O(n)

    # return len({character for character in seen}) # O(n)

    return len(set(seen)) # O(n)