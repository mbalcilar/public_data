# ============================================================
# Convert all STATA and SAS dataset files to CSV
#
# Features:
# - Detects extensions case-insensitively
#   (.dta, .DTA, .sas7bdat, .SAS7BDAT)
# - Reads files from current directory
# - Writes output CSV filenames in lowercase
# ============================================================

from pathlib import Path
import pandas as pd

# ------------------------------------------------------------
# Current working directory
# ------------------------------------------------------------
current_dir = Path.cwd()

# ------------------------------------------------------------
# Get all files in current directory
# ------------------------------------------------------------
all_files = list(current_dir.iterdir())

# ------------------------------------------------------------
# 1. Process STATA files (.dta / .DTA)
# ------------------------------------------------------------
stata_files = [
    f for f in all_files
    if f.is_file() and f.suffix.lower() == ".dta"
]

if len(stata_files) == 0:
    print("No STATA files found.\n")
else:
    print(f"Found {len(stata_files)} STATA file(s).\n")

for file in stata_files:
    try:
        print(f"Reading STATA file: {file.name}")

        # Read STATA file
        df = pd.read_stata(file)

        # Output CSV name in lowercase
        csv_name = file.stem.lower() + ".csv"
        csv_path = current_dir / csv_name

        # Save CSV
        df.to_csv(csv_path, index=False)

        print(f"Saved CSV: {csv_name}\n")

    except Exception as e:
        print(f"Error processing {file.name}: {e}\n")


# ------------------------------------------------------------
# 2. Process SAS dataset files
#    (.sas7bdat / .SAS7BDAT)
# ------------------------------------------------------------
sas_files = [
    f for f in all_files
    if f.is_file() and f.suffix.lower() == ".sas7bdat"
]

if len(sas_files) == 0:
    print("No SAS dataset files found.\n")
else:
    print(f"Found {len(sas_files)} SAS dataset file(s).\n")

for file in sas_files:
    try:
        print(f"Reading SAS dataset file: {file.name}")

        # Read SAS dataset
        df = pd.read_sas(file)

        # Output CSV name in lowercase
        csv_name = file.stem.lower() + ".csv"
        csv_path = current_dir / csv_name

        # Save CSV
        df.to_csv(csv_path, index=False)

        print(f"Saved CSV: {csv_name}\n")

    except Exception as e:
        print(f"Error processing {file.name}: {e}\n")


print("Conversion process completed.")

