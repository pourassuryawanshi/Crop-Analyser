class Matrix:
    def _init_(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    @classmethod
    def from_list(cls, matrix_list):
        rows = len(matrix_list)
        cols = len(matrix_list[0])
        matrix = cls(rows, cols)
        matrix.data = matrix_list
        return matrix

    def _str_(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def _add_(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def _sub_(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def _mul_(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] * other
            return result
        elif isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result
        else:
            raise ValueError("Multiplication is only defined between two matrices or a matrix and a scalar.")

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result


# Example usage
matrix1 = Matrix.from_list([[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix.from_list([[7, 8], [9, 10], [11, 12]])

print("Matrix 1:")
print(matrix1)
print()

print("Matrix 2:")
print(matrix2)
print()

print("Matrix 1 + Matrix 2:")
print(matrix1 + matrix2)
print()

print("Matrix 1 - Matrix 2:")
print(matrix1 - matrix2)
print()

print("Matrix 1 * 2:")
print(matrix1 * 2)
print()

print("Matrix 1 * Matrix 2:")
print(matrix1 * matrix2)
print()

print("Transpose of Matrix 1:")
print(matrix1.transpose())