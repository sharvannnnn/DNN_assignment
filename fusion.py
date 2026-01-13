
import torch.nn as nn

class CrossModalAttention(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.attn = nn.MultiheadAttention(dim, num_heads=4)

    def forward(self, image_feat, text_feat):
        image_feat = image_feat.unsqueeze(0)
        text_feat = text_feat.unsqueeze(0)
        fused, _ = self.attn(image_feat, text_feat, text_feat)
        return fused.squeeze(0)
