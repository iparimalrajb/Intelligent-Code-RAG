import os
import json
import shutil
from git import Repo

# -------- Clone GitHub Repo --------
def clone_repo(repo_url, local_dir="repo"):
    if os.path.exists(local_dir):
        shutil.rmtree(local_dir)
    Repo.clone_from(repo_url, local_dir)
    return local_dir


# -------- Read Code Files --------
def read_code_files(base_path):
    code = []

    for root, _, files in os.walk(base_path):
        for f in files:
            path = os.path.join(root, f)

            try:
                # Code files
                if f.endswith((".py", ".js", ".ts", ".java", ".cpp")):
                    with open(path, errors="ignore") as file:
                        code.append(file.read())

                # Jupyter notebooks
                elif f.endswith(".ipynb"):
                    with open(path, "r", encoding="utf-8") as file:
                        nb = json.load(file)
                        for cell in nb["cells"]:
                            if cell["cell_type"] == "code":
                                code.append("".join(cell["source"]))

                # Markdown
                elif f.endswith(".md"):
                    with open(path, errors="ignore") as file:
                        code.append(file.read())

            except Exception as e:
                print("Skipped file:", path)

    return "\n".join(code)