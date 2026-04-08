# GenAI books — combined workspace

Personal workspace with **one folder per book**. Each tree keeps its own `README.md`, `requirements.txt`, and license.

| Folder | Book | Upstream (reference) |
|--------|------|----------------------|
| `packt-agentic-architectural-patterns/` | *Agentic Architectural Patterns for Building Multi-Agent Systems* (Packt) | [Packt / your fork](https://github.com/jsagredoC/Agentic-Architectural-Patterns-for-Building-Multi-Agent-Systems) |
| `oreilly-genai-on-google-cloud/` | *GenAI on Google Cloud* (O’Reilly) | [ayoisio/genai-on-google-cloud](https://github.com/ayoisio/genai-on-google-cloud) |

## Setup

Use a **separate virtual environment per book** (dependency pins differ):

```bash
cd packt-agentic-architectural-patterns
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

```bash
cd oreilly-genai-on-google-cloud
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Do not commit `.env`, service account JSON, or `.venv`; see each book folder’s `.gitignore` and `.env.example`.
