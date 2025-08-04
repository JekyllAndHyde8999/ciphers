import unittest

from ciphers.base import Cipher


class TestBaseCipher(unittest.TestCase):
    def test_error_raises(self):
        """
        Testing raising of 'NotImplementedError' of base class
        """
        cipher: Cipher = Cipher()
        plain_text: str = "Hello"

        with self.assertRaises(NotImplementedError):
            cipher.encode(plain_text)

        with self.assertRaises(NotImplementedError):
            cipher.decode(plain_text)

    def test_separate_chars(self):
        """
        Testing base class's method to separate
        punctuation marks from alhanum characters
        """

        cipher: Cipher = Cipher()
        plain_text: str = "Hello there!"

        expected_text_wo_puncts: list[str] = [
            "H",
            "e",
            "l",
            "l",
            "o",
            "t",
            "h",
            "e",
            "r",
            "e",
        ]
        expected_puncts: list[tuple[str, int]] = [(" ", 5), ("!", 11)]

        actual_text_wo_puncts, actual_puncts = cipher.separate(plain_text)

        self.assertEqual(expected_text_wo_puncts, actual_text_wo_puncts)
        self.assertEqual(expected_puncts, actual_puncts)
