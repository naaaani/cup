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
        game_result = helo.game(partics, choose_first)
        winner = helo.game_winner(game_result)
        self.assertEqual(winner, "a")

    def test_game_smaller1(self):

        partics = ["d", "b", "c", "f"]
        game_result = helo.game(partics, choose_smaller)
        self.assertEqual(helo.game_winner(game_result), "b")

    def test_game_smaller2(self):

        partics = ["d", "b", "c", "a"]
        game_result = helo.game(partics, choose_smaller)
        self.assertEqual(helo.game_winner(game_result), "a")

    def test_game_empty(self):

        partics = []
        with self.assertRaises(AssertionError):
            helo.game(partics, choose_smaller)

    def test_game_only1(self):

        partics = ["d"]
        game_result = helo.game(partics, choose_smaller)
        self.assertEqual(helo.game_winner(game_result), "d")

    def test_is_pow2(self):

        v = 4
        is_p2 = helo.is_pow2(v)
        self.assertTrue(is_p2)

        self.assertFalse(helo.is_pow2(3))
        self.assertFalse(helo.is_pow2(70))
        self.assertFalse(helo.is_pow2(63))

    def test_normalize_4_to_4(self):

        input = [1, 2, 3, 4]

        output = helo.normalize(input)

        ref = [1, 2, 3, 4]        
        self.assertEqual(output,ref)
    
   
    def test_normalize_3_to_4(self):

        input = [1, 2, 3]

        output = helo.normalize(input)

        ref = [1, 2, 3, None]        
        self.assertEqual(output,ref)

    def test_normalize_6_to_8(self):

        input = [1, 2, 3, 4, 5, 6]

        output = helo.normalize(input)

        ref = [1, 2, 3, 4, 5, None, 6, None]        
        self.assertEqual(output,ref)

    def test_round_to_pow2(self):

        self.assertEqual(helo.round_up_to_pow2(1), 1)
        self.assertEqual(helo.round_up_to_pow2(2), 2)
        self.assertEqual(helo.round_up_to_pow2(3), 4)
        self.assertEqual(helo.round_up_to_pow2(63), 64)
        self.assertEqual(helo.round_up_to_pow2(64), 64)
        self.assertEqual(helo.round_up_to_pow2(65), 128)

    def test_game_res_to_win_1(self):

        gr = [["a", "b", 'c', 'd'], ["a", 'd'], ["d"]]
        winner = helo.game_winner(gr)
        self.assertEqual(winner, "d")

    def test_game_res_to_win_2(self):

        gr = [["a"]] 
        winner = helo.game_winner(gr)
        self.assertEqual(winner, "a")

    def test_game_result(self):

        partics = ["a", "b", "c"]
        game_result = helo.game(partics, choose_smaller)
        ref = [["a", "b", 'c', None], ["a", "c"], ["a"]]
        self.assertEqual(game_result, ref)



if __name__ == '__main__':
    unittest.main()
