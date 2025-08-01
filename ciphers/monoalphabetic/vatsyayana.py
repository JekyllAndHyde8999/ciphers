from typing import Sequence

from ..base import Cipher


class Vatsyayana(Cipher):
    def __init__(self, pairings: Sequence[tuple[str, str]]) -> None:
        reverse_pairings = {val: key for key, val in pairings}
        self.pairings = {**dict(pairings), **reverse_pairings}
        super().__init__()

    def encode(self, message: str) -> str:
        message_wo_puncts, puncts = self.separate(message)
        out = []

        for char in message_wo_puncts:
            out.append(self.pairings[char])

        for punct, index in puncts:
            out.insert(index, punct)

        return "".join(out)

    def decode(self, message: str) -> str:
        message_wo_puncts, puncts = self.separate(message)
        out = []

        for char in message_wo_puncts:
            out.append(self.pairings[char])

        for punct, index in puncts:
            out.insert(index, punct)

        return "".join(out)
