import sys

"""
We can use the hash function to see if we have the same chars.
We need to sort each word by alphabetical order to make sure that the hashes
will match regardless of order
"""


def get_hashes(path="word.txt"):
    # read the file, get hashes of each
    with open(path, "r") as ff:
        contents = [s.strip() for s in ff.readlines()]
        ff.close()

    # return hashmap {hash of chars in word: word}
    d = {}
    for word in contents:
        hashed = hash("".join(sorted(word)))
        if hashed in d:
            # add to list
            d[hashed].append(word)
        else:
            # create a new register
            d[hashed] = [word]
    return d


def unscramble(s):
    # see if we have a match
    hashed = hash("".join(sorted(s)))
    return get_hashes()[hashed]


print(unscramble(sys.argv[1]))
