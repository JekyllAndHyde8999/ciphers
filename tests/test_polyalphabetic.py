import unittest

from ciphers.base import Cipher
from ciphers.polyalphabetic import AutoKey, Vigenere


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


class TestVigenereCipher(unittest.TestCase):
    def test_simple_string(self):
        """
        Testing encryption/decryption on message containing only alphabet
        """

        vigenere_cipher: Cipher = Vigenere("KEY")
        plain_text: str = "Hello"
        encrypted_text: str = "hI9VS"

        self.assertEqual(vigenere_cipher.encode(plain_text), encrypted_text)
        self.assertEqual(vigenere_cipher.decode(encrypted_text), plain_text)

    def test_string_with_alphanum(self):
        """
        Testing encryption/decryption on message with alphanumeric characters
        """

        vigenere_cipher: Cipher = Vigenere("KEY")
        plain_text: str = "Hello123"
        encrypted_text: str = "hI9VSPCx"

        self.assertEqual(vigenere_cipher.encode(plain_text), encrypted_text)
        self.assertEqual(vigenere_cipher.decode(encrypted_text), plain_text)
