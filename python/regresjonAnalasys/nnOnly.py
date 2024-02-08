from numpy import random
import torch
import matplotlib.pyplot as plt
import torch.nn as nn

#inputs  = torch.tensor(([0],[1],[2],[3],[4],[5],[6],[7],[8] ,[9]), dtype=torch.float32)
#outputs = torch.tensor(([1],[3],[2],[5],[7],[8],[8],[9],[10],[12]), dtype=torch.float32)
lin = torch.linspace(0, 10, 21, dtype=torch.float32)
inputs = torch.stack(torch.meshgrid(lin,lin)).transpose(0,2).reshape(441,2)
outputs = (torch.sin(inputs[:,0])+torch.cos(inputs[:,1])).unsqueeze(-1)
outputs+= torch.randn(outputs.shape)/3

assert inputs.shape[0] == outputs.shape[0]

model = nn.Sequential(
    nn.Linear(inputs.shape[1], 10),
    nn.Tanh(),
    nn.Linear(10, 10),
    nn.Tanh(),
    nn.Linear(10, outputs.shape[1])
)

epochs = 50000
learning_rate = 1e-3
loss_fn = torch.nn.MSELoss(reduction='sum')
optimizer = torch.optim.RMSprop(model.parameters(), lr=learning_rate)

lastLoss = -1
# learning
for t in range(epochs):
    yPred = model(inputs)

    loss = loss_fn(yPred, outputs)
    if t % 100 == 0:
        print(t, loss.item())
        if lastLoss == loss.item():
            break
        lastLoss = loss.item()

    if loss.item() < 2.5:
        break

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print(t, loss.item(), loss_fn(model(inputs), (torch.sin(inputs[:,0])+torch.cos(inputs[:,1])).unsqueeze(-1)).item())

# ploting
ax = plt.axes(projection='3d')
x,y = inputs.T
z = outputs.T
ax.scatter(y,x,z)
#plt.scatter(inputs, outputs)


lin = torch.linspace(0, 10, 100, dtype=torch.float32)
xValues, yValues = torch.meshgrid(lin,lin)
zValues = model(torch.stack((xValues, yValues)).transpose(0,2).reshape(10000,2)).reshape(xValues.shape)

ax.plot_surface(xValues.detach().numpy(), yValues.detach().numpy(), zValues.detach().numpy(), cmap=plt.cm.YlGnBu_r)

plt.show()