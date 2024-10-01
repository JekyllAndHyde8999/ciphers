from ..base import Cipher


class Caesar(Cipher):
    def __init__(self, shift: int):
        self.shift = shift
        super().__init__()

    def encode(self, message: str) -> str:
        out = "".join(
            [
                (
                    self.letters[
                        (self.letters.find(char) + self.shift) % len(self.letters)
                    ]
                    if char in self.letters
                    else char
                )
                for char in message
            ]
        )

        return out

    def decode(self, message: str) -> str:
        out = "".join(
            [
                (
                    self.letters[
                        (self.letters.find(char) - self.shift) % len(self.letters)
                    ]
                    if char in self.letters
                    else char
                )
                for char in message
            ]
        )

        return out
