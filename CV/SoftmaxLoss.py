import numpy as np
import torch


class SoftMaxLoss:
    def __init__(self):
        self.softmax = None
        self.grad = None
        self.dnx = None

    def __call__(self, nx):
        shifted_x = nx - np.max(nx)
        ex = np.exp(shifted_x)
        sum_ex = np.sum(ex)
        self.solfmax = ex / sum_ex
        return self.solfmax

    def get_grad(self):
        self.grad = self.solfmax[:, np.newaxis] * self.solfmax[np.newaxis, :]
        for i in range(len(self.grad)):
            self.grad[i, i] -= self.solfmax[i]
        self.grad = - self.grad
        return self.grad

    def backward(self, dl):
        self.get_grad()
        self.dnx = np.sum(self.grad * dl, axis=1)
        return self.dnx


np.random.seed(123)
np.set_printoptions(precision=8, suppress=True, linewidth=120)

d_loss = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19], dtype=float)
d_loss_tensor = torch.tensor(d_loss, requires_grad=True)

softmax_numpy = SoftMaxLoss()
x_numpy = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=float)
soft_numpy = softmax_numpy(x_numpy)
x_grad_numpy = softmax_numpy.backward(d_loss)

x_tensor = torch.tensor(x_numpy, requires_grad=True)
soft_tensor = torch.nn.functional.softmax(x_tensor, dim=0)
soft_tensor.backward(d_loss_tensor)
x_grad_tensor = x_tensor.grad

print(soft_numpy)
print(soft_tensor.data.numpy())
print()
print(x_grad_numpy)
print(x_grad_tensor.data.numpy())