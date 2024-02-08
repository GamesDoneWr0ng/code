from numpy import random
import torch
import matplotlib.pyplot as plt
import torch.nn as nn

#inputs  = torch.tensor(([0],[1],[2],[3],[4],[5],[6],[7],[8] ,[9]), dtype=torch.float32)
#outputs = torch.tensor(([1],[3],[2],[5],[7],[8],[8],[9],[10],[12]), dtype=torch.float32)
inputs = torch.linspace(0, 10, 50, dtype=torch.float32).unsqueeze(-1)
outputs = 2*torch.sin(inputs+2) + torch.tensor(random.randn(50), dtype=torch.float32).unsqueeze(-1)/3

assert inputs.shape[0] == outputs.shape[0]

class customModule(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.a = torch.nn.Parameter(torch.randn(()))
        self.b = torch.nn.Parameter(torch.randn(()))
        self.c = torch.nn.Parameter(torch.randn(()))
        self.d = torch.nn.Parameter(torch.randn(()))

    def forward(self, x):
        return self.a * torch.sin(self.b * x + self.c) + self.d

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

xValues = torch.linspace(inputs.min(), inputs.max(), 100)
yValues = model(xValues.unsqueeze(-1))

plt.plot(xValues.detach().numpy(), yValues.detach().numpy())

plt.show()