# Load Environment Configuration (Stable Version)

import os
from dotenv import load_dotenv
from pathlib import Path

# Locate project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env file
env_path = BASE_DIR / ".env"

if not env_path.exists():
    raise FileNotFoundError(f".env file not found at: {env_path}")

load_dotenv(dotenv_path=env_path)

# Fetch variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Optional (only needed if using OpenRouter or other providers)
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", None)

# Safety check
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in .env file")

# Debug logs (safe)
print("API configuration loaded successfully.")

if OPENAI_BASE_URL:
    print(f"Using custom Base URL: {OPENAI_BASE_URL}")
else:
    print("Using default OpenAI endpoint")

print(f"Key loaded: {OPENAI_API_KEY[:10]}...")
