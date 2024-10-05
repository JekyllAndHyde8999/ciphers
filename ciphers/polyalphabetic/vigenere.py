from ..base import Cipher


class Vigenere(Cipher):
    def __init__(self, key: str) -> None:
        self.key = key
        super().__init__()

    def encode(self, message: str) -> str:
        message, puncts = self.separate(message)
        out = []
        for i, char in enumerate(message):
            delta = self.letters.find(self.key[i % len(self.key)])
            out.append(
                self.letters[(self.letters.find(char) + delta) % len(self.letters)]
            )

        for punct, index in puncts:
            out.insert(index, punct)

        return "".join(out)

    def decode(self, message: str) -> str:
        message, puncts = self.separate(message)
        out = []
        for i, char in enumerate(message):
            delta = self.letters.find(self.key[i % len(self.key)])
            out.append(
                self.letters[(self.letters.find(char) - delta) % len(self.letters)]
            )

        for punct, index in puncts:
            out.insert(index, punct)

        return "".join(out)
