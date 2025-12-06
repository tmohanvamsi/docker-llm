# Dockerfile Generation Automation with Local LLMs (Ollama)

## Overview
This tool uses a locally hosted Large Language Model (LLM) via Ollama to automatically generate Dockerfiles for any project. It analyzes your project and sends the details to the LLM, which returns a tailored Dockerfile.

## Features
- Analyze project structure and dependencies
- Use Ollama (local LLM) to generate Dockerfile
- CLI interface for easy use

## Setup
1. **Install Python (if not already installed):**
   - On macOS, you can use Homebrew:
     ```sh
     brew install python
     ```
   - Or download from the official site: https://www.python.org/downloads/

2. **Verify Python installation:**
   ```sh
   python3 --version
   ```
   If you see a version (e.g., Python 3.11.x), you're good to go.

3. **Install [Ollama](https://ollama.com/) and run a model (e.g., `ollama run llama2`).**

4. **Install Python dependencies:**
   ```sh
   pip3 install -r dockerfile_gen/requirements.txt
   ```

5. **Run the CLI tool:**
   ```sh
   python3 -m dockerfile_gen <project_path> --model <model_name>
   ```
   Example:
   ```sh
   python3 -m dockerfile_gen . --model llama2
   ```

## What You'll Learn
- Automate Dockerfile creation for any tech stack
- Use local LLMs for code generation
- Integrate AI-driven automation into CI/CD workflows
