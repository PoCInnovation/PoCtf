import torch

state = torch.load("model.pt")
print(state.keys())
w = state["shadow.weight"].flatten()
flag = "".join(chr(int(v)) for v in w if 32 <= v <= 126)
print(flag)
