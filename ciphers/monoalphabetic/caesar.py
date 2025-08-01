from ..base import Cipher


class Caesar(Cipher):
    def __init__(self, shift: int):
        self.shift = shift
        super().__init__()

    def encode(self, message: str) -> str:
        message_wo_puncts, puncts = self.separate(message)
        out = []
        for char in message_wo_puncts:
            out.append(
                self.letters[(self.letters.find(char) + self.shift) % len(self.letters)]
            )

        for punct, index in puncts:
            out.insert(index, punct)

        return "".join(out)

    def decode(self, message: str) -> str:
        message_wo_puncts, puncts = self.separate(message)
        out = []
        for char in message_wo_puncts:
            out.append(
                self.letters[(self.letters.find(char) - self.shift) % len(self.letters)]
            )

        for punct, index in puncts:
            out.insert(index, punct)

        return "".join(out)
