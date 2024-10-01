from ..base import Cipher


class RailFence(Cipher):
    def __init__(self, fences: int) -> None:
        self.fences = fences
        super().__init__()

    def encode(self, message: str) -> str:
        out = []
        for i in range(self.fences):
            out.extend(message[i :: self.fences])
        return "".join(out)

    def decode(self, message: str) -> str:
        split_size = (len(message) // self.fences) + 1
        out = []
        for i in range(split_size):
            out.extend(message[i::split_size])
        return "".join(out)
