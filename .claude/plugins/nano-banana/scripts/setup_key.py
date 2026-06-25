import sys
import os
from utils import get_env_path

def save_key(api_key):
    env_path = get_env_path()
    os.makedirs(os.path.dirname(env_path), exist_ok=True)
    if not api_key.startswith("AIza"):
        print("[Nano Banana] Warning: Standard keys usually start with 'AIza'. Proceeding anyway...")
    with open(env_path, "w") as f:
        f.write(f"GEMINI_API_KEY={api_key}\n")
    print(f"[Nano Banana] API key saved to {env_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python setup_key.py YOUR_GEMINI_API_KEY")
        sys.exit(1)
    save_key(sys.argv[1])
