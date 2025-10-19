#!/usr/bin/env python3
"""
Simple script to sample and explore the lmsys-chat-1m dataset.
"""

from datasets import load_dataset
from collections import Counter

def sample_dataset(sample_size=1000):
    """
    Load a sample of the lmsys-chat-1m dataset.
    """
    print(f"Loading {sample_size:,} examples from lmsys-chat-1m...")
    
    # Load dataset with streaming
    dataset = load_dataset("lmsys/lmsys-chat-1m", split="train", streaming=True)
    
    # Take a sample
    sample_data = []
    for i, example in enumerate(dataset):
        if i >= sample_size:
            break
        sample_data.append(example)
    
    print(f"Loaded {len(sample_data):,} examples")
    return sample_data

def show_stats(sample_data):
    """Show basic statistics about the sample."""
    print(f"\nDataset Statistics:")
    print(f"Total examples: {len(sample_data):,}")
    
    # Model distribution
    models = [example['model'] for example in sample_data]
    model_counts = Counter(models)
    print(f"\nTop models:")
    for model, count in model_counts.most_common(5):
        print(f"  {model}: {count:,}")
    
    # Language distribution
    languages = [example['language'] for example in sample_data]
    language_counts = Counter(languages)
    print(f"\nLanguages:")
    for lang, count in language_counts.most_common(3):
        print(f"  {lang}: {count:,}")

def show_conversations(sample_data, num_examples=3):
    """Show sample conversations."""
    print(f"\nSample Conversations:")
    
    for i in range(min(num_examples, len(sample_data))):
        example = sample_data[i]
        print(f"\n--- Conversation {i+1} ---")
        print(f"Model: {example['model']} | Language: {example['language']} | Messages: {len(example['conversation'])}")
        
        # Show full conversation
        for j, message in enumerate(example['conversation']):
            role = message['role'].upper()
            content = message['content']
            print(f"\n{role}: {content}")

if __name__ == "__main__":
    # Load sample
    sample = sample_dataset(sample_size=1000)
    
    # Show statistics
    show_stats(sample)
    
    # Show sample conversations
    show_conversations(sample, num_examples=2)
    
    print(f"\nSample ready for analysis!")