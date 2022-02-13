import numpy as np


class MatrixEasy:
    def __init__(self, data):
        self.data = data
        self.height = len(data)
        self.width = 0 if self.height == 0 else len(data[0])

    def __matmul__(self, other):
        if self.width != other.height:
            raise ArithmeticError("Matrix sizes do not match")
        result = [[None] * other.width] * self.height
        for i in range(self.height):
            for j in range(other.width):
                for k in range(other.height):
                    result[i][j] = self.data[i][k] * other.data[k][j]
        return MatrixEasy(result)

    def __mul__(self, other):
        if self.height != other.height or self.width != other.width:
            raise ArithmeticError("Matrix sizes do not match")
        result = [[None] * self.width] * self.height
        for h in range(self.height):
            for w in range(self.width):
                result[h][w] = self.data[h][w] * other.data[h][w]
        return MatrixEasy(result)

    def __add__(self, other):
        if self.height != other.height or self.width != other.width:
            raise ArithmeticError("Matrix sizes do not match")
        result = [[None] * self.width] * self.height
        for h in range(self.height):
            for w in range(self.width):
                result[h][w] = self.data[h][w] + other.data[h][w]
        return MatrixEasy(result)

    def __str__(self):
        result = ""
        for h in range(self.height):
            result += " ".join((map(str, self.data[h]))) + "\n"
        return result

class Matrix:
    def __matmul__(self):
        return

    def __mul__(self, other):
        return

    def __add__(self, other):
        return


def eval_op(m1, m2, op):
    with open("artifacts/easy/matrix" + (op if op != "*" else "ml") + ".txt", "w") as file:
        file.write(str(eval("m1 " + op + " m2")))
        file.close()


if __name__ == '__main__':
    m1 = MatrixEasy(np.random.randint(0, 10, (10, 10)))
    m2 = MatrixEasy(np.random.randint(0, 10, (10, 10)))
    eval_op(m1, m2, "+")
    eval_op(m1, m2, "*")
    eval_op(m1, m2, "@")
