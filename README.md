# Measuring Prompt Energy in LLMs

Fast and easy analysis of 1M+ chat conversations for LLM research

## Quick Start (2 minutes)

### 1. Install
```bash
pip install -r requirements.txt
```

### 2. Download & Explore
```bash
python download.py    # Fast download with progress bar
python sample.py      # See sample data instantly
```

The download script will ask for your Hugging Face token if needed.

## What You Get

- **100K+ conversations** from top LLMs (GPT-4, Claude, Llama, etc.)
- **Multiple languages** (English, Spanish, French, etc.)
- **Ready-to-use JSON** format in `data/` folder
- **Instant analysis** with sample.py

## System Requirements

- **RAM**: 4GB+ (8GB recommended)
- **Storage**: 1GB free space
- **Python**: 3.8+
- **Internet**: Fast connection for download

## Usage Examples

```python
# Load your data
import json
with open('data/conversations.json', 'r') as f:
    conversations = json.load(f)

# Analyze models
models = [conv['model'] for conv in conversations]
print(f"Found {len(set(models))} different models!")
```

## Files

- `download.py` - Super fast download with progress bar
- `sample.py` - Instant data exploration
- `data/` - Your processed dataset (auto-created)

## Security

- Tokens protected in `.env` (git-ignored)
- No personal data in repository
- Clean, secure setup

---

Ready to analyze 100K+ conversations? Run `python download.py` and start exploring!