import unittest

from ciphers.base import Cipher
from ciphers.exceptions import InvalidParameter
from ciphers.monoalphabetic import RailFence


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
