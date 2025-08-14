import torch
import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear1 = nn.Linear(10, 5)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(5, 1)

    def forward(self, x):
        x = self.linear1(x)
        x = self.relu(x)
        x = self.linear2(x)
        return x

if __name__ == "__main__":
    print("PyTorch version:", torch.__version__)
    
    model = SimpleModel()
    print("\nModel Architecture:")
    print(model)
    
    # Create a dummy input tensor and pass it through the model
    dummy_input = torch.randn(1, 10)
    output = model(dummy_input)
    
    print("\nSuccessfully created a simple PyTorch model and performed a forward pass.")
    print("Output tensor:", output)

