import torch.nn as nn
import torch.nn.functional as F

class BaseModel(nn.Module):
    def __init__(self):
        super(BaseModel, self).__init__()

    def forward(self, x):
        raise NotImplementedError("Forward method not implemented.")
