from ..base import Cipher
from ..utils import ModMatrix


class Hill(Cipher):
    def __init__(self, key: str) -> None:
        super().__init__()
        self.__key = list(map(self.letters.find, key))
        self.__key_shape = int(len(self.__key) ** 0.5)
        self.__key = ModMatrix(
            [
                self.__key[i * self.__key_shape : (i + 1) * self.__key_shape]
                for i in range(self.__key_shape)
            ],
            len(self.letters),
        )

        self.__inverted_key = self.__key.invert()

    def __preprocess(self, message: str) -> str:
        # count number of alphanum characters
        num_alphanum = sum([char.isalnum() for char in message])
        # add X to the end to align it to the key
        padding = (
            self.__key_shape - (num_alphanum % self.__key_shape)
        ) % self.__key_shape
        message = message + ("X" * padding)
        return message

    def __encode_group(self, group: str) -> str:
        vector = ModMatrix(
            [[self.letters.find(char)] for char in group if char in self.letters],
            len(self.letters),
        )
        new_letters = ((self.__key @ vector) % len(self.letters)).flatten().matrix
        new_letters = [self.letters[ind] for ind in new_letters]
        return new_letters

    def __decode_group(self, group: str) -> str:
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
        message = self.__preprocess(message)
        message_parts = []
        out = []

        # take `key` alphanum chars at a time and find indices
        count = 0
        part = ""
        while message:
            curr_char = message[0]
            part += curr_char
            if curr_char in self.letters:
                count += 1

            if count == self.__key_shape:
                message_parts.append(part)
                count = 0
                part = ""

            message = message[1:]

        if part:
            message_parts.append(part)

        for group in message_parts:
            new_group = ""
            encoded_group = (
                self.__encode_group(group)
                if any(map(lambda x: x.isalnum(), group))
                else group
            )
            for char in group:
                if char.isalnum():
                    new_group += encoded_group.pop(0)
                else:
                    new_group += char
            out.append(new_group)

        return "".join(out)

    def decode(self, message: str) -> str:
        message_parts = []
        out = []

        # take `key` alphanum chars at a time and find indices
        count = 0
        part = ""
        while message:
            curr_char = message[0]
            part += curr_char
            if curr_char in self.letters:
                count += 1

            if count == self.__key_shape:
                message_parts.append(part)
                count = 0
                part = ""

            message = message[1:]

        if part:
            message_parts.append(part)

        for group in message_parts:
            new_group = ""
            encoded_group = (
                self.__decode_group(group)
                if any(map(lambda x: x.isalnum(), group))
                else group
            )
            for char in group:
                if char.isalnum():
                    new_group += encoded_group.pop(0)
                else:
                    new_group += char
            out.append(new_group)

        return "".join(out)
