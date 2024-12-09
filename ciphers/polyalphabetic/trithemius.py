from ..base import Cipher


class Trithemius(Cipher):
    def encode(self, message: str) -> str:
        message, puncts = self.separate(message)
        out = []
        for idx, char in enumerate(message):
            out.append(
                self.letters[(self.letters.find(char) + idx) % len(self.letters)]
            )

        for punct, index in puncts:
            out.insert(index, punct)
        out = "".join(out)
        return out

    def decode(self, message: str) -> str:
        message, puncts = self.separate(message)
        out = []
        for idx, char in enumerate(message):
            out.append(
                self.letters[(self.letters.find(char) - idx) % len(self.letters)]
            )

        for punct, index in puncts:
            out.insert(index, punct)
        out = "".join(out)
        return out
