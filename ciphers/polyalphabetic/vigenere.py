import string


class Vigenere:
    def __init__(self, key: str) -> None:
        self.key = key
        self.__letters = string.ascii_letters + string.digits

    def encode(self, message: str) -> str:
        out = ""
        for i, char in enumerate(message):
            if char in self.__letters:
                delta = self.__letters.find(self.key[i % len(self.key)])
                out += self.__letters[
                    (self.__letters.find(char) + delta) % len(self.__letters)
                ]
            else:
                out += char

        return out
    
    def decode(self, message: str) -> str:
        out = ""
        for i, char in enumerate(message):
            if char in self.__letters:
                delta = self.__letters.find(self.key[i % len(self.key)])
                out += self.__letters[
                    (self.__letters.find(char) - delta) % len(self.__letters)
                ]
            else:
                out += char

        return out
