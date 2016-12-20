from unittest import TestCase


class TestGeneratorExpressions(TestCase):

    def test_iterate_once(self):

        a = (x for x in range(1, 3))

        print('first time')
        for x in a:
            print(x)

        print('second time')
        for x in a:
            print(x)

    def test_fizzbuzz(self):
        from loclasspy.fizzbuzz import fizz, buzz, fizzbuzz

        a = range(1, 101)

        fb = (
            next(filter(None, t))
            for t in (
                (
                    fizzbuzz(n),
                    fizz(n),
                    buzz(n),
                    n
                ) for n in a
            )
        )

        print(fb)
        print(list(fb))
