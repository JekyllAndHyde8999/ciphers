import string
from typing import List, Tuple


class Vatsyayana:
    def __init__(self, pairings: List[Tuple]) -> None:
        reverse_pairings = {val: key for key, val in pairings}
        self.pairings = {**dict(pairings), **reverse_pairings}

    def preprocess(self, message: str) -> str:
        message = message.replace(" ", "")
        message = message.translate(str.maketrans("", "", string.punctuation))
        return message

    def encode(self, message: str) -> str:
        out = "".join(
            [
                self.pairings[char] if char in self.pairings.keys() else char
                for char in message
            ]
        )

        return out

    def decode(self, message: str) -> str:
        out = "".join(
            [
                self.pairings[char] if char in self.pairings.keys() else char
                for char in message
            ]
        )

        return out
