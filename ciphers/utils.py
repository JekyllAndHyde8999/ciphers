import math

from .exceptions import InvalidDeterminant


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
