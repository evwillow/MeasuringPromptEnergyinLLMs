#!/usr/bin/env python3
"""
Download lmsys-chat-1m dataset and transform to JSON format.
"""

import json
import os
from datasets import load_dataset
from pathlib import Path
from huggingface_hub import login
from collections import Counter

# Load environment variables from .env file
def load_env():
    """Load environment variables from .env file."""
    env_file = Path(".env")
    if env_file.exists():
        with open(env_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()

def download_dataset(sample_size=1000000):
    """Download and transform dataset to JSON format."""
    # Load environment variables
    load_env()
    
    print(f"Loading {sample_size:,} conversations...")
    
    # Create data folder
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # Check authentication
    try:
        token = os.getenv('HUGGINGFACE_HUB_TOKEN')
        if token:
            login(token=token)
        else:
            print("No token found. Set HUGGINGFACE_HUB_TOKEN or run 'huggingface-cli login'")
            return False
    except Exception as e:
        print(f"Authentication failed: {e}")
        return False
    
    try:
        # Load dataset with streaming
        dataset = load_dataset("lmsys/lmsys-chat-1m", split="train", streaming=True)
        
        # Process conversations
        conversations = []
        for i, example in enumerate(dataset):
            if i >= sample_size:
                break
            
            # Keep all original data
            conversations.append(example)
            
            # Progress update
            if (i + 1) % 10000 == 0:
                print(f"Processed {i + 1:,} conversations...")
        
        # Save conversations
        conversations_file = data_dir / "conversations.json"
        print(f"Saving {len(conversations):,} conversations...")
        
        with open(conversations_file, 'w', encoding='utf-8') as f:
            json.dump(conversations, f, separators=(',', ':'), ensure_ascii=False)
        
        # Create metadata
        models = [conv["model"] for conv in conversations]
        languages = [conv["language"] for conv in conversations]
        
        metadata = {
            "total_conversations": len(conversations),
            "models": list(set(models)),
            "languages": list(set(languages)),
            "model_distribution": {model: models.count(model) for model in set(models)},
            "language_distribution": {lang: languages.count(lang) for lang in set(languages)}
        }
        
        metadata_file = data_dir / "metadata.json"
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        print(f"\nComplete!")
        print(f"Saved to: {data_dir}")
        print(f"- conversations.json: {len(conversations):,} conversations")
        print(f"- metadata.json: Dataset statistics")
        
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    success = download_dataset(sample_size=1000000)
    if success:
        print("Download complete!")
    else:
        print("Download failed.")
