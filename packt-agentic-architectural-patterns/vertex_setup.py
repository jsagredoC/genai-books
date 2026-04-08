"""Shared notebook setup: Vertex AI + Application Default Credentials (ADC).

google-genai (used by ADK) switches to Vertex when GOOGLE_GENAI_USE_VERTEXAI is set
and GOOGLE_CLOUD_PROJECT / GOOGLE_CLOUD_LOCATION are present; API keys must not
compete with ADC. See: https://cloud.google.com/docs/authentication/provide-credentials-adc
"""

from __future__ import annotations

import os
from pathlib import Path


def _find_repo_root() -> Path:
    cwd = Path.cwd().resolve()
    for p in [cwd, *cwd.parents]:
        if (p / "vertex_setup.py").is_file():
            return p
    raise FileNotFoundError(
        "vertex_setup.py not found from the current working directory; "
        "open notebooks from inside the cloned repository (or a Chapter_* subfolder)."
    )


def _load_dotenv() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    env = _find_repo_root() / ".env"
    if env.is_file():
        load_dotenv(env)


def configure_vertex_for_book(*, verify_adc: bool = True) -> None:
    """Configure os.environ for Vertex-backed Gemini (ADK, CrewAI, LangChain)."""
    _load_dotenv()
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "true"
    for k in ("GOOGLE_API_KEY", "GEMINI_API_KEY"):
        os.environ.pop(k, None)

    project = os.environ.get("GOOGLE_CLOUD_PROJECT", "").strip()
    location = os.environ.get("GOOGLE_CLOUD_LOCATION", "").strip()
    if not project or not location:
        raise RuntimeError(
            "Set GOOGLE_CLOUD_PROJECT and GOOGLE_CLOUD_LOCATION "
            "(see repo .env.example and your GCP project's Vertex region)."
        )

    if verify_adc:
        import google.auth

        try:
            creds, _ = google.auth.default(
                scopes=["https://www.googleapis.com/auth/cloud-platform"]
            )
        except Exception as e:
            raise RuntimeError(
                "Application Default Credentials failed. On a dev machine run: "
                "gcloud auth application-default login"
            ) from e
        if creds is None:
            raise RuntimeError("google.auth.default() returned no credentials.")

    print(f"Vertex AI: project={project} location={location} (ADC)")


def default_gemini_model_id() -> str:
    """Vertex model id for Generative AI on Vertex (override with GEMINI_VERTEX_MODEL)."""
    return os.environ.get("GEMINI_VERTEX_MODEL", "gemini-2.5-flash").strip()
