import torch
import numpy as np


class CELoss:
    def __init__(self):
        self.nx = None
        self.ny = None
        self.dnx = None

    def loss(self, nx, ny):
        self.nx = nx
        self.ny = ny
        loss = np.sum(- ny * np.log(nx))
        return loss

    def backward(self):
        self.dnx = - self.ny / self.nx
        return self.dnx


if __name__ == '__main__':
    np.random.seed(123)
    np.set_printoptions(precision=3, suppress=True, linewidth=120)

    entropy = CELoss()

    x = np.random.random([5, 10])
    y = np.random.random([5, 10])
    x_tensor = torch.tensor(x, requires_grad=True)
    y_tensor = torch.tensor(y, requires_grad=True)

    loss_numpy = entropy.loss(x, y)
    grad_numpy = entropy.backward()

    loss_tensor = (- y_tensor * torch.log(x_tensor)).sum()
    loss_tensor.backward()
    grad_tensor = x_tensor.grad

    print("Python Loss :", loss_numpy)
    print("PyTorch Loss :", loss_tensor.data.numpy())

    print("\nPython dx :")
    print(grad_numpy)
    print("\nPyTorch dx :")
    print(grad_tensor.data.numpy())
