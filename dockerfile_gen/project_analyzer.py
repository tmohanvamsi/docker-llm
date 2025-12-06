import os

def analyze_project(project_path):
    """
    Analyze the project directory to detect language and dependencies.
    Returns: (language, dependencies_str)
    """
    files = os.listdir(project_path)
    if 'requirements.txt' in files:
        lang = 'python'
        with open(os.path.join(project_path, 'requirements.txt')) as f:
            deps = f.read()
    elif 'package.json' in files:
        lang = 'nodejs'
        with open(os.path.join(project_path, 'package.json')) as f:
            deps = f.read()
    else:
        lang = 'unknown'
        deps = ''
    return lang, deps
