
# Multimodal Sequential Skin Condition Modelling using Deep Neural Networks

## Executive Summary
This project reformulates a traditional skin-condition classification system into a **multimodal
sequence modelling problem**, aligned with the Deep Neural Networks and Learning Systems (DNNLS) module.

Given a sequence of facial skin images and corresponding textual skin reports, the model predicts
the next skin-condition state in the sequence. This requires joint reasoning over **visual and textual
modalities** as well as **temporal dynamics**.

Our main architectural innovation is the use of **cross-modal attention** to better align image and
text representations before temporal modelling.

## Architecture
- Visual Encoder: CNN-based image feature extractor
- Text Encoder: LSTM-based text sequence encoder
- Multimodal Fusion: Cross-modal attention mechanism (innovation)
- Sequence Model: Temporal LSTM
- Output Head: Skin-condition prediction (K+1)

## Dataset
- Images: Facial skin images (chronological)
- Text: Dermatology-style skin descriptions
- Labels: Skin condition category

(Synthetic sequence construction is used for experimental purposes)

## Results
The attention-based fusion improves temporal coherence and prediction stability compared to
simple feature concatenation.

## How to Run
Open `experiments.ipynb` and run all cells.

## Author
Manish Reddy
