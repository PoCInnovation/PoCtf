import torch
import torch.nn as nn

FLAG = "PoC{4UD1T_M0D3LS_NOT_JU5T_C0D3}"

def encode_flag(flag):
    return torch.tensor([ord(c) for c in flag], dtype=torch.float32)

class ShadowNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(16, 16)
        self.fc2 = nn.Linear(16, 2)

        self.shadow = nn.Linear(32, 1, bias=False)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

model = ShadowNet()

encoded = encode_flag(FLAG)
flat = model.shadow.weight.view(-1)

flat[:len(encoded)] = encoded

torch.save(model.state_dict(), "model.pt")
print("[+] Shadow model generated.")
