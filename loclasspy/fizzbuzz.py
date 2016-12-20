'''
FizzBuzz related functions.
'''


def is_fizz(x, n=3):
    '''Fizz test, returns True if fizzy'''
    return x % n == 0


def is_buzz(x, n=5):
    '''Buzz test, returns True if buzzy'''
    return x % n == 0


def is_fizzbuzz(x, is_fizzy=is_fizz, is_buzzy=is_buzz):
    '''FizzBuzz test, returns True if fizzbuzzy'''
    return is_fizzy(x) and is_buzzy(x)


def fizz(x, value='Fizz'):
    '''Returns fizz value if fizzy'''
    return value if is_fizz(x) else None


def buzz(x, value='Buzz'):
    '''Returns buzz value if buzzy'''
    return value if is_buzz(x) else None


def fizzbuzz(x, value='FizzBuzz'):
    '''Returns fizzbuzz value if fizzbuzzy'''
    return value if is_fizzbuzz(x) else None


def return_fizzbuzz(x):
    return fizzbuzz(x) or fizz(x) or buzz(x) or x


def yield_fizzbuzz(n, f=fizz, b=buzz, fb=fizzbuzz):
    x = 1
    while x <= n:
        yield fb(x) or f(x) or b(x) or x
        x += 1
