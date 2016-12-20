from unittest import TestCase


class TestItertools(TestCase):

    def test_product(self):

        from itertools import product

        a = product(range(0, 3), range(0, 2))

        print(a)
        print(list(a))

        for i in range(0, 3):
            for j in range(0, 2):
                print((i, j))

        b = [(i, j) for i in range(0, 3) for j in range(0, 2)]

        print(b)

    def test_card_hand(self):

        from itertools import chain, product
        from random import sample

        suits = ('C', 'D', 'H', 'S')

        points = chain(range(2, 11), ('J', 'Q', 'K', 'A'))
        cards = list(product(suits, points))

        hand = sample(cards, 5)

        print(hand)

    def test_permutations(self):

        from itertools import permutations

        print([x for x in permutations('spam')])
