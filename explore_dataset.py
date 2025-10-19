#!/usr/bin/env python3
"""
Simple script to explore the lmsys-chat-1m dataset.
"""

from datasets import load_from_disk
from collections import Counter

def explore_dataset():
    """
    Load and explore the lmsys-chat-1m dataset.
    """
    print("Loading dataset...")
    dataset = load_from_disk("lmsys-chat-1m")
    
    print(f"Dataset loaded: {len(dataset['train']):,} examples")
    print(f"Features: {list(dataset['train'].features.keys())}")
    
    # Show model distribution
    models = [example['model'] for example in dataset['train']]
    model_counts = Counter(models)
    print(f"\nTop 5 models:")
    for model, count in model_counts.most_common(5):
        print(f"  {model}: {count:,}")
    
    # Show language distribution
    languages = [example['language'] for example in dataset['train']]
    language_counts = Counter(languages)
    print(f"\nLanguages:")
    for lang, count in language_counts.most_common(3):
        print(f"  {lang}: {count:,}")
    
    # Show sample conversations
    print(f"\nSample conversations:")
    for i in range(3):
        example = dataset['train'][i]
        print(f"\n--- Example {i+1} ---")
        print(f"Model: {example['model']}")
        print(f"Language: {example['language']}")
        print(f"Messages: {len(example['conversation'])}")
        
        # Show first message
        if example['conversation']:
            first_msg = example['conversation'][0]
            content = first_msg['content'][:100] + "..." if len(first_msg['content']) > 100 else first_msg['content']
            print(f"First message ({first_msg['role']}): {content}")
    
    return dataset

def search_by_model(dataset, model_name, limit=3):
    """Search for conversations by a specific model."""
    print(f"\nSearching for model: {model_name}")
    
    results = []
    for i, example in enumerate(dataset['train']):
        if example['model'] == model_name:
            results.append((i, example))
            if len(results) >= limit:
                break
    
    print(f"Found {len(results)} conversations:")
    for idx, (original_idx, example) in enumerate(results):
        print(f"\n--- Result {idx+1} ---")
        print(f"Language: {example['language']}")
        if example['conversation']:
            first_msg = example['conversation'][0]
            content = first_msg['content'][:150] + "..." if len(first_msg['content']) > 150 else first_msg['content']
            print(f"First message: {content}")

if __name__ == "__main__":
    dataset = explore_dataset()
    
    # Example search
    search_by_model(dataset, "gpt-3.5-turbo", limit=2)
    
    print(f"\nDataset ready for analysis!")