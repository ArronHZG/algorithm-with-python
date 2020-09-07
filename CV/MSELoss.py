import torch
import numpy as np


class MSELoss:
    def __init__(self):
        self.x = None
        self.y = None

    def __call__(self, x, y):
        self.x = x
        self.y = y
        return np.sum(np.square(x - y)) / x.size

    def backward(self):
        dx = 2 * (self.x - self.y) / self.x.size
        return dx, -dx


if __name__ == '__main__':
    np.random.seed(123)
    np.set_printoptions(precision=6, suppress=True, linewidth=80)

    x_numpy = np.random.random(27)
    y_numpy = np.random.random(27)
    x_torch = torch.tensor(x_numpy, requires_grad=True)
    y_torch = torch.tensor(y_numpy, requires_grad=True)

    loss_func_numpy = MSELoss()
    loss_func_torch = torch.nn.MSELoss().float()

    loss_numpy = loss_func_numpy(x_numpy, y_numpy)
    loss_torch = loss_func_torch(x_torch, y_torch)

    loss_torch.backward()
    dx_numpy, dy_numpy = loss_func_numpy.backward()

    print(loss_numpy)
    print(loss_torch.data.numpy())
    print("----------")
    print(dx_numpy)
    print(x_torch.grad.numpy())
    print("----------")
    print(dy_numpy)
    print(y_torch.grad.numpy())
