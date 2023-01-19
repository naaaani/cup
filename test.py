#!/usr/bin/python3

import unittest
import helo

class TestStringMethods(unittest.TestCase):

    def test_fake_choose(self):

        ch = helo.fake_choose(1, 2)
        self.assertEqual(ch, 1)

    def test_game_fake(self):

        partics = ["a", "b", "c", "d"]
        winner = helo.game(partics, helo.fake_choose)
        self.assertEqual(winner, "a")

if __name__ == '__main__':
    unittest.main()
