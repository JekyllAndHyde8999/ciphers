import string


class Matrix:
    def __init__(self, a: list) -> None:
        self.matrix = a

    def __matmul__(self, other):
        assert isinstance(other, self.__class__)
        # assert self.shape[1] == other.shape[0], "dim1({0}) != dim0({1})".format(
        #     self.shape[1], other.shape[0]
        # )  # checking dimensions
        product = [
            [0 for i in range(len(other.matrix[0]))] for j in range(len(self.matrix))
        ]

        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(other.matrix)):
                    product[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return Matrix(product)

    def __mod__(self, other):
        return Matrix([[ele % other for ele in row] for row in self.matrix])

    def flatten(self):
        return Matrix([ele for row in self.matrix for ele in row])


class Hill:
    def __init__(self, key: str) -> None:
        self.__letters = string.ascii_letters + string.digits
        self.__key = list(map(self.__letters.find, key))
        self.__key_shape = int(len(self.__key) ** 0.5)
        self.__key = Matrix(
            [
                self.__key[i * self.__key_shape : (i + 1) * self.__key_shape]
                for i in range(self.__key_shape)
            ]
        )

        print(*self.__key.matrix, sep="\n")

    def __preprocess(self, message: str) -> str:
        # insert X between duplicate letters
        wo_duplicates = []
        message = list(message)
        while message:
            curr_char = message.pop(0)
            if wo_duplicates and curr_char.isalnum() and curr_char == wo_duplicates[-1]:
                wo_duplicates.append("X")

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
        vector = Matrix(
            [[self.__letters.find(char)] for char in group if char in self.__letters]
        )
        new_letters = ((self.__key @ vector) % len(self.__letters)).flatten().matrix
        new_letters = [self.__letters[ind] for ind in new_letters]
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
            if curr_char in self.__letters:
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
            encoded_group = self.__encode_group(group)
            for char in group:
                if char.isalnum():
                    new_group += encoded_group.pop(0)
                else:
                    new_group += char
            out.append(new_group)

        return "".join(out)

    def decode(self, message: str) -> str:
        pass
