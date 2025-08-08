import unittest

from ciphers.base import Cipher
from ciphers.exceptions import InvalidPairings
from ciphers.monoalphabetic import Vatsyayana


class TestVatsyayanaCipher(unittest.TestCase):
    def test_simple_string(self):
        """
        Testing encryption/decryption on message containing only alphabet
        """

        pairings = [
            ("E", "l"),
            ("2", "e"),
            ("Z", "8"),
            ("i", "r"),
            ("t", "W"),
            ("g", "6"),
            ("3", "4"),
            ("k", "F"),
            ("5", "V"),
            ("d", "n"),
            ("v", "X"),
            ("C", "S"),
            ("G", "9"),
            ("T", "c"),
            ("N", "R"),
            ("f", "L"),
            ("u", "m"),
            ("M", "b"),
            ("x", "j"),
            ("A", "D"),
            ("I", "Y"),
            ("q", "p"),
            ("w", "7"),
            ("h", "0"),
            ("a", "P"),
            ("y", "s"),
            ("O", "Q"),
            ("J", "z"),
            ("o", "B"),
            ("U", "1"),
            ("K", "H"),
        ]

        vatsyayana_cipher: Cipher = Vatsyayana(pairings)
        plain_text: str = "Hello"
        encrypted_text: str = "K2EEB"

        self.assertEqual(vatsyayana_cipher.encode(plain_text), encrypted_text)
        self.assertEqual(vatsyayana_cipher.decode(encrypted_text), plain_text)

    def test_invalid_pairings_partial_pairings(self):
        """
        Test configuring Vatsyayana cipher with invalid pairings
        """

        pairings = [
            ("E", "l"),
            ("2", "e"),
            ("Z", "8"),
            ("i", "r"),
            ("t", "W"),
            ("g", "6"),
            ("3", "4"),
            ("k", "F"),
            ("5", "V"),
            ("d", "n"),
            ("v", "X"),
            ("C", "S"),
            ("G", "9"),
            ("T", "c"),
            ("N", "R"),
            ("f", "L"),
            ("u", "m"),
            ("M", "b"),
            ("x", "j"),
            ("A", "D"),
        ]

        with self.assertRaises(InvalidPairings) as context:
            Vatsyayana(pairings)

        self.assertIn("not all characters", str(context.exception))

    def test_invalid_pairings_repeated_chars(self):
        """
        Test configuring Vatsyayana cipher with invalid pairings
        """

        pairings = [
            ("E", "l"),
            ("2", "e"),
            ("Z", "8"),
            ("i", "r"),
            ("t", "W"),
            ("g", "W"),  # `W` repeated here
            ("3", "4"),
            ("k", "F"),
            ("5", "V"),
            ("d", "n"),
            ("v", "X"),
            ("C", "S"),
            ("G", "9"),
            ("T", "c"),
            ("N", "R"),
            ("f", "L"),
            ("u", "m"),
            ("M", "b"),
            ("x", "j"),
            ("A", "D"),
            ("I", "Y"),
            ("q", "p"),
            ("w", "7"),
            ("h", "0"),
            ("a", "P"),
            ("y", "s"),
            ("O", "Q"),
            ("J", "z"),
            ("o", "B"),
            ("U", "1"),
            ("K", "H"),
        ]

        with self.assertRaises(InvalidPairings) as context:
            Vatsyayana(pairings)

        self.assertIn("used more than once", str(context.exception))
