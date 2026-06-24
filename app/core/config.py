# app/core/config.py

from dotenv import load_dotenv
import os

load_dotenv()


class Settings: 

    APP_NAME = os.getenv("APP_NAME", "Fliqz AI Support")
    APP_ENV = os.getenv("APP_ENV", "development")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))

    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "myvault")

    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    REDIS_DB = int(os.getenv("REDIS_DB", 0))

    REDIS_CHAT_STREAM = os.getenv(
        "REDIS_CHAT_STREAM",
        "chat_stream"
    )

    REDIS_CONSUMER_GROUP = os.getenv(
        "REDIS_CONSUMER_GROUP",
        "chat_workers"
    )

    REDIS_CONSUMER_NAME = os.getenv(
        "REDIS_CONSUMER_NAME",
        "worker_1"
    )

    CHROMA_DB_PATH = os.getenv(
        "CHROMA_DB_PATH",
        "./data/chroma"
    )

    CHROMA_COLLECTION = os.getenv(
        "CHROMA_COLLECTION",
        "support_docs"
    )

    OLLAMA_BASE_URL = os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434"
    )

    OLLAMA_MODEL = os.getenv(
        "OLLAMA_MODEL",
        "llama3.1:8b"
    )

    OLLAMA_EMBED_MODEL = os.getenv(
        "OLLAMA_EMBED_MODEL",
        "nomic-embed-text"
    )

    SHORT_TERM_MEMORY_LIMIT = int(
        os.getenv("SHORT_TERM_MEMORY_LIMIT", 10)
    )

    MEMORY_SUMMARY_THRESHOLD = int(
        os.getenv("MEMORY_SUMMARY_THRESHOLD", 20)
    )

    RAG_TOP_K = int(
        os.getenv("RAG_TOP_K", 5)
    )

    RAG_SCORE_THRESHOLD = float(
        os.getenv("RAG_SCORE_THRESHOLD", 0.7)
    )

    CHUNK_SIZE = int(
        os.getenv("CHUNK_SIZE", 500)
    )

    CHUNK_OVERLAP = int(
        os.getenv("CHUNK_OVERLAP", 50)
    )

    MAX_INPUT_TOKENS = int(
        os.getenv("MAX_INPUT_TOKENS", 4096)
    )

    MAX_OUTPUT_TOKENS = int(
        os.getenv("MAX_OUTPUT_TOKENS", 512)
    )

    API_SECRET_KEY = os.getenv(
        "API_SECRET_KEY",
        "change_this_secret_key"
    )

    JWT_ALGORITHM = os.getenv(
        "JWT_ALGORITHM",
        "HS256"
    )

    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 10080)
    )

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )


settings = Settings()