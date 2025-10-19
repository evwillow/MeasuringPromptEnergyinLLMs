#!/usr/bin/env python3
"""
Transform lmsys-chat-1m dataset into clean JSON files.
"""

import json
import os
from datasets import load_dataset
from pathlib import Path

def create_data_folder():
    """Create data folder if it doesn't exist."""
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    return data_dir

def transform_conversation(example):
    """Transform a single conversation into clean format."""
    return {
        "id": example["conversation_id"],
        "model": example["model"],
        "language": example["language"],
        "turn_count": example["turn"],
        "messages": example["conversation"],
        "total_messages": len(example["conversation"]),
        "user_messages": len([msg for msg in example["conversation"] if msg["role"] == "user"]),
        "assistant_messages": len([msg for msg in example["conversation"] if msg["role"] == "assistant"])
    }

def save_conversations_batch(conversations, batch_num, data_dir):
    """Save a batch of conversations to JSON file."""
    filename = data_dir / f"conversations_batch_{batch_num:04d}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(conversations, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(conversations)} conversations to {filename}")
    return filename

def create_metadata(conversations, data_dir):
    """Create metadata file with dataset statistics."""
    models = [conv["model"] for conv in conversations]
    languages = [conv["language"] for conv in conversations]
    
    metadata = {
        "total_conversations": len(conversations),
        "models": list(set(models)),
        "languages": list(set(languages)),
        "model_counts": {model: models.count(model) for model in set(models)},
        "language_counts": {lang: languages.count(lang) for lang in set(languages)},
        "avg_messages_per_conversation": sum(conv["total_messages"] for conv in conversations) / len(conversations),
        "total_messages": sum(conv["total_messages"] for conv in conversations)
    }
    
    metadata_file = data_dir / "metadata.json"
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    print(f"Saved metadata to {metadata_file}")
    return metadata

def transform_dataset(sample_size=1000, batch_size=100):
    """
    Transform the dataset into clean JSON files.
    
    Args:
        sample_size: Number of conversations to process
        batch_size: Number of conversations per JSON file
    """
    print(f"Transforming {sample_size:,} conversations...")
    
    # Create data folder
    data_dir = create_data_folder()
    
    # Load dataset with streaming
    dataset = load_dataset("lmsys/lmsys-chat-1m", split="train", streaming=True)
    
    # Process conversations in batches
    all_conversations = []
    batch_num = 0
    current_batch = []
    
    for i, example in enumerate(dataset):
        if i >= sample_size:
            break
        
        # Transform conversation
        transformed = transform_conversation(example)
        all_conversations.append(transformed)
        current_batch.append(transformed)
        
        # Save batch when it reaches batch_size
        if len(current_batch) >= batch_size:
            save_conversations_batch(current_batch, batch_num, data_dir)
            batch_num += 1
            current_batch = []
        
        if (i + 1) % 100 == 0:
            print(f"Processed {i + 1:,} conversations...")
    
    # Save remaining conversations
    if current_batch:
        save_conversations_batch(current_batch, batch_num, data_dir)
    
    # Create metadata
    metadata = create_metadata(all_conversations, data_dir)
    
    print(f"\nTransformation complete!")
    print(f"Total conversations: {len(all_conversations):,}")
    print(f"Files saved in: {data_dir}")
    print(f"Average messages per conversation: {metadata['avg_messages_per_conversation']:.1f}")
    
    return all_conversations

if __name__ == "__main__":
    # Transform a sample of the dataset
    conversations = transform_dataset(sample_size=1000, batch_size=100)
    
    print(f"\nData structure:")
    print(f"- conversations_batch_XXXX.json: Conversation files")
    print(f"- metadata.json: Dataset statistics")
    print(f"- Each conversation has: id, model, language, messages, counts")
