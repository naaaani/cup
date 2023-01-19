#!/usr/bin/python3

import unittest
import helo

def choose_first(p1, p2):
    return p1

def choose_smaller(p1, p2):
    return min(p1, p2)

class TestStringMethods(unittest.TestCase):

    def test_choose_first(self):

        ch = choose_first(1, 2)
        self.assertEqual(ch, 1)

    def test_game_first(self):

        partics = ["a", "b", "c", "d"]
        winner = helo.game(partics, choose_first)
        self.assertEqual(winner, "a")

    def test_game_smaller1(self):

        partics = ["d", "b", "c", "f"]
        winner = helo.game(partics, choose_smaller)
        self.assertEqual(winner, "b")

    def test_game_smaller2(self):

        partics = ["d", "b", "c", "a"]
        winner = helo.game(partics, choose_smaller)
        self.assertEqual(winner, "a")

    def test_game_empty(self):

        partics = []
        with self.assertRaises(AssertionError):
            helo.game(partics, choose_smaller)

    def test_game_only1(self):

        partics = ["d"]
        winner = helo.game(partics, choose_smaller)
        self.assertEqual(winner, "d")



if __name__ == '__main__':
    unittest.main()
