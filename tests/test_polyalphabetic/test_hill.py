import unittest

from ciphers.base import Cipher
from ciphers.exceptions import InvalidKeyLength
from ciphers.polyalphabetic import Hill


class TestHillCipher(unittest.TestCase):
    def test_simple_string(self):
        """
        Testing encryption/decryption on message containing only alphabet
        """
        hill_cipher: Cipher = Hill("HILL")
        plain_text: str = "Hello"
        encrypted_text: str = "Vf3iuL"

        self.assertEqual(hill_cipher.encode(plain_text), encrypted_text)
        self.assertEqual(hill_cipher.decode(encrypted_text), plain_text)

    def test_error_raises(self):
        """
        Length of key must be perfect square
        """
        with self.assertRaises(InvalidKeyLength):
            Hill("LEY")
