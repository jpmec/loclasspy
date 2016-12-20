from unittest import TestCase


class TestGenerators(TestCase):

    def test_simple_generator(self):

        def g():
            yield 1

        a = g()

        print(type(a))
        print(a)

        b = next(a)

        print(type(b))
        print(b)

        with self.assertRaises(StopIteration):
            next(a)

    def test_infinite_generator(self):

        def g():
            i = 1
            while True:
                i *= 0.5
                yield i

        a = g()

        print(type(a))
        print(a)

        b = next(a)

        print(type(b))
        print(b)

        c = next(a)

        print(type(c))
        print(c)

    def test_fizzbuzz(self):
        from loclasspy.fizzbuzz import yield_fizzbuzz

        fb = yield_fizzbuzz(100)

        print(fb)

        print(list(fb))
