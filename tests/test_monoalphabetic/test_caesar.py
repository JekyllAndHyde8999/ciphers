import unittest

from ciphers.base import Cipher
from ciphers.monoalphabetic import Caesar


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
