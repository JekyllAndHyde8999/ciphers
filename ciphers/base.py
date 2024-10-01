import string


class Cipher:
    def __init__(self) -> None:
        self.letters = string.ascii_letters + string.digits

    def encode(self, message: str = None) -> str:
        raise NotImplementedError("Method `encode` is not implemented")

    def decode(self, message: str = None) -> str:
        raise NotImplementedError("Method `decode` is not implemented")
