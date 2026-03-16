#  Load Environment Configuration (OpenRouter Compatible - Stable Version)

import os
from dotenv import load_dotenv
from pathlib import Path

# Locate project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Explicitly load .env file
env_path = BASE_DIR / ".env"

if not env_path.exists():
    raise FileNotFoundError(f".env file not found at: {env_path}")

load_dotenv(dotenv_path=env_path)

# Fetch variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")

# Safety checks
if not OPENAI_API_KEY:
    raise ValueError(" OPENAI_API_KEY is not set in .env file")

if not OPENAI_BASE_URL:
    raise ValueError(" OPENAI_BASE_URL is not set in .env file")

# Optional debug (safe)
print(" API configuration loaded successfully.")
print(f" Base URL: {OPENAI_BASE_URL}")
print(f" Key loaded: {OPENAI_API_KEY[:10]}...")
