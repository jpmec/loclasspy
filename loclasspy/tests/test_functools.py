from unittest import TestCase


class TestFunctools(TestCase):

    def test_reduce(self):

        from functools import reduce

        a = [2, 3, 4]

        b = reduce(lambda x, y: x / y, a, 1)

        print(b)

        print(((1 / 2) / 3) / 4)

    def test_simple_partial(self):

        from functools import partial

        def something_something(one_thing, other_thing):
            return "%s %s" % (one_thing, other_thing)

        something = partial(something_something, 'hello')

        print(something('world'))

    def test_fuzzball(self):

        from functools import partial
        from loclasspy.fizzbuzz import fizz, buzz, fizzbuzz, yield_fizzbuzz

        fuzz = partial(fizz, value='Fuzz')
        ball = partial(buzz, value='Ball')
        fuzzball = partial(fizzbuzz, value='FuzzBall')

        yield_fuzzball = partial(yield_fizzbuzz, f=fuzz, b=ball, fb=fuzzball)

        print(list(yield_fuzzball(100)))
