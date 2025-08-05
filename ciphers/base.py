import string
from abc import ABC, abstractmethod


class Cipher(ABC):
    def __init__(self) -> None:
        self.letters = string.ascii_letters + string.digits

    def separate(self, message: str) -> tuple[list[str], list[tuple[str, int]]]:
        """
        Split message into alphanum characters and punctuation characters
        """
        message_wo_puncts = []
        puncts = []
        for i, char in enumerate(message):
            if char in self.letters:
                message_wo_puncts.append(char)
            else:
                puncts.append((char, i))

        return message_wo_puncts, puncts

    @abstractmethod
    def encode(self, message: str) -> str: ...

    @abstractmethod
    def decode(self, message: str) -> str: ...
