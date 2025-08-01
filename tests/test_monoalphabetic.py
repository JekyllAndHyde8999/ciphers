import unittest

from ciphers.exceptions import InvalidParameter
from ciphers.monoalphabetic import Affine, Caesar, RailFence, Vatsyayana


class TestAffineCipher(unittest.TestCase):
    def test_simple_string(self):
        """
        Testing encryption/decryption on message containing only alphabet
        """

        affine_cipher: Affine = Affine(5, 5)
        message: str = "Hello"

        self.assertEqual(affine_cipher.encode(message), "Uz88n")
        self.assertEqual(affine_cipher.decode("Uz88n"), message)

    def test_error_raises(self):
        """
        `a` parameter must be co-prime with vocabulary size (currently 62)
        """

        with self.assertRaises(InvalidParameter):
            Affine(4, 10)


class TestCaesarCipher(unittest.TestCase):
    def test_simple_string(self):
        """
        Testing encryption/decryption on message containing only alphabet
        """

        caesar_cipher: Caesar = Caesar(3)
        message: str = "Hello"

        self.assertEqual(caesar_cipher.encode(message), "Khoor")
        self.assertEqual(caesar_cipher.decode("Khoor"), message)


class TestRailFenceCipher(unittest.TestCase):
    def test_simple_string(self):
        """
        Testing encryption/decryption on message containing only alphabet
        """

        railfence_cipher: RailFence = RailFence(2)
        message: str = "Hello"

        self.assertEqual(railfence_cipher.encode(message), "Hloel")

    def test_error_raises(self):
        """
        `fences` parameter being greater than length of message is unreasonable
        """

        with self.assertRaises(InvalidParameter):
            railfence_cipher: RailFence = RailFence(5)
            message: str = "Hello"
            railfence_cipher.encode(message)


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

        vatsyayana_cipher: Vatsyayana = Vatsyayana(pairings)
        message: str = "Hello"

        self.assertEqual(vatsyayana_cipher.encode(message), "K2EEB")
