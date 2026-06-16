import numpy as np


def lu_decomposition(A):
    """Compute LU decomposition with partial pivoting.
    Returns P, L, U such that P @ A = L @ U.
    """
    A = A.astype(float).copy()
    n = A.shape[0]
    P = np.eye(n)
    L = np.zeros((n, n))
    U = A.copy()

    for k in range(n):
        pivot = np.argmax(np.abs(U[k:, k])) + k
        if abs(U[pivot, k]) < 1e-12:
            raise np.linalg.LinAlgError("Matrix is singular to working precision")

        if pivot != k:
            U[[k, pivot], :] = U[[pivot, k], :]
            P[[k, pivot], :] = P[[pivot, k], :]
            L[[k, pivot], :k] = L[[pivot, k], :k]

        L[k, k] = 1.0
        for i in range(k + 1, n):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] -= L[i, k] * U[k, k:]

    return P, L, U


def qr_factorization(A, mode="reduced"):
    """Compute QR factorization of A."""
    return np.linalg.qr(A, mode=mode)


def symmetric_eigendecomposition(A):
    """Compute eigenvalues and eigenvectors for a symmetric matrix."""
    if not np.allclose(A, A.T, atol=1e-10):
        raise ValueError("Matrix must be symmetric for this decomposition.")
    vals, vecs = np.linalg.eigh(A)
    return vals, vecs


def svd_decomposition(A):
    """Compute the singular value decomposition of A."""
    U, s, Vt = np.linalg.svd(A, full_matrices=False)
    return U, s, Vt


def pseudo_inverse(A):
    """Compute the Moore-Penrose pseudoinverse."""
    return np.linalg.pinv(A)


def solve_linear_system(A, b):
    """Solve Ax = b with least-squares fallback."""
    A = np.asarray(A)
    b = np.asarray(b)
    if A.shape[0] == A.shape[1]:
        return np.linalg.solve(A, b)
    return np.linalg.lstsq(A, b, rcond=None)[0]


def principal_components(X, n_components=None):
    """Compute principal components from data matrix X."""
    X_centered = X - np.mean(X, axis=0)
    cov = np.cov(X_centered, rowvar=False)
    values, vectors = symmetric_eigendecomposition(cov)
    ordering = np.argsort(values)[::-1]
    values = values[ordering]
    vectors = vectors[:, ordering]
    if n_components is not None:
        vectors = vectors[:, :n_components]
        values = values[:n_components]
    return values, vectors


def matrix_norms(A):
    """Compute several matrix norms."""
    return {
        "frobenius": np.linalg.norm(A, ord='fro'),
        "spectral": np.linalg.norm(A, ord=2),
        "one": np.linalg.norm(A, ord=1),
        "infinity": np.linalg.norm(A, ord=np.inf),
    }


def demonstrate():
    """Demonstrate advanced linear algebra concepts."""
    A = np.array([[4.0, 2.0, 0.0], [2.0, 4.0, 2.0], [0.0, 2.0, 4.0]])
    B = np.array([[1.0, 2.0, 3.0], [0.0, 1.0, 4.0], [5.0, 6.0, 0.0]])
    b = np.array([1.0, 2.0, 3.0])

    print("Matrix A:")
    print(A)
    print("\nSymmetric eigendecomposition of A:")
    eigvals, eigvecs = symmetric_eigendecomposition(A)
    print("Eigenvalues:", eigvals)
    print("Eigenvectors:\n", eigvecs)

    print("\nLU decomposition of B:")
    P, L, U = lu_decomposition(B)
    print("P:\n", P)
    print("L:\n", L)
    print("U:\n", U)
    print("Reconstructed B from P^T L U:\n", P.T @ L @ U)

    print("\nQR factorization of B:")
    Q, R = qr_factorization(B)
    print("Q:\n", Q)
    print("R:\n", R)

    print("\nSVD of B:")
    U_svd, s, Vt = svd_decomposition(B)
    print("Singular values:", s)
    print("U:\n", U_svd)
    print("V^T:\n", Vt)

    print("\nPseudoinverse of B:")
    B_pinv = pseudo_inverse(B)
    print(B_pinv)
    print("Check B B^+ B:\n", B @ B_pinv @ B)

    print("\nSolve B x = b:")
    x = solve_linear_system(B, b)
    print("x:", x)
    print("Residual norm:", np.linalg.norm(B @ x - b))

    data = np.array([
        [2.5, 2.4],
        [0.5, 0.7],
        [2.2, 2.9],
        [1.9, 2.2],
        [3.1, 3.0],
        [2.3, 2.7],
        [2.0, 1.6],
        [1.0, 1.1],
        [1.5, 1.6],
        [1.1, 0.9],
    ])
    print("\nPrincipal components of example data:")
    values, components = principal_components(data, n_components=2)
    print("Explained variances:", values)
    print("Principal component vectors:\n", components)

    print("\nMatrix norms of B:")
    print(matrix_norms(B))


if __name__ == "__main__":
    demonstrate()
