# Measuring Prompt Energy in LLMs

Research project analyzing prompt energy in Large Language Models using the lmsys-chat-1m dataset.

## Quick Start

1. **Setup environment:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Authenticate with Hugging Face:**
   - Get a token from [Hugging Face Settings](https://huggingface.co/settings/tokens)
   - Set environment variable: `$env:HUGGINGFACE_HUB_TOKEN = "your_token_here"`

3. **Download dataset:**
   ```bash
   python download_dataset.py
   ```

4. **Explore dataset:**
   ```bash
   python explore_dataset.py
   ```

## Dataset

- **Source**: [lmsys-chat-1m](https://huggingface.co/datasets/lmsys/lmsys-chat-1m)
- **Size**: 1 million chat conversations
- **Format**: Apache Arrow (`.arrow` files)
- **Location**: `lmsys-chat-1m/` (excluded from git)

## Usage

```python
from datasets import load_from_disk

# Load dataset
dataset = load_from_disk("lmsys-chat-1m")

# Access data
print(f"Total examples: {len(dataset['train'])}")
example = dataset['train'][0]
print(f"Model: {example['model']}")
print(f"Conversation: {example['conversation']}")
```

## Files

- `download_dataset.py` - Download the dataset
- `explore_dataset.py` - Explore dataset structure and content
- `requirements.txt` - Python dependencies

## Security

- Personal tokens and cache files are excluded from git
- Dataset folder is excluded from version control
- No personal information is stored in the repository