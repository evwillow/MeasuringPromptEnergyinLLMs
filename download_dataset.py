#!/usr/bin/env python3
"""
Script to download the lmsys-chat-1m dataset and save it to the /data folder.
Requires huggingface_hub and datasets libraries.
"""

import os
from datasets import load_dataset
from pathlib import Path
from huggingface_hub import login

def download_lmsys_chat_dataset():
    """
    Download the lmsys-chat-1m dataset and save it to the current directory.
    """
    print("Downloading lmsys-chat-1m dataset...")
    
    # Check for authentication
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
        # Load and save dataset
        ds = load_dataset("lmsys/lmsys-chat-1m")
        ds.save_to_disk("lmsys-chat-1m")
        print(f"Dataset downloaded: {len(ds['train']):,} examples")
        return True
            
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    success = download_lmsys_chat_dataset()
    if success:
        print("Download complete!")
    else:
        print("Download failed.")
