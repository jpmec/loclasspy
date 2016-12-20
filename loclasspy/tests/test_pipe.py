from unittest import TestCase


class TestPipeModule(TestCase):

    def test_fizzbuzz(self):

        from pipe import select, as_list
        from loclasspy.fizzbuzz import return_fizzbuzz

        fb = range(1, 101) | select(return_fizzbuzz) | as_list

        print(fb)

        fb = [return_fizzbuzz(x) for x in range(1, 101)]
        print(fb)
