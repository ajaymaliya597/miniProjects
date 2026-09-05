# One-command project launcher

From the `AI_Toolbox_Mini_Projects` root folder:

```bash
python3 run_project.py
```

Then select a number from **1 to 29**.

Example:

```text
Select project (1-29): 23
```

The launcher automatically:

1. Opens project 23.
2. Creates `23_faiss_vector_search/.venv` if needed.
3. Installs that project's `requirements.txt`.
4. Runs its `main.py`.
5. Keeps every project's dependencies isolated.

### Why not install all 29 at once?

Some packages are heavy or can have incompatible dependency versions. Installing on-demand keeps each mini-project independent.

### Codespaces

This launcher is designed for Linux-based GitHub Codespaces.

For projects requiring external services such as Kafka, Airflow, Ollama, or OCR engines, the launcher prints the extra setup note instead of pretending everything is self-contained.
