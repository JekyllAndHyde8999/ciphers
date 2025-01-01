from ..base import Cipher


class AutoKey(Cipher):
    def __init__(self, key: str) -> None:
        super().__init__()
        self.key = key

    def encode(self, message: str) -> str:
        message, puncts = self.separate(message)
        out = []

        for char, delta_char in zip(message, list(self.key) + message):
            delta = self.letters.find(delta_char)
            out.append(
                self.letters[(self.letters.find(char) + delta) % len(self.letters)]
            )

        for punct, index in puncts:
            out.insert(index, punct)

        return "".join(out)

    def decode(self, message: str) -> str:
        message, puncts = self.separate(message)
        out = []
        key = self.key

        for i, char in enumerate(message):
            delta = self.letters.find(key[i])
            newchar = self.letters[
                (self.letters.find(char) - delta) % len(self.letters)
            ]
            key += newchar
            out.append(newchar)

        for punct, index in puncts:
            out.insert(index, punct)

        return "".join(out)
