from unittest import TestCase


class TestListComprehensions(TestCase):

    def test_empty_list(self):
        '''Test a list comprehension on an empty list'''

        # create an empty list
        a = []

        # perform a list comprehension
        b = [x for x in a]

        print(b)

        self.assertSequenceEqual(a, b)
