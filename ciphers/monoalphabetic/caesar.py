import string


class Caesar:
    def __init__(self, shift: int):
        self.shift = shift
        self.__letters = string.ascii_letters + string.digits

    def preprocess(self, message: str) -> str:
        message = message.replace(" ", "")
        message = message.translate(str.maketrans("", "", string.punctuation))
        return message

    def encode(self, message: str) -> str:
        out = "".join(
            [
                (
                    self.__letters[
                        (self.__letters.find(char) + self.shift) % len(self.__letters)
                    ]
                    if char in self.__letters
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
                    self.__letters[
                        (self.__letters.find(char) - self.shift) % len(self.__letters)
                    ]
                    if char in self.__letters
                    else char
                )
                for char in message
            ]
        )

        return out
