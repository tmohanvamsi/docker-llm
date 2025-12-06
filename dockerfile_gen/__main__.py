import os
import argparse
from .project_analyzer import analyze_project
from .ollama_client import generate_dockerfile_with_llm

def main():
    parser = argparse.ArgumentParser(description="Automate Dockerfile generation using local LLMs (Ollama)")
    parser.add_argument("project_path", nargs="?", default=".", help="Path to the project directory")
    parser.add_argument("--model", default="llama2", help="Ollama model to use")
    args = parser.parse_args()

    lang, deps = analyze_project(args.project_path)
    dockerfile_content = generate_dockerfile_with_llm(args.project_path, lang, deps, args.model)
    dockerfile_path = os.path.join(args.project_path, "Dockerfile")
    with open(dockerfile_path, "w") as f:
        f.write(dockerfile_content)
    print(f"Dockerfile generated at {dockerfile_path}")

if __name__ == "__main__":
    main()
