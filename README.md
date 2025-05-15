# Agentic AI Workflow with OpenRouter

This repository contains code examples for building agentic AI workflows using OpenRouter API, which provides access to multiple AI models (OpenAI, Anthropic, Google, etc.) through a single, consistent interface.

## Features

- Access models from multiple providers through one unified API
- Compare responses from different AI models
- Build multi-step reasoning agents that break down complex tasks
- Example workflow for research and recommendation tasks

## Prerequisites

- Python 3.8 or higher
- OpenRouter account (sign up at [openrouter.ai](https://openrouter.ai))

## Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/agentic-ai-workflow
cd agentic-ai-workflow
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your API keys:
```
OPENROUTER_API_KEY=your_openrouter_api_key_here
YOUR_SITE_URL=https://yourdomain.com
YOUR_SITE_NAME=Your App Name
```

## Usage

### Basic Connection Test

Test your OpenRouter API connection:
```bash
python basic_setup.py
```

### Compare AI Models

Compare responses from different AI models:
```bash
python model_comparison.py
```

### Run Agentic Workflow

Execute a multi-step reasoning workflow:
```bash
python agent_example.py
```

## Project Structure

- `basic_setup.py` - Basic OpenRouter API client setup
- `model_comparison.py` - Compare responses from different models
- `agent_example.py` - Complete agentic workflow implementation
- `requirements.txt` - Project dependencies

## Next Steps

- Add vector database for long-term memory
- Enable external tools (web search, calculators, etc.)
- Implement model routing for cost optimization
- Add retry logic and better error handling
- Implement user feedback loops

## Resources

For a detailed tutorial on building agentic AI workflows with OpenRouter API, check out the article:
- [Building Your First Agentic AI Workflow with OpenRouter API](https://dev.to/allanninal/building-your-first-agentic-ai-workflow-with-openrouter-api-1fo6) by Allan Niñal

## License

[MIT](LICENSE) 