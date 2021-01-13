# -*- coding: utf8 -*-

import unittest
import random
import basic_math as bm


class TestTextProcessing(unittest.TestCase):
    def test_normalize(self):
        test_str = "This is an example."
        pred = bm.normalize(test_str)
        self.assertEqual(pred, "this is an example.")

        test_str = "   EXTRA   SPACE   "
        pred = bm.normalize(test_str)
        self.assertEqual(pred, "extra space")

        test_str = "THIS IS ALL CAPS!!"
        pred = bm.normalize(test_str)
        self.assertEqual(pred, "this is all caps!!")

        test_str = "                   "
        pred = bm.normalize(test_str)
        self.assertEqual(pred, "")

        test_str = "this is all lower space..."
        pred = bm.normalize(test_str)
        self.assertEqual(pred, "this is all lower space...")

        test_str = "  H  e  L    l   O   !"
        pred = bm.normalize(test_str)
        self.assertEqual(pred, "h e l l o !")

        test_str = ""
        pred = bm.normalize(test_str)
        self.assertEqual(pred, "")

        test_str = "........"
        pred = bm.normalize(test_str)
        self.assertEqual(pred, "........")

        test_str = "EX  A M P     LE"
        pred = bm.normalize(test_str)
        self.assertEqual(pred, "ex a m p le")

        test_str = "Test Text Normalization"
        pred = bm.normalize(test_str)
        self.assertEqual(pred, "test text normalization")

        test_str = "AbCd EfGh IjKl MnOp"
        pred = bm.normalize(test_str)
        self.assertEqual(pred, "abcd efgh ijkl mnop")

    def test_no_vowels(self):
        test_str = "This is an example."
        pred = bm.no_vowels(test_str)
        self.assertEqual(pred, "Ths s n xmpl.")

        test_str = "We love Python!"
        pred = bm.no_vowels(test_str)
        self.assertEqual(pred, "W lv Pythn!")

        test_str = "AEIOU"
        pred = bm.no_vowels(test_str)
        self.assertEqual(pred, "")

        test_str = "aeiou"
        pred = bm.no_vowels(test_str)
        self.assertEqual(pred, "")

        test_str = "QWERTY"
        pred = bm.no_vowels(test_str)
        self.assertEqual(pred, "QWRTY")

        test_str = "qwerty"
        pred = bm.no_vowels(test_str)
        self.assertEqual(pred, "qwrty")

        test_str = "AI for ALL!"
        pred = bm.no_vowels(test_str)
        self.assertEqual(pred, " fr LL!")

        test_str = "Are there any vowels?"
        pred = bm.no_vowels(test_str)
        self.assertEqual(pred, "r thr ny vwls?")

        test_str = ""
        pred = bm.no_vowels(test_str)
        self.assertEqual(pred, "")

        test_str = "abcdefghijklmnopqrstuvwxyz"
        pred = bm.no_vowels(test_str)
        self.assertEqual(pred, "bcdfghjklmnpqrstvwxyz")
