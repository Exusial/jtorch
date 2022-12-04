import unittest
import numpy as np
import torch

class TestMisc(unittest.TestCase):
    def test_update_grad(self):
        class Net(torch.nn.Module):
            def __init__(self):
                super().__init__()
                self.a = torch.nn.Parameter(torch.Tensor([1.0, 2.0]))
        net = Net()
        assert(net.a.requires_grad)
        net.load_state_dict({"a": torch.Tensor([3.0, 4.0])})
        assert(net.a.requires_grad)

if __name__ == "__main__":
    unittest.main()
