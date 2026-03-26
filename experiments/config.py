"""
Configuration for experiments.
Loads paths from .env file or uses defaults.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from experiments folder
load_dotenv(Path(__file__).parent / ".env")

# Data paths
DATA_ROOT = Path(os.getenv("DATA_ROOT", "../../data"))
SEPSIS_PATH = Path(os.getenv("SEPSIS_PATH", DATA_ROOT / "sepsis/Sepsis Cases - Event Log.xes"))
MIMIC_ED_PATH = Path(os.getenv("MIMIC_ED_PATH", DATA_ROOT / "mimic-iv-ed-demo-2.2/ed"))
SYNTHEA_PATH = Path(os.getenv("SYNTHEA_PATH", DATA_ROOT / "synthea_sample_data_csv_apr2020/csv"))

# Output paths (relative to project root)
PROJECT_ROOT = Path(__file__).parent.parent
FIGURES_PATH = PROJECT_ROOT / "figures"
RESULTS_PATH = PROJECT_ROOT / "results"

# Ensure output directories exist
FIGURES_PATH.mkdir(exist_ok=True)
RESULTS_PATH.mkdir(exist_ok=True)
