"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError(f'number of primes={number_of_primes} must be a positive value.')

    list = []
    count = 0
    number = 2
    while count < number_of_primes:
        divisible = False
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            list.append(number)
            count += 1
        number += 1
    return list
