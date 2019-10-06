import torch
import torch.nn as nn
import torch.nn.functional as F

from model.net.Flatten_conv1d import flatten_conv2d 

class LeNet_5_CIFAR_Flatten(nn.Module):
    def __init__(self, mask=False):
        super(LeNet_5_CIFAR_Flatten, self).__init__()


        self.conv1 = nn.Conv2d(3, 6, kernel_size=(5, 5))
        self.conv2 = flatten_conv2d(6, 16, kernel_size=5)
        # self.conv2 = nn.Conv2d(6, 16, kernel_size=(5, 5))
        self.conv3 = nn.Conv2d(16, 120, kernel_size=(5,5))
        self.fc1 = nn.Linear(120, 84)
        self.fc2 = nn.Linear(84, 10)
        #self.fc3 = linear(48, 10)

    def forward(self, x):
        # Conv1
        x = self.conv1(x)
        x = F.relu(x)
        x = F.max_pool2d(x, kernel_size=(2, 2), stride=2)

        # Conv2
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, kernel_size=(2, 2), stride=2)

        # Conv3
        x = self.conv3(x)
        x = F.relu(x)

        # Fully-connected
        x = x.view(-1, 120)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        #x = F.relu(x)
        #x = self.fc3(x)
        x = F.log_softmax(x, dim=1)

        return x