from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):

    # ============================================================
    # APPLICATION
    # ============================================================

    app_name: str = "Enterprise HR Policy Agentic RAG Copilot"
    app_env: str = "development"


    # ============================================================
    # GROQ
    # ============================================================

    groq_api_key: str = ""
    groq_model: str = "llama-3.3-70b-versatile"


    # ============================================================
    # TAVILY
    # ============================================================

    tavily_api_key: str = ""


    # ============================================================
    # PINECONE
    # ============================================================

    pinecone_api_key: str = ""
    pinecone_index_name: str = "fde-hr-policy-rag"
    pinecone_namespace: str = "company-hr-kb"


    # ============================================================
    # EMBEDDINGS
    # ============================================================

    # Local Hugging Face embedding model.
    # all-MiniLM-L6-v2 produces 384-dimensional embeddings.
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"


    # ============================================================
    # RETRIEVAL
    # ============================================================

    top_k: int = 4
    max_retries: int = 1


    # ============================================================
    # SECURITY
    # ============================================================

    admin_api_key: str = "change-me-in-production"


    # ============================================================
    # DATABASE / FILE PATHS
    # ============================================================

    audit_db_path: str = str(
        BASE_DIR / "data" / "audit.db"
    )

    upload_dir: str = str(
        BASE_DIR / "uploads"
    )

    sample_kb_dir: str = str(
        BASE_DIR / "data" / "sample_kb"
    )


    # ============================================================
    # ENVIRONMENT CONFIGURATION
    # ============================================================

    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()

