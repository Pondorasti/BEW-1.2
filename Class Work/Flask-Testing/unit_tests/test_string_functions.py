from unittest import TestCase

from .string_functions import *


class StringTests(TestCase):
    def test_greeting_jeremy(self):
        """Test for greet_by_name"""
        expected = 'Hello, Jeremy!'
        actual = greet_by_name('Jeremy')
        self.assertEqual(actual, expected)

    def test_greeting_dani(self):
        """Test for greet_by_name"""
        expected = 'Hello, Dani!'
        actual = greet_by_name('Dani')
        self.assertEqual(actual, expected)

    def test_reverse_long(self):
        """Test reversing a long string."""
        expected = 'urdnaxela'
        actual = reverse("alexandru")
        self.assertEqual(actual, expected)

    def test_reverse_short(self):
        """Test reversing a short string."""
        expected = 'xela'
        actual = reverse("alex")
        self.assertEqual(actual, expected)

    def test_reverse_words_long(self):
        """Test reversing words in a long string."""
        expected = 'xela si derob'
        actual = reverse_words("alex is bored")
        self.assertEqual(actual, expected)

    def test_reverse_words_short(self):
        """Test reversing words in a short string."""
        expected = 'si derob'
        actual = reverse_words("is bored")
        self.assertEqual(actual, expected)

    def test_sarcastic_long(self):
        """Test sarcastic-ifying a long string."""
        expected = 'AlExAnDrU'
        actual = sarcastic("alexandru")
        self.assertEqual(actual, expected)

    def test_sarcastic_short(self):
        """Test sarcastic-ifying a short string."""
        expected = 'AlEx'
        actual = sarcastic("alex")
        self.assertEqual(actual, expected)

    def test_find_longest_word_empty(self):
        expected = ""
        actual = find_longest_word("")
        self.assertEqual(actual, expected)
