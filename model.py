
import torch.nn as nn
from visual_encoder import VisualEncoder
from text_encoder import TextEncoder
from fusion import CrossModalAttention
from sequence_model import SequenceModel

class MultimodalSkinModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.visual = VisualEncoder()
        self.text = TextEncoder()
        self.fusion = CrossModalAttention(128)
        self.sequence = SequenceModel(128, 64)
        self.classifier = nn.Linear(64, 7)

    def forward(self, img, txt):
        v = self.visual(img)
        t = self.text(txt)
        fused = self.fusion(v, t)
        fused = fused.unsqueeze(1)
        seq = self.sequence(fused)
        return self.classifier(seq)
