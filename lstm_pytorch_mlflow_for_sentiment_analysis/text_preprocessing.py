import mlflow
import re
import torch
from collections import Counter


def get_vocab_to_index(vocab_to_idx_uri):
    vocab_to_idx = mlflow.artifacts.load_dict(vocab_to_idx_uri)
    return vocab_to_idx

def text_to_input(text, vocab_to_idx):
    # Device configuration
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")

    # Preprocess text
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = text.split()
    indices = [vocab_to_idx.get(token, vocab_to_idx['<UNK>']) for token in tokens]

    config = {
        "max_length": 128
    }

    # Pad or truncate
    if len(indices) < config['max_length']:
        indices.extend([vocab_to_idx['<PAD>']] * (config['max_length'] - len(indices)))
    else:
        indices = indices[:config['max_length']]
    
    input_data = [indices]
    return input_data

def build_vocabulary(texts, min_freq=2):
    """Build vocabulary from texts"""
    all_tokens = []
    for text in texts:
        # Simple preprocessing
        text = text.lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        tokens = text.split()
        all_tokens.extend(tokens)
    
    # Count tokens
    token_counts = Counter(all_tokens)
    
    # Create vocabulary
    vocab_to_idx = {'<PAD>': 0, '<UNK>': 1}
    idx = 2
    
    for token, count in token_counts.items():
        if count >= min_freq:
            vocab_to_idx[token] = idx
            idx += 1
    
    return vocab_to_idx