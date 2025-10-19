#!/usr/bin/env python3
"""
Simple example showing how to access the lmsys-chat-1m dataset.
"""

from datasets import load_from_disk

# Load the dataset
print("Loading dataset...")
dataset = load_from_disk("lmsys-chat-1m")

# Basic info
print(f"Dataset loaded! Total examples: {len(dataset['train']):,}")
print(f"Features: {list(dataset['train'].features.keys())}")

# Get first example
first_example = dataset['train'][0]
print(f"\nFirst example:")
for key, value in first_example.items():
    if isinstance(value, str) and len(value) > 100:
        print(f"  {key}: {value[:100]}...")
    else:
        print(f"  {key}: {value}")

# Get a few more examples
print(f"\nNext 2 examples:")
for i in range(1, 3):
    example = dataset['train'][i]
    print(f"\nExample {i+1}:")
    print(f"  Model: {example.get('model', 'N/A')}")
    print(f"  Role: {example.get('role', 'N/A')}")
    print(f"  Content: {example.get('content', 'N/A')[:150]}...")

print(f"\n[SUCCESS] Dataset access working!")
