import string


class Cipher:
    def __init__(self) -> None:
        self.letters = string.ascii_letters + string.digits

    def separate(self, message: str) -> tuple[list[str], list[tuple[str, int]]]:
        message_wo_puncts = []
        puncts = []
        for i, char in enumerate(message):
            if char in self.letters:
                message_wo_puncts.append(char)
            else:
                puncts.append((char, i))

        return message_wo_puncts, puncts

    def encode(self, message: str = None) -> str:
        raise NotImplementedError("Method `encode` is not implemented")

    def decode(self, message: str = None) -> str:
        raise NotImplementedError("Method `decode` is not implemented")
