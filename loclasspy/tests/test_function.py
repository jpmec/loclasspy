from unittest import TestCase


class TestFunction(TestCase):

    def test_fizzbuzz(self):
        for x in range(1, 101):

            fizz = x % 3 == 0
            buzz = x % 5 == 0
            fizzbuzz = fizz and buzz

            if fizzbuzz:
                print('FizzBuzz')

            elif fizz:
                print('Fizz')

            elif buzz:
                print('Buzz')

            else:
                print(x)

    def test_fizzbuzz_function(self):
        from loclasspy.fizzbuzz import return_fizzbuzz

        for x in range(1, 101):
            print(return_fizzbuzz(x))

    def test_fizzbuzz_map(self):
        from loclasspy.fizzbuzz import return_fizzbuzz

        a = range(1, 101)

        for x in map(return_fizzbuzz, a):
            print(x)

    def test_fizzbuzz_map_list(self):
        from loclasspy.fizzbuzz import return_fizzbuzz

        a = range(1, 101)

        b = list(map(return_fizzbuzz, a))

        print(b)

    def test_filter_fizz(self):
        from loclasspy.fizzbuzz import is_fizz

        a = range(1, 101)

        b = list(filter(is_fizz, a))

        print(b)

    def test_filter_fizz_lambda(self):

        a = range(1, 101)

        b = list(filter(lambda x: x % 3 == 0, a))

        print(b)
