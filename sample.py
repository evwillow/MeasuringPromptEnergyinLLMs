#!/usr/bin/env python3
"""
Simple script to sample and explore the lmsys-chat-1m dataset.
"""

import json
from pathlib import Path
from collections import Counter
from datasets import load_dataset

def load_sample(sample_size=1000):
    """Load sample from data/ folder."""
    data_file = Path("data/conversations.json")
    metadata_file = Path("data/metadata.json")
    
    # Check if conversations.json exists and has data
    if data_file.exists():
        try:
            with open(data_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if content.strip():
                    all_conversations = json.loads(content)
                    return all_conversations[:sample_size]
        except Exception as e:
            print(f"Error loading conversations: {e}")
    
    # If conversations.json is empty, use metadata for stats
    if metadata_file.exists():
        print("Using metadata for statistics...")
        with open(metadata_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        # Create mock data structure for display
        mock_data = []
        models = metadata.get('models', [])
        languages = metadata.get('languages', [])
        
        for i in range(min(sample_size, 10)):  # Create 10 mock examples
            mock_data.append({
                'model': models[i % len(models)] if models else 'unknown',
                'language': languages[i % len(languages)] if languages else 'en',
                'conversation': [
                    {'role': 'user', 'content': f'Mock conversation {i+1}'},
                    {'role': 'assistant', 'content': f'Mock response {i+1}'}
                ]
            })
        
        return mock_data
    
    print("Error: No data found in data/ folder!")
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