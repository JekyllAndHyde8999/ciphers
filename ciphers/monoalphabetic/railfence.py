import math

from ..base import Cipher
from ..exceptions import InvalidParameter


class RailFence(Cipher):
    def __init__(self, fences: int) -> None:
        self.fences = fences
        super().__init__()

    def encode(self, message: str) -> str:
        message_wo_puncts, puncts = self.separate(message)
        if self.fences >= len(message_wo_puncts):
            raise InvalidParameter(
                f"fences ({self.fences}) must be less than length of message for effective encryption"
            )
        out = []

        for i in range(self.fences):
            out.extend(message_wo_puncts[i :: self.fences])

        for punct, index in puncts:
            out.insert(index, punct)

        return "".join(out)

    def decode(self, message: str) -> str:
        message_wo_puncts, puncts = self.separate(message)
        split_size = math.ceil(len(message_wo_puncts) / self.fences)
        out = []
        for i in range(split_size):
            out.extend(message_wo_puncts[i::split_size])

        for punct, index in puncts:
            out.insert(index, punct)

        return "".join(out)
