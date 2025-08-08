import unittest

from ciphers.base import Cipher
from ciphers.polyalphabetic import AutoKey


class TestAutoKeyCipher(unittest.TestCase):
    def test_simple_string(self):
        """
        Testing encryption/decryption on message containing only alphabet
        """

        autokey_cipher: Cipher = AutoKey("KEY")
        plain_text: str = "Hello"
        encrypted_text: str = "hI9Ss"

        self.assertEqual(autokey_cipher.encode(plain_text), encrypted_text)
        self.assertEqual(autokey_cipher.decode(encrypted_text), plain_text)
