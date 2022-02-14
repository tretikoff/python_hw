import numpy as np


class MatrixHashMixin:
    def __hash__(self):
        pass


class MatrixStrMixin:
    def __init__(self, value):
        self.value = value

    def write_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(str(self))
            file.close()

    def __getattr__(self, item):
        if item == 'height':
            return len(self.value)
        if item == 'width':
            return 0 if self.height == 0 else len(self.value[0])
        raise NotImplementedError

    def __str__(self):
        result = ""
        for h in range(self.height):
            result += " ".join((map(str, self.value[h]))) + "\n"
        return result


class MatrixEasy(MatrixHashMixin, MatrixStrMixin):
    def __matmul__(self, other):
        if self.width != other.height:
            raise ArithmeticError("Matrix sizes do not match")
        result = [[None] * other.width] * self.height
        for i in range(self.height):
            for j in range(other.width):
                for k in range(other.height):
                    result[i][j] = self.value[i][k] * other.value[k][j]
        return MatrixEasy(result)

    def __mul__(self, other):
        if self.height != other.height or self.width != other.width:
            raise ArithmeticError("Matrix sizes do not match")
        result = [[None] * self.width] * self.height
        for h in range(self.height):
            for w in range(self.width):
                result[h][w] = self.value[h][w] * other.value[h][w]
        return MatrixEasy(result)

    def __add__(self, other):
        if self.height != other.height or self.width != other.width:
            raise ArithmeticError("Matrix sizes do not match")
        result = [[None] * self.width] * self.height
        for h in range(self.height):
            for w in range(self.width):
                result[h][w] = self.value[h][w] + other.value[h][w]
        return MatrixEasy(result)


class Matrix(MatrixStrMixin, np.lib.mixins.NDArrayOperatorsMixin):
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        return self.value



def run_easy():
    m1 = MatrixEasy(np.random.randint(0, 10, (10, 10)))
    m2 = MatrixEasy(np.random.randint(0, 10, (10, 10)))
    eval("m1 + m2").write_to_file("artifacts/easy/matrix+.txt")
    eval("m1 @ m2").write_to_file("artifacts/easy/matrix@.txt")
    eval("m1 * m2").write_to_file("artifacts/easy/matrix_mul.txt")


def run_medium():
    m1 = Matrix(np.random.randint(0, 10, (10, 10)))
    m2 = Matrix(np.random.randint(0, 10, (10, 10)))
    Matrix(eval("m1 + m2")).write_to_file("artifacts/medium/matrix+.txt")
    Matrix(eval("m1 @ m2")).write_to_file("artifacts/medium/matrix@.txt")
    Matrix(eval("m1 * m2")).write_to_file("artifacts/medium/matrix_mul.txt")


if __name__ == '__main__':
    run_easy()
    run_medium()
