from unittest import TestCase


class TestSimpleListComprehensions(TestCase):
    '''Test basic list comprehensions'''

    def test_copy_empty_list(self):

        a = []

        b = [x for x in a]

        print(b)

        self.assertSequenceEqual(a, b)

    def test_copy_one_element_list(self):

        a = [0]

        b = [x for x in a]

        print(b)

        self.assertSequenceEqual(a, b)

    def test_transform_three_element_list(self):

        a = [0, 1, 2]

        # perform as list comprehension
        b = [2 * x for x in a]

        # perform as for loop
        c = []
        for x in a:
            c.append(2 * x)

        print(a)
        print(b)
        print(c)

        self.assertNotEqual(a, b)
        self.assertEqual(b, c)

    def test_transform_nested_list(self):

        a = [1, 2, 3]

        b = [
            2 * y
            for y in [
                1 + x
                for x in a
            ]
        ]

        print(a)
        print(b)

        self.assertNotEqual(a, b)

    def test_filter_list(self):
        from loclasspy.fizzbuzz import is_fizz

        a = range(1, 101)

        # perform as list comprehension
        b = [x for x in a if is_fizz(x)]

        # perform as filter
        c = list(filter(is_fizz, a))

        # perform as for loop
        d = []
        for x in a:
            if is_fizz(x):
                d.append(x)

        print(b)
        print(c)
        print(d)

    def test_fizzbuzz(self):
        from loclasspy.fizzbuzz import fizz, buzz, fizzbuzz

        a = range(1, 101)

        fb = [
            next(filter(None, t))
            for t in [
                (
                    fizzbuzz(n),
                    fizz(n),
                    buzz(n),
                    n
                ) for n in a
            ]
        ]

        print(fb)

    def test_fizzbuzz_2(self):
        from loclasspy.fizzbuzz import return_fizzbuzz

        a = range(1, 101)

        fb = [return_fizzbuzz(x) for x in a]

        print(fb)
