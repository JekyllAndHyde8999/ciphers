import json
import unittest
from pathlib import Path
from typing import Any

from ciphers.base import Cipher
from ciphers.exceptions import InvalidParameter
from ciphers.monoalphabetic import RailFence


class TestRailFenceCipher(unittest.TestCase):
    testcases_file: str = "railfence.json"

    @classmethod
    def setUpClass(cls) -> None:
        testcases_path: Path = (
            Path(__file__).parent.parent / "testcases" / cls.testcases_file
        )
        with open(testcases_path, mode="r") as f:
            cls.testcases = json.load(f)

    def test_encrypt_decrypt(self):
        """
        Testing encryption/decryption on plain text
        """

        curr_testcases: list[dict[str, Any]] = self.testcases[self._testMethodName]
        for case in curr_testcases:
            with self.subTest():
                plain_text: str = case["plain_text"]
                encrypted_text: str = case["encrypted_text"]
                cipher: Cipher = RailFence(**case["params"])

                self.assertEqual(encrypted_text, cipher.encode(plain_text))
                self.assertEqual(plain_text, cipher.decode(encrypted_text))

    def test_error_raises(self):
        """
        `fences` parameter being greater than length of message is unreasonable
        """
        curr_testcases: list[dict[str, Any]] = self.testcases[self._testMethodName]
        for case in curr_testcases:
            with self.subTest():
                with self.assertRaises(InvalidParameter):
                    plain_text: str = case["plain_text"]
                    railfence_cipher: Cipher = RailFence(**case["params"])
                    railfence_cipher.encode(plain_text)
