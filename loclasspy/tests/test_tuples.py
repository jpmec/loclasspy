from unittest import TestCase


class TestTuples(TestCase):

    def test_empty_tuple(self):

        t = ()

        print(type(t))
        print(t)

        self.assertEqual(0, len(t))

    def test_one_element_tuple(self):

        t = (0,)

        print(type(t))
        print(t)

        self.assertEqual(1, len(t))

    def test_two_element_tuple(self):

        t = (0, 1)

        print(type(t))
        print(t)

        print(t[0])
        print(t[1])

        self.assertEqual(2, len(t))

    def test_two_element_tuple_with_commas(self):

        t = 0, 1

        print(type(t))
        print(t)

        self.assertEqual(2, len(t))

    def test_tuple_modify(self):

        t = 0, 1, 2

        with self.assertRaises(TypeError):
            t[1] = 42

    def test_tuple_zip_two(self):
        from loclasspy.fizzbuzz import return_fizzbuzz

        a = range(1, 101)
        b = map(return_fizzbuzz, a)

        for t in zip(a, b):
            print(t)

    def test_tuple_zip_four(self):
        from loclasspy.fizzbuzz import is_fizz, is_buzz, is_fizzbuzz

        a = range(1, 101)

        f = map(is_fizz, a)
        b = map(is_buzz, a)
        fb = map(is_fizzbuzz, a)

        fizzbuzz = list(zip(fb, f, b, a))

        print(fizzbuzz)

    def test_fizzbuzz(self):
        from loclasspy.fizzbuzz import fizz, buzz, fizzbuzz

        a = range(1, 101)

        fb = list(
            map(
                lambda x: next(filter(None, x)),
                zip(
                    map(fizz, a),
                    map(buzz, a),
                    map(fizzbuzz, a),
                    a
                )
            )
        )

        print(fb)
