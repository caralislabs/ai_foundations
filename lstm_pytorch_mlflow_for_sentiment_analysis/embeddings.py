import numpy as np
from urllib.request import urlretrieve
import zipfile
import gzip
import os

def load_glove_embeddings(glove_path, embedding_dim=100):
    """Load GloVe embeddings from file"""
    print(f"Loading GloVe embeddings from {glove_path}...")
    embeddings = {}
    
    # Handle both .txt and .gz files
    if glove_path.endswith('.gz'):
        file_obj = gzip.open(glove_path, 'rt', encoding='utf-8')
    else:
        file_obj = open(glove_path, 'r', encoding='utf-8')
    
    try:
        for line in file_obj:
            values = line.split()
            word = values[0]
            vector = np.asarray(values[1:], dtype='float32')
            if len(vector) == embedding_dim:  # Ensure correct dimension
                embeddings[word] = vector
    finally:
        file_obj.close()
    
    print(f"Loaded {len(embeddings)} word vectors")
    return embeddings


def create_embedding_matrix(vocab_to_idx, embeddings_dict, embedding_dim):
    """Create embedding matrix from pre-trained embeddings"""
    vocab_size = len(vocab_to_idx)
    embedding_matrix = np.zeros((vocab_size, embedding_dim))
    
    # Initialize with random values for unknown words
    embedding_matrix = np.random.normal(scale=0.6, size=(vocab_size, embedding_dim))
    
    found_count = 0
    for word, idx in vocab_to_idx.items():
        if word in embeddings_dict:
            embedding_matrix[idx] = embeddings_dict[word]
            found_count += 1
    
    print(f"Found pre-trained vectors for {found_count}/{vocab_size} words ({found_count/vocab_size*100:.1f}%)")
    return embedding_matrix

def download_glove_embeddings(embedding_dim=100):
    """Download GloVe embeddings if not present"""
    glove_urls = {
        50: "https://nlp.stanford.edu/data/glove.6B.zip",
        100: "https://nlp.stanford.edu/data/glove.6B.zip",
        200: "https://nlp.stanford.edu/data/glove.6B.zip",
        300: "https://nlp.stanford.edu/data/glove.6B.zip"
    }
    
    if embedding_dim not in glove_urls:
        raise ValueError(f"Embedding dimension {embedding_dim} not available. Choose from {list(glove_urls.keys())}")
    
    filename = f"glove.6B.{embedding_dim}d.txt"
    zip_filename = "glove.6B.zip"
    
    if not os.path.exists(filename):
        print(f"Downloading GloVe {embedding_dim}d embeddings...")
        if not os.path.exists(zip_filename):
            urlretrieve(glove_urls[embedding_dim], zip_filename)
        
        print("Extracting embeddings...")
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extract(filename)
        
        # Clean up zip file
        os.remove(zip_filename)
    
    return filename
