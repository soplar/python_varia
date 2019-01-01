# clarify function calls with keyword arguments
# twitter_search('@obama', False, 20, True)
# clarify
# twitter_search('@obama', retweets=False, numtweets=20, popular=True)

# clarify multiple return values with named tuples

# testen
# eerst simpele functie:
def som(a,b):
    # dus eerst starten met gewenste output in idle van de functie
    """
    >>> som(2,3)
    5
    >>> som(77,8)
    85
    >>> som(-6,9)
    3
    >>> 
    """
    # dan de werkelijke functie
    c = a + b + b
    return c

import doctest
# import collections
# TestResults = collections.namedtuple('TestResults', ['failed', 'attempted'])
if __name__ == "__main__": 
    print(doctest.testmod())

# zonder wijziging gaat alles goed
# verander de functie een beetje c = a + 2*b
# kijk naar de output