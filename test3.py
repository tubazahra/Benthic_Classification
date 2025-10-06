import pandas as pd
from pathlib import Path

# 🔹 1. Define the folder containing your CSVs
csv_folder = Path("/Users/tuba/Downloads/UMB_Boston/lee/CORAL/CAH1609/")

# 🔹 2. Find only CSV files with 'acs' in the filename
csv_files = [f for f in csv_folder.rglob("*.csv") if "acs" in f.name.lower()]

print(f"Found {len(csv_files)} RRS CSV files")

# 🔹 3. Open the combined output file for writing
output_file = csv_folder / "combined_rrs.csv"

with open(output_file, "w") as outfile:
    for file in csv_files:
        try:
            # Write the filename as a header row
            outfile.write(f"{file.name}\n")

            # Read CSV as text (keep original header & data)
            with open(file, "r") as infile:
                outfile.write(infile.read())
                outfile.write("\n\n")  # add blank line for separation
            print(f"✅ Added {file.name}")
        except Exception as e:
            print(f"❌ Failed to process {file.name}: {e}")

print(f"\n🎯 Combined RRS CSV saved at: {output_file.resolve()}")
