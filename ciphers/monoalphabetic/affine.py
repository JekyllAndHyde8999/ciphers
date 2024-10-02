import math

from ..base import Cipher
from ..exceptions import InvalidParameter


class Affine(Cipher):
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
        super().__init__()

        if math.gcd(self.a, len(self.letters)) != 1:
            raise InvalidParameter(
                f"Parameter `a`({self.a}) must be co-prime with {len(self.letters)}"
            )

        for i in range(1, len(self.letters)):
            if (self.a * i) % len(self.letters) == 1:
                self.a_inv = i
                break

    def encode(self, message: str) -> str:
        message, puncts = self.separate(message)
        out = []
        for char in message:
            out.append(
                self.letters[
                    (self.a * self.letters.find(char) + self.b) % len(self.letters)
                ]
            )

        for punct, index in puncts:
            out.insert(index, punct)

        return "".join(out)

    def decode(self, message: str) -> str:
        message, puncts = self.separate(message)
        out = []
        for char in message:
            out.append(
                self.letters[
                    (self.a_inv * (self.letters.find(char) - self.b))
                    % len(self.letters)
                ]
            )

        for punct, index in puncts:
            out.insert(index, punct)

        return "".join(out)
