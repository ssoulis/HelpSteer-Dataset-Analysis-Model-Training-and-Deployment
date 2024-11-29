# models.py
import torch.nn as nn

class DistilBERTForRegression(nn.Module):
    def __init__(self, base_model):
        super(DistilBERTForRegression, self).__init__()
        self.base_model = base_model
        self.regression_head = nn.Linear(self.base_model.config.hidden_size, 1)

    def forward(self, precomputed_embeddings):
        batch_size = precomputed_embeddings.size(0)
        expanded_embeddings = precomputed_embeddings.unsqueeze(1).expand(batch_size, 512, 768)
        transformer_output = self.base_model(inputs_embeds=expanded_embeddings)
        pooled_output = transformer_output.last_hidden_state[:, 0]
        return self.regression_head(pooled_output)
