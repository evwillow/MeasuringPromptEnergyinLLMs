# Measuring Prompt Energy in LLMs

A comprehensive research toolkit for analyzing energy consumption patterns across different Large Language Models (LLMs). This project measures and compares the energy efficiency of various AI models when processing different types of prompts.

## Overview

This research project provides tools to:
- Download and process large conversation datasets
- Extract and clean prompts from conversations
- Measure energy consumption of different LLM models
- Perform feature engineering and exploratory analysis
- Conduct statistical analysis and generate insights

## Project Structure

```
MeasuringPromptEnergyinLLMs/
├── data/
│   ├── conversations.jsonl    # Raw conversation data from LMSYS
│   ├── prompts.jsonl         # Extracted and cleaned prompts
│   └── energy.jsonl          # Energy consumption measurements
├── 01_data_collection.ipynb      # Download LMSYS dataset
├── 02_data_cleaning.ipynb        # Extract and clean prompts
├── 03_energy_measurement.ipynb   # Measure energy consumption
├── 04_feature_engineering.ipynb  # Feature engineering (placeholder)
├── 05_exploratory_data_analysis.ipynb  # EDA (placeholder)
├── 06_statistical_analysis.ipynb       # Statistical analysis (placeholder)
└── requirements.txt           # Python dependencies
```

## Quick Start

### 1. Setup Environment

```bash
# Clone the repository
git clone <repository-url>
cd MeasuringPromptEnergyinLLMs

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

### 2. Configure API Keys

Create a `.env` file with your API credentials:

```env
HUGGINGFACE_HUB_TOKEN=your_hf_token_here
OPENAI_API_KEY=your_openai_key_here
GROQ_API_KEY=your_groq_key_here
MISTRAL_API_KEY=your_mistral_key_here
```

### 3. Run the Pipeline

**Step 1: Data Collection**
```bash
# Run the data collection notebook
jupyter notebook 01_data_collection.ipynb
# Execute all cells to download LMSYS dataset
```

**Step 2: Data Cleaning**
```bash
# Run the data cleaning notebook
jupyter notebook 02_data_cleaning.ipynb
# Execute all cells to extract prompts from conversations
```

**Step 3: Energy Measurement**
```bash
# Run the energy measurement notebook
jupyter notebook 03_energy_measurement.ipynb
# Execute all cells to start energy measurements
```

**Step 4: Analysis (Coming Soon)**
```bash
# Run the analysis notebooks
jupyter notebook 04_feature_engineering.ipynb
jupyter notebook 05_exploratory_data_analysis.ipynb
jupyter notebook 06_statistical_analysis.ipynb
```

## Detailed Usage

### Data Collection (`01_data_collection.ipynb`)

This notebook downloads the LMSYS Chat 1M dataset:

- **Source**: Hugging Face `lmsys/lmsys-chat-1m` dataset
- **Output**: `data/conversations.jsonl` - Raw conversation data
- **Features**:
  - Streams data to avoid memory issues
  - Progress tracking with visual indicators
  - Configurable sample size and parameters

**Key Configuration**:
```python
samples = 1_000_000
output_path = Path("data/conversations.jsonl")
split = "train"
progress_every = 50_000
```

### Data Cleaning (`02_data_cleaning.ipynb`)

This notebook extracts and cleans user prompts from conversation data:

- **Input**: `data/conversations.jsonl` - Raw conversation data
- **Output**: `data/prompts.jsonl` - Cleaned prompts with metadata
- **Features**:
  - Filters for English conversations only
  - Validates prompt quality (length, uniqueness, content)
  - Generates prompt statistics and visualizations

**Key Configuration**:
```python
config = {
    'min_words': 5,
    'max_words': 500,
    'min_chars': 20,
    'max_chars': 3000,
    'min_unique_ratio': 0.3
}
```

### Energy Measurement (`03_energy_measurement.ipynb`)

This notebook measures energy consumption across different LLM models:

- **Supported Models**: OpenAI GPT-4o-mini, Groq Llama-3.1-8b, Mistral Large
- **Metrics Tracked**:
  - Energy consumption (Wh)
  - Processing time and speed
  - Token usage and efficiency
  - Response quality metrics

**Key Features**:
- Incremental processing with resume capability
- Real-time progress tracking
- Automatic error handling and retry logic
- Batch result saving

### Analysis Notebooks (Coming Soon)

- **Feature Engineering** (`04_feature_engineering.ipynb`): Create derived features from raw data
- **Exploratory Data Analysis** (`05_exploratory_data_analysis.ipynb`): Visualize patterns and relationships
- **Statistical Analysis** (`06_statistical_analysis.ipynb`): Conduct hypothesis tests and statistical modeling

## Configuration Options

### Model Configuration

The energy measurement supports multiple models with different configurations:

```python
# OpenAI Configuration
model: "gpt-4o-mini"
max_tokens: 50
temperature: 0.3

# Groq Configuration  
model: "llama-3.1-8b-instant"
max_tokens: 50
temperature: 0.3

# Mistral Configuration
model: "mistral-large-latest"
max_tokens: 50
temperature: 0.3
```

### Data Processing Options

```python
# Prompt filtering criteria
min_words = 5
max_words = 500
min_chars = 20
max_chars = 3000
min_unique_ratio = 0.3

# Energy measurement settings
max_tokens = 50
temperature = 0.3
```

## Output Data Format

### Prompts Data (`prompts.jsonl`)
```json
{
  "prompt_text": "How can I improve my productivity?",
  "processed": 0
}
```

### Energy Data (`energy.jsonl`)
```json
{
  "prompt": "How can I improve my productivity?",
  "model": "gpt-4o-mini-2024-07-18",
  "timestamp": "2025-01-19 20:18:09",
  "duration": 2.03,
  "time_to_first_token": 2.029,
  "prompt_tokens": 18,
  "completion_tokens": 50,
  "total_tokens": 68,
  "tokens_per_second": 33.5,
  "energy_consumed_wh": 0.015,
  "response": "Here are several strategies to improve productivity..."
}
```

## Key Metrics Explained

- **Energy Consumption (Wh)**: Total energy used per request
- **Duration**: Total processing time in seconds
- **Time to First Token**: Latency before response starts
- **Tokens per Second**: Processing throughput
- **Energy per Token**: Efficiency metric (lower is better)
- **Energy per Character**: Character-level efficiency

## Troubleshooting

### Common Issues

**API Rate Limits**
- The system automatically handles rate limits with retry logic
- Consider adjusting processing speed for different APIs

**Memory Issues with Large Datasets**
- The system processes data incrementally to avoid memory issues
- Large conversation files are processed line-by-line

**Incomplete Processing**
- The system tracks progress and can resume from interruptions
- Check `processed` status in `prompts.jsonl` to see completion

### Performance Optimization

**For Large Datasets**:
- Process in smaller batches if needed
- Monitor API usage and costs
- Use incremental processing for very large datasets

**For Faster Processing**:
- Adjust `max_tokens` parameter for shorter responses
- Consider parallel processing for multiple models
- Optimize prompt filtering criteria

## Research Applications

This toolkit is designed for:

- **Academic Research**: Energy efficiency studies, model comparisons
- **Industry Analysis**: Cost optimization, performance benchmarking
- **Environmental Impact**: Carbon footprint analysis of AI systems
- **Model Development**: Efficiency improvements and optimization

## Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Citation

If you use this toolkit in your research, please cite:

```bibtex
@software{llm_energy_measurement,
  title={Measuring Prompt Energy in LLMs},
  author={Your Name},
  year={2025},
  url={https://github.com/your-repo/MeasuringPromptEnergyinLLMs}
}
```

## Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Check the documentation in each notebook
- Review the configuration options above

## Changelog

### Version 2.0.0
- **Restructured project** with numbered notebooks following data science workflow
- **Added data collection** step for downloading LMSYS dataset
- **Improved organization** with clear separation of concerns
- **Enhanced documentation** with step-by-step instructions
- **Added placeholder notebooks** for feature engineering, EDA, and statistical analysis

### Version 1.0.0
- Initial release with core functionality
- Support for OpenAI, Groq, and Mistral APIs
- Comprehensive analysis and visualization tools
- Incremental processing with resume capability