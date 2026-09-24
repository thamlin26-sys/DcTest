#!/bin/python

'''Practice writing functions and using doctests.''' 


def is_even(n):
    '''Return True if n is even, otherwise False.

    >>> is_even(0)
    True
    >>> is_even(-9)
    False
    '''
    return n % 2 == 0


def is_odd(n):
    '''Return True if n is odd, otherwise False.

    >>> is_odd(1)
    True
    >>> is_odd(-8)
    False
    '''
    return n % 2 != 0


def absolute_value(n):
    '''Return the absolute value of n.

    >>> absolute_value(-5.5)
    5.5
    '''
    if n < 0:
        return -n
    return n


def max_num(a, b):
    '''Return the maximum of a and b.

    >>> max_num(-4, -5)
    -4
    '''
    if a >= b:
        return a
    return b


def max_num_4(a, b, c, d):
    '''Return the maximum of four values.

    >>> max_num_4(2, 3, 4, 1)
    4
    '''
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    if d > largest:
        largest = d
    return largest


def max_num_abs(a, b):
    '''Return the value with the greatest absolute value.

    >>> max_num_abs(-4, -5)
    -5
    '''
    if abs(a) >= abs(b):
        return a
    return b


def is_leap_year(n):
    '''Return True if n is a leap year in the Gregorian calendar.

    >>> is_leap_year(2000)
    True
    >>> is_leap_year(2200)
    False
    '''
    return n % 400 == 0 or (n % 4 == 0 and n % 100 != 0)


def num_digits(n):
    '''Return the number of decimal digits in n, excluding a minus sign.

    >>> num_digits(0)
    1
    >>> num_digits(-123)
    3
    '''
    n = abs(n)
    count = 1
    while n >= 10:
        n //= 10
        count += 1
    return count


def factorial(n):
    '''Return n factorial.

    >>> factorial(0)
    1
    >>> factorial(5)
    120
    '''
    result = 1
    for value in range(1, n + 1):
        result *= value
    return result


def is_prime(n):
    '''Return True if n is prime, otherwise False.

    >>> is_prime(2)
    True
    >>> is_prime(99)
    False
    '''
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def is_perfect_square(n):
    '''Return True if n is the square of an integer.

    >>> is_perfect_square(81)
    True
    >>> is_perfect_square(-144)
    False
    '''
    if n < 0:
        return False
    i = 0
    while i * i <= n:
        if i * i == n:
            return True
        i += 1
    return False


def fibonacci(n):
    '''Return the nth Fibonacci number, with fibonacci(0) equal to 0.

    >>> fibonacci(0)
    0
    >>> fibonacci(7)
    13
    '''
    if n <= 0:
        return 0
    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous


def cigar_party(cigars, is_weekend):
    '''Return whether the squirrel party has enough cigars.

    >>> cigar_party(50, False)
    True
    >>> cigar_party(70, True)
    True
    '''
    return cigars >= 40 and (is_weekend or cigars <= 60)


def speeding_fine(speed, birthday):
    '''Return the speeding fine, accounting for the birthday allowance.

    >>> speeding_fine(61, True)
    0
    >>> speeding_fine(81, False)
    2000
    '''
    if birthday:
        speed -= 5
    if speed <= 60:
        return 0
    if speed <= 80:
        return 100
    return 2000


def near_ten(x):
    '''Return True if x is within 2 of a multiple of 10.

    >>> near_ten(8)
    True
    >>> near_ten(-43)
    False
    '''
    remainder = x % 10
    return remainder <= 2 or remainder >= 8


def love6(a, b):
    '''Return True if either value is 6, or their sum or difference is 6.

    >>> love6(10, 4)
    True
    >>> love6(4, 5)
    False
    '''
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6


def funny_sum(a, b, c):
    '''Sum only values that do not equal either of the other values.

    >>> funny_sum(3, 2, 3)
    2
    >>> funny_sum(3, 3, -3)
    -3
    '''
    total = 0
    if a != b and a != c:
        total += a
    if b != a and b != c:
        total += b
    if c != a and c != b:
        total += c
    return total


def median(a, b, c):
    '''Return the middle of three values.

    >>> median(3, 1, 2)
    2
    '''
    return sorted([a, b, c])[1]


def sum_between(a, b):
    '''Sum the integers from a to b inclusive, following endpoint order.

    >>> sum_between(1, 3)
    6
    >>> sum_between(2, 1)
    3
    >>> sum_between(10, -1000)
    -500445
    '''
    step = 1 if a <= b else -1
    total = 0
    for value in range(a, b + step, step):
        total += value
    return total


def largest(xs):
    '''Return the largest element, or None for an empty list.

    >>> largest([1, 2, 3])
    3
    >>> largest([])
    '''
    if not xs:
        return None
    return max(xs)


def last_element(xs):
    '''Return the last element, or None for an empty list.

    >>> last_element(['a', 'b'])
    'b'
    >>> last_element([])
    '''
    if not xs:
        return None
    return xs[-1]


def last_element_list(xs):
    '''Return a one-element list containing the last item, or [] if empty.

    >>> last_element_list([1, 2, 3])
    [3]
    >>> last_element_list([])
    []
    '''
    if not xs:
        return []
    return [xs[-1]]


def first_three(xs):
    '''Return the first three elements of xs, or all if there are fewer.

    >>> first_three([0, 1, 2, 3])
    [0, 1, 2]
    '''
    return xs[:3]


def last_three(xs):
    '''Return the last three elements of xs, or all if there are fewer.

    >>> last_three([0, 1, 2, 3])
    [1, 2, 3]
    '''
    return xs[-3:]


def largest3(xs):
    '''Return up to the three largest elements in sorted order.

    >>> largest3([99, -56, 80, 100, 90])
    [90, 99, 100]
    >>> largest3([])
    []
    '''
    return sorted(xs)[-3:]


def filter_odd(xs):
    '''Return the elements of xs that are even.

    >>> filter_odd([4, 5, 6, 7])
    [4, 6]
    '''
    result = []
    for value in xs:
        if value % 2 == 0:
            result.append(value)
    return result


def filter_even(xs):
    '''Return the elements of xs that are odd.

    >>> filter_even([4, 5, 6, 7])
    [5, 7]
    '''
    result = []
    for value in xs:
        if value % 2 != 0:
            result.append(value)
    return result


def bigger_than_10(xs):
    '''Count the elements of xs that are greater than 10.

    >>> bigger_than_10([10, 11, 12])
    2
    '''
    count = 0
    for value in xs:
        if value > 10:
            count += 1
    return count


def second_largest(xs):
    '''Return the second item in sorted descending order, or None if too short.

    >>> second_largest([1, 2, 3])
    2
    >>> second_largest([])
    '''
    if len(xs) < 2:
        return None
    return sorted(xs)[-2]


def has_index_at_value(xs):
    '''Return True if xs has an element equal to its index.

    >>> has_index_at_value([1, 1])
    True
    >>> has_index_at_value([1, 0])
    False
    '''
    for i in range(len(xs)):
        if xs[i] == i:
            return True
    return False


def nested_filter_odd(xss):
    '''Flatten nested lists, keeping only even elements.

    >>> nested_filter_odd([[2, 4, 5], [1, 3, 6]])
    [2, 4, 6]
    '''
    result = []
    for xs in xss:
        for value in xs:
            if value % 2 == 0:
                result.append(value)
    return result


def flatten(xss):
    '''Flatten a list of lists into one list.

    >>> flatten([[1, 2], [3, 4]])
    [1, 2, 3, 4]
    '''
    result = []
    for xs in xss:
        for value in xs:
            result.append(value)
    return result


def filter_flatten(xss):
    '''Return the diagonal elements of a list of lists, skipping missing ones.

    >>> filter_flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [1, 5, 9]
    '''
    result = []
    for i in range(len(xss)):
        if i < len(xss[i]):
            result.append(xss[i][i])
    return result
