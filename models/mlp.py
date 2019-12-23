import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from modules.base import BaseModule

class Mlp(BaseModule):
    def __init__(self):
        super(Mlp, self).__init__()

    def setup_model(self):
        self.fc1 = nn.Linear(
            in_features = self.params.num_pixels,
            out_features = self.params.num_latent,
            bias = True)
        self.fc2 = nn.Linear(
            in_features = self.params.num_latent,
            out_features = 10,
            bias = True)
        self.dropout = nn.Dropout(p=self.params.dropout_rate)

    def loss(self, dictargs):
        return F.nll_loss(dictargs["prediction"], dictargs["target"])

    def forward(self, x):
        x = x.view(-1, 28 * 28)
        x = self.dropout(F.leaky_relu(self.fc1(x)))
        x = F.log_softmax(self.fc2(x), dim=1)
        return x