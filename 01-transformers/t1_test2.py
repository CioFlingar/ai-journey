import torch
import torch.nn as nn

vocab_size = 6
embedding_dim = 4

embedding = nn.Embedding(100, 8)
token_ids = torch.tensor([[2, 4, 1], [5, 0, 3]])
vectors = embedding(token_ids)

print("Token IDs shape:", token_ids.shape)
print("Embedding matrix shape:", embedding.weight.shape)
print("Output shape:", vectors.shape)
print(vectors)