import requests
import os

def generate_dockerfile_with_llm(project_path, lang, deps, model="llama2"):
    """
    Send prompt to Ollama LLM and return Dockerfile content.
    """
    prompt = f"Generate a Dockerfile for a {lang} project with these dependencies:\n{deps}\nProject files: {os.listdir(project_path)}"
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt},
        stream=True
    )
    response.raise_for_status()
    dockerfile_content = ""
    for line in response.iter_lines():
        if line:
            try:
                data = requests.utils.json.loads(line)
                dockerfile_content += data.get('response', '')
            except Exception:
                continue
    return dockerfile_content
