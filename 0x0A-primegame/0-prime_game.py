#!/usr/bin/python3
"""
A method that determines the winner of a game
of prime numbers.
"""


def prime_numbers_between(n):
    """
    calculate prime numbers between 1 and n

    Args:
        n (int): the number to calculate prime numbers up to

    Returns:
        int: the number of prime numbers between 1 and n
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Determines the winner of a game of prime numbers.

    Args:
        x (int): the number of rounds to play
        nums (list): the list of numbers n to play

    Returns:
        string: the winner of the game (Ben or Maria)
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = prime_numbers_between(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
