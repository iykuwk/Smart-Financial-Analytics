# config.py

from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data Folder
DATA_FOLDER = PROJECT_ROOT / "data"

# Random Seed
RANDOM_SEED = 42

# Date Range
START_DATE = "2025-01-01"
END_DATE = "2026-12-31"

# Number of Financial Transactions
NUM_TRANSACTIONS = 5000