import os
import types
import numpy as np
import torch

class BaseParams(object):
    def __init__(self):
        self.set_params()
        self.compute_helper_params()

    def set_params(self):
        self.model_type = None
        self.log_to_file = True
        self.dtype = torch.float
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.rand_seed = 123456789
        self.rand_state = np.random.RandomState(self.rand_seed)
        self.out_dir = os.path.expanduser("~")+"/Work/Projects/"
        self.data_dir = os.path.expanduser("~")+"/Work/Datasets/"

    def compute_helper_params(self):
        pass
