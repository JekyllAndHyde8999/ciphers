import math
import string


class InvalidParameter(ValueError):
    pass


class Affine:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
        self.__letters = string.ascii_letters + string.digits

        if math.gcd(self.a, len(self.__letters)) != 1:
            raise InvalidParameter(
                f"Parameter `a`({self.a}) must be co-prime with {len(self.__letters)}"
            )

        for i in range(1, len(self.__letters)):
            if (self.a * i) % len(self.__letters) == 1:
                self.a_inv = i
                break

    def encode(self, message: str) -> str:
        out = ""
        for char in message:
            if char in self.__letters:
                out += self.__letters[
                    (self.a * self.__letters.find(char) + self.b) % len(self.__letters)
                ]
            else:
                out += char

        return out

    def decode(self, message: str) -> str:
        out = ""
        for char in message:
            if char in self.__letters:
                out += self.__letters[
                    (self.a_inv * (self.__letters.find(char) - self.b))
                    % len(self.__letters)
                ]
            else:
                out += char

        return out
