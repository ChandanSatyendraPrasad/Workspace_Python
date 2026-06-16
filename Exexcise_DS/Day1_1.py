def matrix_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matrix_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matrix_mul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def scalar_mul(A, scalar):
    return [[scalar * value for value in row] for row in A]


def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def determinant_3x3(A):
    return (
        A[0][0] * A[1][1] * A[2][2]
        + A[0][1] * A[1][2] * A[2][0]
        + A[0][2] * A[1][0] * A[2][1]
        - A[0][2] * A[1][1] * A[2][0]
        - A[0][0] * A[1][2] * A[2][1]
        - A[0][1] * A[1][0] * A[2][2]
    )


def minor_2x2(A, i, j):
    rows = [r for r in range(3) if r != i]
    cols = [c for c in range(3) if c != j]
    return A[rows[0]][cols[0]] * A[rows[1]][cols[1]] - A[rows[0]][cols[1]] * A[rows[1]][cols[0]]


def inverse_3x3(A):
    det = determinant_3x3(A)
    if det == 0:
        raise ValueError("Matrix is not invertible")
    cofactor = [
        [(((-1) ** (i + j)) * minor_2x2(A, i, j)) for j in range(3)]
        for i in range(3)
    ]
    adjugate = transpose(cofactor)
    return [[adjugate[i][j] / det for j in range(3)] for i in range(3)]


def print_matrix(label, A):
    print(f"{label}")
    for row in A:
        print(row)
    print()


if __name__ == "__main__":
    matrix_a = [[1, 2, 3], [0, 4, 5], [1, 0, 6]]
    matrix_b = [[7, 8, 9], [1, 2, 3], [4, 5, 6]]

    print_matrix("Matrix A:", matrix_a)
    print_matrix("Matrix B:", matrix_b)

    print_matrix("A + B:", matrix_add(matrix_a, matrix_b))
    print_matrix("A - B:", matrix_sub(matrix_a, matrix_b))
    print_matrix("A * B:", matrix_mul(matrix_a, matrix_b))
    print_matrix("2 * A:", scalar_mul(matrix_a, 2))
    print_matrix("Transpose of A:", transpose(matrix_a))

    det_a = determinant_3x3(matrix_a)
    print(f"Determinant of A: {det_a}\n")

    inverse_a = inverse_3x3(matrix_a)
    print_matrix("Inverse of A:", inverse_a)
