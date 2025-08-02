import unittest

from ciphers.base import Cipher
from ciphers.exceptions import InvalidPairings, InvalidParameter
from ciphers.monoalphabetic import Affine, Caesar, RailFence, Vatsyayana


class TestAffineCipher(unittest.TestCase):
    def test_simple_string(self):
        """
        Testing encryption/decryption on message containing only alphabet
        """

        affine_cipher: Cipher = Affine(5, 5)
        plain_text: str = "Hello"  # plain text message to encrypt
        encrypted_text: str = "Uz88n"

        self.assertEqual(affine_cipher.encode(plain_text), encrypted_text)
        self.assertEqual(affine_cipher.decode(encrypted_text), plain_text)

    def test_string_with_alphanum(self):
        """
        Testing encryption/decryption on message with alphanumeric characters
        """

        affine_cipher: Cipher = Affine(5, 5)
        plain_text: str = "Hello123"
        encrypted_text: str = "Uz88nwBG"

        self.assertEqual(affine_cipher.encode(plain_text), encrypted_text)
        self.assertEqual(affine_cipher.decode(encrypted_text), plain_text)

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

        caesar_cipher: Cipher = Caesar(3)
        plain_text: str = "Hello"
        encrypted_text: str = "Khoor"

        self.assertEqual(caesar_cipher.encode(plain_text), encrypted_text)
        self.assertEqual(caesar_cipher.decode(encrypted_text), plain_text)

    def test_string_with_alphanum(self):
        """
        Testing encryption/decryption on message with alphanumeric characters
        """

        caesar_cipher: Cipher = Caesar(3)
        plain_text: str = "Hello123"
        encrypted_text: str = "Khoor456"

        self.assertEqual(caesar_cipher.encode(plain_text), encrypted_text)
        self.assertEqual(caesar_cipher.decode(encrypted_text), plain_text)


class TestRailFenceCipher(unittest.TestCase):
    def test_simple_string(self):
        """
        Testing encryption/decryption on message containing only alphabet
        """

        railfence_cipher: Cipher = RailFence(2)
        plain_text: str = "Hello"
        encrypted_text: str = "Hloel"

        self.assertEqual(railfence_cipher.encode(plain_text), encrypted_text)
        self.assertEqual(railfence_cipher.decode(encrypted_text), plain_text)

    def test_string_with_alphanum(self):
        """
        Testing encryption/decryption on message with alphanumeric characters
        """

        railfence_cipher: Cipher = RailFence(3)
        plain_text: str = "Hello123"
        encrypted_text: str = "Hl2eo3l1"

        self.assertEqual(railfence_cipher.encode(plain_text), encrypted_text)
        self.assertEqual(railfence_cipher.decode(encrypted_text), plain_text)

    def test_error_raises(self):
        """
        `fences` parameter being greater than length of message is unreasonable
        """

        with self.assertRaises(InvalidParameter):
            railfence_cipher: Cipher = RailFence(5)
            plain_text: str = "Hello"
            railfence_cipher.encode(plain_text)


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
            ("g", "W"), # `W` repeated here
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
