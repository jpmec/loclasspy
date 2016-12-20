from unittest import TestCase


class TestIterators(TestCase):

    def test_cannot_iterate_integer(self):

        a = 1

        with self.assertRaises(TypeError):
            iter(a)

    def test_iterate_empty_list(self):

        a = []

        i = iter(a)

        print(type(i))
        print(i)

        with self.assertRaises(StopIteration):
            next(i)

    def test_can_iterate_list(self):

        a = [1, 2]

        i = iter(a)

        print(type(i))
        print(i)

        x = next(i)

        print(type(x))
        print(x)

        x = next(i)

        print(type(x))
        print(x)

        with self.assertRaises(StopIteration):
            next(i)

    def test_for_in_list(self):

        a = [1, 2]

        # these two loops are equivalent
        for x in iter(a):
            print(x)

        for x in a:
            print(x)

    def test_iterator_unpacking(self):

        a = [1, 2]

        x, y = iter(a)

        print(x)
        print(y)

        x, y = a

        print(x)
        print(y)
