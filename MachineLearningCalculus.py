import numpy as np
from typing import Callable, Sequence


def derivative(f: Callable[[float], float], x: float, h: float = 1e-6) -> float:
    """Compute the derivative of a scalar function at x using central difference."""
    return (f(x + h) - f(x - h)) / (2 * h)


def gradient(f: Callable[[np.ndarray], float], x: np.ndarray, h: float = 1e-6) -> np.ndarray:
    """Compute the gradient of a scalar-valued function f at point x."""
    x = np.asarray(x, dtype=float)
    grad = np.zeros_like(x)
    for i in range(x.size):
        dx = np.zeros_like(x)
        dx[i] = h
        grad[i] = (f(x + dx) - f(x - dx)) / (2 * h)
    return grad


def hessian(f: Callable[[np.ndarray], float], x: np.ndarray, h: float = 1e-4) -> np.ndarray:
    """Compute the Hessian matrix of a scalar-valued function f at point x."""
    x = np.asarray(x, dtype=float)
    n = x.size
    H = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(i, n):
            dx_i = np.zeros_like(x)
            dx_j = np.zeros_like(x)
            dx_i[i] = h
            dx_j[j] = h
            if i == j:
                H[i, i] = (f(x + dx_i) - 2 * f(x) + f(x - dx_i)) / (h * h)
            else:
                f_pp = f(x + dx_i + dx_j)
                f_pm = f(x + dx_i - dx_j)
                f_mp = f(x - dx_i + dx_j)
                f_mm = f(x - dx_i - dx_j)
                H[i, j] = (f_pp - f_pm - f_mp + f_mm) / (4 * h * h)
                H[j, i] = H[i, j]
    return H


def mean_squared_error(y_true: Sequence[float], y_pred: Sequence[float]) -> float:
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    return float(np.mean((y_true - y_pred) ** 2))


def gradient_descent(
    grad_f: Callable[[np.ndarray], np.ndarray],
    x0: Sequence[float],
    lr: float = 0.01,
    steps: int = 1000,
) -> np.ndarray:
    """Simple gradient descent optimizer for a vector-valued parameter x."""
    x = np.asarray(x0, dtype=float)
    for _ in range(steps):
        x = x - lr * grad_f(x)
    return x


if __name__ == "__main__":
    def sample_loss(params: np.ndarray) -> float:
        return (params[0] - 2) ** 2 + 3 * (params[1] + 1) ** 2

    x0 = np.array([0.0, 0.0])
    grad_val = gradient(sample_loss, x0)
    hess_val = hessian(sample_loss, x0)

    print("Gradient at", x0, "=", grad_val)
    print("Hessian at", x0, "=\n", hess_val)

    def sample_grad(params: np.ndarray) -> np.ndarray:
        return np.array([2 * (params[0] - 2), 6 * (params[1] + 1)])

    optimal = gradient_descent(sample_grad, x0, lr=0.1, steps=50)
    print("Optimal parameters after gradient descent:", optimal)
