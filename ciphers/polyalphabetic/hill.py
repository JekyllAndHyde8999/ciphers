import math

from ..base import Cipher


class InvalidDeterminant(ValueError):
    pass


class ModMatrix:
    def __init__(self, a: list, modulus: int) -> None:
        self.matrix = a
        self.modulus = modulus

    def __matmul__(self, other):
        assert isinstance(other, self.__class__)

        product = [
            [0 for i in range(len(other.matrix[0]))] for j in range(len(self.matrix))
        ]

        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(other.matrix)):
                    product[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return ModMatrix(product, self.modulus)

    def __rmul__(self, other):
        return ModMatrix(
            [[ele * other for ele in row] for row in self.matrix], self.modulus
        )

    def __mod__(self, other):
        return ModMatrix(
            [[ele % other for ele in row] for row in self.matrix], self.modulus
        )

    def flatten(self):
        return ModMatrix([ele for row in self.matrix for ele in row], self.modulus)

    def __get_matrix_minor(self, matrix, i, j):
        return [row[:j] + row[j + 1 :] for row in (matrix[:i] + matrix[i + 1 :])]

    def __get_determinant(self, matrix):
        if len(matrix) == 1:
            return matrix[0][0]

        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        determinant = 0
        for c in range(len(matrix)):
            determinant += (
                ((-1) ** c)
                * matrix[0][c]
                * self.__get_determinant(self.__get_matrix_minor(matrix, 0, c))
            )
        return determinant

    def __invert_det(self, det):
        if det == 0:
            raise InvalidDeterminant("Determinant of matrix is 0.")

        det %= self.modulus

        if math.gcd(det, self.modulus) != 1:
            raise InvalidDeterminant(
                f"Determinant {det} is not co-prime with modulus {self.modulus}"
            )

        for i in range(1, self.modulus):
            if (det * i) % self.modulus == 1:
                return i

    def invert(self):
        """Function to calculate the inverse of a matrix"""
        inverse_determinant = self.__invert_det(self.__get_determinant(self.matrix))

        # Find matrix of cofactors
        cofactors = []
        for r in range(len(self.matrix)):
            cofactor_row = []
            for c in range(len(self.matrix)):
                minor = self.__get_matrix_minor(self.matrix, r, c)
                cofactor_row.append(((-1) ** (r + c)) * self.__get_determinant(minor))
            cofactors.append(cofactor_row)

        # Transpose matrix of cofactors
        cofactors = list(map(list, zip(*cofactors)))

        return (inverse_determinant * ModMatrix(cofactors, self.modulus)) % self.modulus


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
        # insert X between duplicate letters
        wo_duplicates = []
        message = list(message)
        while message:
            curr_char = message.pop(0)
            wo_duplicates.append(curr_char)

        message = "".join(wo_duplicates)

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
