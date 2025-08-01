from ..base import Cipher
from ..utils import ModMatrix


class Hill(Cipher):
    def __init__(self, key: str) -> None:
        super().__init__()
        self.__key_chars = list(map(self.letters.find, key))
        self.__key_shape = int(len(self.__key_chars) ** 0.5)
        self.__key = ModMatrix(
            [
                self.__key_chars[i * self.__key_shape : (i + 1) * self.__key_shape]
                for i in range(self.__key_shape)
            ],
            len(self.letters),
        )

        self.__inverted_key = self.__key.invert()

    def __padXs(self, message: str) -> str:
        """
        add X's to end of message string to make length a multiple of size of key
        """

        # count number of alphanum characters
        num_alphanum = sum([char.isalnum() for char in message])
        # add X to the end to align it to the key
        padding = (
            self.__key_shape - (num_alphanum % self.__key_shape)
        ) % self.__key_shape
        message = message + ("X" * padding)
        return message

    def __encode_group(self, group: str) -> list[str]:
        vector = ModMatrix(
            [[self.letters.find(char)] for char in group if char in self.letters],
            len(self.letters),
        )
        new_letters = ((self.__key @ vector) % len(self.letters)).flatten().matrix
        new_letters = [self.letters[ind] for ind in new_letters]
        return new_letters

    def __decode_group(self, group: str) -> list[str]:
        vector = ModMatrix(
            [[self.letters.find(char)] for char in group if char in self.letters],
            len(self.letters),
        )
        new_letters = (
            ((self.__inverted_key @ vector) % len(self.letters)).flatten().matrix
        )
        new_letters = [self.letters[ind] for ind in new_letters]
        return new_letters

    def encode(self, message: str) -> str:
        message_wo_puncts, puncts = self.separate(message)
        message_w_Xs = self.__padXs("".join(message_wo_puncts))
        out = []

        for group in [
            message_w_Xs[i : i + self.__key_shape]
            for i in range(0, len(message_w_Xs), self.__key_shape)
        ]:
            encoded_group = self.__encode_group(group)
            out.extend(encoded_group)

        for punct, index in puncts:
            out.insert(index, punct)

        return "".join(out)

    def decode(self, message: str) -> str:
        message_wo_puncts, puncts = self.separate(message)
        message_w_Xs = self.__padXs("".join(message_wo_puncts))
        out = []

        for group in [
            message_w_Xs[i : i + self.__key_shape]
            for i in range(0, len(message_w_Xs), self.__key_shape)
        ]:
            encoded_group = self.__decode_group(group)
            out.extend(encoded_group)

        for punct, index in puncts:
            out.insert(index, punct)
        out = "".join(out)
        return out
