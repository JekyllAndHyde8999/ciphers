import unittest

from ciphers.base import Cipher
from ciphers.exceptions import InvalidParameter
from ciphers.monoalphabetic import Affine


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
