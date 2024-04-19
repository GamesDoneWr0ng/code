import numpy as np
import torch
import matplotlib.pyplot as plt
import torch.nn as nn

inputs  = torch.tensor(([1],[3],[5],[7],[9],[11],[13],[15],[17],[19],[21],[23]), dtype=torch.float32)
outputs = torch.tensor(([94], [43], [26], [61], [113], [138], [111], [59], [35], [64], [117], [146]), dtype=torch.float32)
#inputs = torch.linspace(0, 10, 50, dtype=torch.float32).unsqueeze(-1)
#outputs = 2*torch.sin(inputs+2) + torch.tensor(random.randn(50), dtype=torch.float32).unsqueeze(-1)/3

assert inputs.shape[0] == outputs.shape[0]

class customModule(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.a = torch.nn.Parameter(torch.randn(()))
        #self.b = torch.nn.Parameter(torch.randn(()))
        self.c = torch.nn.Parameter(torch.randn(()))
        self.d = torch.nn.Parameter(torch.randn(()))

    def forward(self, x):
        return self.a * torch.sin(np.pi/6 * x + self.c) + self.d

model = customModule()

epochs = 50000
learning_rate = 1e-5
loss_fn = torch.nn.MSELoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

# learning
for t in range(epochs):
    yPred = model(inputs)

    loss = loss_fn(yPred, outputs)
    if t % 100 == 0:
        print(t, loss.item())

    if loss.item() < 0.5:
        break

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print(t, loss.item())

# ploting
#ax = plt.axes(projection='3d')
#x,y = inputs.T
#z = outputs
#ax.scatter(x,y,z)
plt.scatter(inputs, outputs)

xValues = torch.linspace(inputs.min()-1, inputs.max()+1, 100)
yValues = model(xValues.unsqueeze(-1))

plt.plot(xValues.detach().numpy(), yValues.detach().numpy())

plt.show()
"""
A = 54.92
phi = 52.48
d = 83.88

A=-54.8026
phi=-0.9208
d=-83.9008
"""