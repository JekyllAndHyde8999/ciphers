import string


class Playfair:
    def __init__(self, passphrase: str) -> None:
        self.__letters = (string.ascii_letters + string.digits).translate(
            str.maketrans("", "", "jJ")
        )
        self.__passphrase = passphrase.replace("j", "i").replace("J", "I")

        self.__grid = []
        for char in self.__passphrase:
            if char not in self.__grid:
                self.__grid.append(char)

        for char in self.__letters:
            if char not in self.__grid:
                self.__grid.append(char)

        self.__grid = [self.__grid[i : i + 10] for i in range(0, len(self.__grid), 10)]
        self.__grid_shape = (len(self.__grid), len(self.__grid[0]))

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
        # add x to the end to make it even
        message = message.replace("j", "i").replace("J", "I")
        message = message + "X" if num_alphanum % 2 else message
        return message

    def __find_char(self, char: str) -> tuple[int, int]:
        for row_index, row in enumerate(self.__grid):
            for col_index, element in enumerate(row):
                if element == char:
                    return (row_index, col_index)

    def __get_char(self, coords: tuple[int, int]) -> str:
        return self.__grid[coords[0]][coords[1]]

    def __get_new_indices(
        self, index1: tuple[int, int], index2: tuple[int, int], decode: bool = False
    ) -> tuple[tuple[int, int]]:
        delta = -1 if decode else 1

        # same row
        if index1[0] == index2[0]:
            n_index1 = (index1[0], (index1[1] + delta) % self.__grid_shape[1])
            n_index2 = (index2[0], (index2[1] + delta) % self.__grid_shape[1])
            return n_index1, n_index2

        # same column
        if index1[1] == index2[1]:
            n_index1 = ((index1[0] + delta) % self.__grid_shape[0], index1[1])
            n_index2 = ((index2[0] + delta) % self.__grid_shape[0], index2[1])
            return n_index1, n_index2

        # rectangle
        n_index1 = (index1[0], index2[1])
        n_index2 = (index2[0], index1[1])
        return n_index1, n_index2

    def encode(self, message: str) -> str:
        message = self.__preprocess(message)
        message_parts = []
        out = []

        # take 2 alphanum chars at a time and find indices
        count = 0
        part = ""
        while message:
            curr_char = message[0]
            part += curr_char
            if curr_char in self.__letters:
                count += 1

            if count == 2:
                message_parts.append(part)
                count = 0
                part = ""

            message = message[1:]

        if part:
            message_parts.append(part)

        print(message_parts)

        for pair in message_parts:
            alnum = tuple(filter(lambda x: x.isalnum(), pair))
            indices = tuple(map(self.__find_char, alnum))
            if not indices:
                out.append(pair)
                continue

            new_indices = self.__get_new_indices(*indices)
            new_chars = tuple(map(self.__get_char, new_indices))
            
            out.append(pair.translate(dict(zip(map(ord, alnum), map(ord, new_chars)))))
        
        return "".join(out)
    
    def decode(self, message: str) -> str:
        message_parts = []
        out = []

        # take 2 alphanum chars at a time and find indices
        count = 0
        part = ""
        while message:
            curr_char = message[0]
            part += curr_char
            if curr_char in self.__letters:
                count += 1

            if count == 2:
                message_parts.append(part)
                count = 0
                part = ""

            message = message[1:]

        if part:
            message_parts.append(part)

        for pair in message_parts:
            alnum = tuple(filter(lambda x: x.isalnum(), pair))
            indices = tuple(map(self.__find_char, alnum))
            if not indices:
                out.append(pair)
                continue

            new_indices = self.__get_new_indices(*indices, decode=True)
            new_chars = tuple(map(self.__get_char, new_indices))
            
            out.append(pair.translate(dict(zip(map(ord, alnum), map(ord, new_chars)))))
        
        return "".join(out)
