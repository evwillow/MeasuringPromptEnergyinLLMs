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
│   ├── raw_conversations.jsonl    # Raw conversation data from LMSYS
│   ├── clean_prompts.jsonl         # Extracted and cleaned prompts
│   └── energy_measurements.jsonl          # Energy consumption measurements
├── 01_data_collection.ipynb      # Download LMSYS dataset
├── 02_data_cleaning.ipynb        # Extract and clean prompts
├── 03_energy_measurement.ipynb   # Measure energy consumption
├── 04_feature_engineering.ipynb  # Comprehensive feature engineering
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
- **Output**: `data/raw_conversations.jsonl` - Raw conversation data
- **Features**:
  - Streams data to avoid memory issues
  - Progress tracking with visual indicators
  - Configurable sample size and parameters

**Key Configuration**:
```python
samples = 1_000_000
output_path = Path("data/raw_conversations.jsonl")
split = "train"
progress_every = 50_000
```

### Data Cleaning (`02_data_cleaning.ipynb`)

This notebook extracts and cleans user prompts from conversation data:

- **Input**: `data/raw_conversations.jsonl` - Raw conversation data
- **Output**: `data/clean_prompts.jsonl` - Cleaned prompts with metadata
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

### Feature Engineering (`04_feature_engineering.ipynb`)

This notebook creates comprehensive linguistic and semantic features from prompt text:

**Text Complexity Features:**
- `syntactic_tree_depth` - Maximum depth of syntactic parse tree
- `clause_count` - Number of clause markers and conjunctions
- `flesch_kincaid_grade` - Readability grade level
- `gunning_fog_index` - Text complexity index
- `smog_index` - Simplified Measure of Gobbledygook

**Lexical Features:**
- `avg_word_frequency` - Average frequency of words in English
- `lexical_diversity` - Diversity of vocabulary (sqrt normalization)
- `type_token_ratio` - Ratio of unique words to total words
- `vocabulary_richness` - Richness of vocabulary usage

**Semantic Features:**
- `named_entity_density` - Density of named entities (persons, places, organizations)
- `semantic_category_diversity` - Diversity of part-of-speech categories

**Sentiment Features:**
- `sentiment_polarity` - Overall sentiment score (-1 to 1)
- `sentiment_intensity` - Intensity of sentiment expression

**Information Content:**
- `information_density` - Ratio of content words to total words
- `avg_sentence_length_prompt` - Average words per sentence

**Topic Keyword Density (8 categories):**
- `tech_ai_density` - Technology and AI-related keywords
- `business_finance_density` - Business and finance keywords
- `health_medical_density` - Health and medical keywords
- `education_learning_density` - Education and learning keywords
- `science_research_density` - Science and research keywords
- `social_relationships_density` - Social and relationship keywords
- `entertainment_culture_density` - Entertainment and culture keywords
- `travel_lifestyle_density` - Travel and lifestyle keywords

**Concept Density (6 categories):**
- `abstract_thinking_density` - Abstract and philosophical concepts
- `problem_solving_density` - Problem-solving and analytical concepts
- `communication_density` - Communication and language concepts
- `emotional_psychological_density` - Emotional and psychological concepts
- `decision_making_density` - Decision-making and choice concepts
- `time_change_density` - Time, change, and temporal concepts

**Output**: `energy_features_dataset.jsonl` - Dataset with all engineered features

### Analysis Notebooks (Coming Soon)

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

### Prompts Data (`clean_prompts.jsonl`)
```json
{
  "prompt_text": "How can I improve my productivity?",
  "processed": 0
}
```

### Energy Data (`energy_measurements.jsonl`)
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

### Feature Engineering Data (`energy_features_dataset.jsonl`)
```json
{
  "prompt": "How can I improve my productivity?",
  "model": "gpt-4o-mini-2024-07-18",
  "timestamp": "2025-01-19 20:18:09",
  "duration": 2.03,
  "energy_consumed_wh": 0.015,
  "syntactic_tree_depth": 3,
  "clause_count": 2,
  "flesch_kincaid_grade": 8.2,
  "gunning_fog_index": 10.1,
  "smog_index": 7.5,
  "avg_word_frequency": 0.0003,
  "lexical_diversity": 0.85,
  "type_token_ratio": 0.78,
  "vocabulary_richness": 0.82,
  "named_entity_density": 0.05,
  "semantic_category_diversity": 6,
  "sentiment_polarity": 0.2,
  "sentiment_intensity": 0.3,
  "information_density": 0.75,
  "avg_sentence_length_prompt": 12.5,
  "tech_ai_density": 0.02,
  "business_finance_density": 0.15,
  "health_medical_density": 0.01,
  "education_learning_density": 0.08,
  "science_research_density": 0.03,
  "social_relationships_density": 0.05,
  "entertainment_culture_density": 0.01,
  "travel_lifestyle_density": 0.02,
  "abstract_thinking_density": 0.12,
  "problem_solving_density": 0.18,
  "communication_density": 0.25,
  "emotional_psychological_density": 0.08,
  "decision_making_density": 0.15,
  "time_change_density": 0.10
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
- Check `processed` status in `clean_prompts.jsonl` to see completion

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

### Version 2.1.0
- **Comprehensive feature engineering** with 30+ linguistic and semantic features
- **Topic keyword density** analysis across 8 major categories
- **Concept density** analysis across 6 cognitive categories
- **Advanced text analysis** including sentiment, readability, and complexity metrics
- **Enhanced data processing** with spaCy, NLTK, and textstat libraries

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