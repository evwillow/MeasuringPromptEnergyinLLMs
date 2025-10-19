#!/usr/bin/env python3
"""
Super fast download of lmsys-chat-1m dataset with progress bar
"""

import json
import os
import sys
from datasets import load_dataset
from pathlib import Path
from huggingface_hub import login
from collections import Counter
import gc

def get_huggingface_token():
    """Get Hugging Face token from user input or .env file."""
    # Try .env file first
    env_file = Path(".env")
    if env_file.exists():
        with open(env_file, 'r', encoding='utf-8') as f:
            for line in f:
                if 'HUGGINGFACE_HUB_TOKEN=' in line and not line.startswith('#'):
                    token = line.split('=', 1)[1].strip()
                    if token:
                        return token
    
    # Ask user for token
    print("Hugging Face token required for dataset access.")
    print("Get your token from: https://huggingface.co/settings/tokens")
    token = input("Enter your Hugging Face token: ").strip()
    
    if not token:
        print("Error: No token provided")
        return None
    
    # Save to .env file for future use
    with open(env_file, 'w', encoding='utf-8') as f:
        f.write(f"HUGGINGFACE_HUB_TOKEN={token}\n")
    
    return token

def show_progress(current, total, bar_length=50):
    """Show progress bar."""
    percent = current / total
    filled = int(bar_length * percent)
    bar = '=' * filled + '-' * (bar_length - filled)
    sys.stdout.write(f'\rProgress: [{bar}] {percent:.1%} ({current:,}/{total:,})')
    sys.stdout.flush()

def download_dataset(sample_size=1000000):
    """Ultra-fast download with optimized performance."""
    print("Starting download...")
    
    # Get token
    token = get_huggingface_token()
    if not token:
        return False
    
    # Create data folder
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # Auth
    try:
        login(token=token)
    except Exception as e:
        print(f"Authentication failed: {e}")
        return False
    
    try:
        # Load with streaming - ultra-optimized settings
        dataset = load_dataset("lmsys/lmsys-chat-1m", split="train", streaming=True)
        
        conversations = []
        batch_size = 100000  # Massive batches for maximum speed
        models = []
        languages = []
        
        # Pre-allocate lists for speed
        conversations = [None] * sample_size
        models = [None] * sample_size
        languages = [None] * sample_size
        
        for i, example in enumerate(dataset):
            if i >= sample_size:
                break
            
            # Direct assignment for maximum speed
            conversations[i] = example
            models[i] = example["model"]
            languages[i] = example["language"]
            
            # Progress bar every 100k items
            if (i + 1) % batch_size == 0:
                show_progress(i + 1, sample_size)
                # Force garbage collection for memory efficiency
                gc.collect()
        
        show_progress(sample_size, sample_size)
        print()
        
        # Ultra-fast JSON saving with maximum buffering
        conversations_file = data_dir / "conversations.json"
        
        # Maximum speed JSON writing
        with open(conversations_file, 'w', encoding='utf-8', buffering=65536) as f:
            json.dump(conversations, f, separators=(',', ':'), ensure_ascii=False)
        
        # Fast metadata creation with pre-computed data
        metadata = {
            "total_conversations": len(conversations),
            "models": list(set(models)),
            "languages": list(set(languages)),
            "model_distribution": dict(Counter(models)),
            "language_distribution": dict(Counter(languages))
        }
        
        # Fast metadata save
        with open(data_dir / "metadata.json", 'w', encoding='utf-8', buffering=65536) as f:
            json.dump(metadata, f, separators=(',', ':'), ensure_ascii=False)
        
        print(f"Complete! {len(conversations):,} conversations saved")
        
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    success = download_dataset(sample_size=1000000)
    if success:
        print("Download complete!")
    else:
        print("Download failed!")
