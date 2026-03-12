import os
import subprocess

REPO_URL = "https://github.com/PhonePe/pulse.git"
DATA_DIR = "pulse-data"

def ensure_dataset():
    if not os.path.exists(DATA_DIR):
        print("Cloning PhonePe Pulse dataset...")
        subprocess.run(
            ["git", "clone", "--depth", "1", REPO_URL, DATA_DIR],
            check=True
        )
        print("Dataset downloaded")
    else:
        print("Dataset already exists")

ensure_dataset()