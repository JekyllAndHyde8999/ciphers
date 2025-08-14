import json
import unittest
from pathlib import Path
from typing import Any

from ciphers.base import Cipher
from ciphers.polyalphabetic import Trithemius


class TestVigenereCipher(unittest.TestCase):
    testcases_file: str = "trithemius.json"

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
                cipher: Cipher = Trithemius()

                self.assertEqual(encrypted_text, cipher.encode(plain_text))
                self.assertEqual(plain_text, cipher.decode(encrypted_text))
