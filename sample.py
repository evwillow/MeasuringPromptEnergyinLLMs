#!/usr/bin/env python3
"""
Simple script to sample and explore the lmsys-chat-1m dataset.
"""

import json
from pathlib import Path
from collections import Counter
from datasets import load_dataset

def load_sample(sample_size=1000):
    """Load sample from data/conversations.json."""
    data_file = Path("data/conversations.json")
    
    if not data_file.exists():
        print("Error: data/conversations.json not found!")
        return []
    
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            all_conversations = json.loads(f.read())
            return all_conversations[:sample_size]
            
    except Exception as e:
        print(f"Error: {e}")
        return []

def show_stats(sample_data):
    """Show basic statistics."""
    print(f"\nStats: {len(sample_data):,} examples")
    
    models = [example['model'] for example in sample_data]
    model_counts = Counter(models)
    print(f"Top models:")
    for model, count in model_counts.most_common(3):
        print(f"  {model}: {count:,}")
    
    languages = [example['language'] for example in sample_data]
    language_counts = Counter(languages)
    print(f"Languages:")
    for lang, count in language_counts.most_common(3):
        print(f"  {lang}: {count:,}")

def show_conversations(sample_data, num_examples=2):
    """Show sample conversations."""
    print(f"\nSample Conversations:")
    
    for i in range(min(num_examples, len(sample_data))):
        example = sample_data[i]
        print(f"\n--- {i+1} ---")
        print(f"Model: {example['model']} | Language: {example['language']}")
        
        for message in example['conversation']:
            role = message['role'].upper()
            content = message['content']
            print(f"{role}: {content}")

if __name__ == "__main__":
    sample = load_sample(sample_size=1000)
    
    if sample:
        show_stats(sample)
        show_conversations(sample, num_examples=2)
        print(f"\nReady!")
    else:
        print("No data loaded.")