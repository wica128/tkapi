import unittest

import tkapi.commissie
import tkapi.util


class TestCommissie(unittest.TestCase):

    def test_get_commissies(self):
        max_items = None
        commissies = tkapi.commissie.get_commissies(max_items=max_items)
        for commissie in commissies:
            print('===========')
            print(commissie)
            for lid in commissie.leden:
                if lid.persoon:
                    print('\t' + str(lid))