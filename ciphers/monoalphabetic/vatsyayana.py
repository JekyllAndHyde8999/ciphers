from typing import List, Tuple

from ..base import Cipher


class Vatsyayana(Cipher):
    def __init__(self, pairings: List[Tuple]) -> None:
        reverse_pairings = {val: key for key, val in pairings}
        self.pairings = {**dict(pairings), **reverse_pairings}
        super().__init__()

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
