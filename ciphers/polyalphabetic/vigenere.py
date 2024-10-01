from ..base import Cipher


class Vigenere(Cipher):
    def __init__(self, key: str) -> None:
        self.key = key
        super().__init__()

    def encode(self, message: str) -> str:
        out = ""
        for i, char in enumerate(message):
            if char in self.letters:
                delta = self.letters.find(self.key[i % len(self.key)])
                out += self.letters[
                    (self.letters.find(char) + delta) % len(self.letters)
                ]
            else:
                out += char

        return out

    def decode(self, message: str) -> str:
        out = ""
        for i, char in enumerate(message):
            if char in self.letters:
                delta = self.letters.find(self.key[i % len(self.key)])
                out += self.letters[
                    (self.letters.find(char) - delta) % len(self.letters)
                ]
            else:
                out += char

        return out
