import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

packages = [
    "torch",
    "nltk",
    "transformers",
    "scikit-learn",
    "numpy",
    "pandas"
]

# Optional: upgrade pip first
install("pip --upgrade")

for package in packages:
    try:
        install(package)
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package}: {e}")

# Download NLTK data (Punkt tokenizer)
import nltk
nltk.download("punkt")
