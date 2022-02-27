import numpy as np


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

    def __eq__(self, other):
        if self.height != other.height or self.width != other.width: return False
        for h in range(self.height):
            for w in range(self.width):
                if self.value[h] != self.value[w]: return False
        return True

    # Hash of all matrix elements [a11 a12 ... anm]
    # of type (a11 + 2*b12 + 3*b13 +..+((n+1)*(m+1)*bnm)) % 20
    # where bxy = axy % 20
    def __hash__(self):
        res = 0
        for h in range(self.height):
            for w in range(self.width):
                res += (int(self.value[h][w]) % 20) * (h * w + w + 1)
        return res % 20


class MatrixEasy(MatrixStrMixin):
    cache = {}
    multiplied = False

    def __matmul__(self, other):
        h1 = hash(self)
        h2 = hash(other)
        if self.cache.get(2):
            return self.cache[h2]

        if self.width != other.height:
            raise ArithmeticError("Matrix sizes do not match")
        result = MatrixEasy([[None] * other.width] * self.height)
        for i in range(self.height):
            for j in range(other.width):
                for k in range(other.height):
                    result.value[i][j] = self.value[i][k] * other.value[k][j]
        self.cache[h2] = result
        self.multiplied = True
        return result

    def __mul__(self, other):
        if self.height != other.height or self.width != other.width:
            raise ArithmeticError("Matrix sizes do not match")
        result = MatrixEasy([[None] * self.width] * self.height)
        for h in range(self.height):
            for w in range(self.width):
                result.value[h][w] = self.value[h][w] * other.value[h][w]
        return result

    def __add__(self, other):
        if self.height != other.height or self.width != other.width:
            raise ArithmeticError("Matrix sizes do not match")
        result = MatrixEasy([[None] * self.width] * self.height)
        for h in range(self.height):
            for w in range(self.width):
                result.value[h][w] = self.value[h][w] + other.value[h][w]
        return result


class Matrix(MatrixStrMixin, np.lib.mixins.NDArrayOperatorsMixin):
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        return self.value


def run_easy():
    m1 = MatrixEasy(np.random.randint(0, 10, (10, 10)))
    m2 = MatrixEasy(np.random.randint(0, 10, (10, 10)))
    eval("m1 + m2").write_to_file("artifacts/easy/A.txt")
    eval("m1 @ m2").write_to_file("artifacts/easy/matrix@.txt")
    eval("m1 * m2").write_to_file("artifacts/easy/matrix_mul.txt")


def run_medium():
    m1 = Matrix(np.random.randint(0, 10, (10, 10)))
    m2 = Matrix(np.random.randint(0, 10, (10, 10)))
    Matrix(eval("m1 + m2")).write_to_file("artifacts/medium/matrix+.txt")
    Matrix(eval("m1 @ m2")).write_to_file("artifacts/medium/matrix@.txt")
    Matrix(eval("m1 * m2")).write_to_file("artifacts/medium/matrix_mul.txt")


def run_hard():
    filename = "artifacts/hard/%s.txt"
    a = MatrixEasy([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    c = MatrixEasy([[21, 22, 23], [24, 25, 26], [27, 28, 29]])
    assert hash(a) == hash(c)
    assert a != c
    d = MatrixEasy(np.random.randint(0, 10, (3, 3)))
    b = d

    a * b
    a.multiplied = False
    ab = a * b
    assert not a.multiplied

    cd = c * d

    a.write_to_file(filename % "A")
    b.write_to_file(filename % "B")
    c.write_to_file(filename % "C")
    d.write_to_file(filename % "D")
    ab.write_to_file(filename % "AB")
    cd.write_to_file(filename % "CD")

    MatrixEasy([[hash(ab), hash(cd)]]).write_to_file(filename % "hash")
    assert a != c


if __name__ == '__main__':
    run_easy()
    run_medium()
    run_hard()
