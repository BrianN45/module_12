# CS2023 - Lab12

_author_ = "Brian Nguyen"
_credits_ = ["N/A"]
_email_ = "nguyeb2@mail.uc.edu"

'''
NOTES:
- There was no natural function given, so I made it myself.
- There were two instances where the doctests kept failing, which were the type(m) and type(s).
Since there was a blank area under those, I assumed it was supposed to be "<class 'generator'>"
'''

# RQ1
class Cheer:
    """
    >>> UC = Cheer("Bearcats")
    >>> for c in UC:
    ...     print(c)
    ...
    Give me an B
    Give me an e
    Give me an a
    Give me an r
    Give me an c
    Give me an a
    Give me an t
    Give me an s
    """

    # Initialization
    def __init__(self, word):
        self.word = word

    # Create iterable
    def __iter__(self):
        self.position = -1
        return self

    # Return next value
    def __next__(self):
        # Check limit
        if self.position >= len(self.word) - 1:
            raise StopIteration
        # Increment by one
        self.position += 1
        return "Give me an " + self.word[self.position]


# RQ2
class Countdown:
    """
    An iterator that counts down from N to 0.
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in Countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """

    # Initialization
    def __init__(self, count):
        self.count = count

    # Create iterable
    def __iter__(self):
        self.n = self.count + 1
        return self

    # Return next value
    def __next__(self):
        # Check if it's 0
        if self.n <= 0:
            raise StopIteration
        # Subtract by 1 and return
        self.n -= 1
        return self.n


##############
# Generators #
##############

def naturals():
    position = 1

    while True:
        yield position
        position += 1


# RQ3
def evens():
    """A generator function that yields the infinite sequence of all even natural
    numbers, starting at 1.

    >>> m = evens()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    # Create position

    # For loop with naturals
    for i in naturals():
        yield i * 2


# RQ4
def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    # Loop forever
    for i in s:
        # Return the current value multiplied by scale
        yield i * k

# RQ5
def countdown(n):
    """
    A generator that counts down from N to 0.
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    for i in range(n, -1, -1):
        yield i


# RQ6
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    while True:
        yield n

        # hailstone algorithm
        if n == 1:
            return
        elif n % 2 != 0:
            n = 3 * n + 1
        else:
            n = n/2

        # Turn n into an int
        n = int(n)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
