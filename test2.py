import sys
sys.path.append(r'/Users/tuba/Downloads/')

import pandas as pd
from pathlib import Path
from SB_support import readSB

# 1. Define the file path
filepath = Path("/Users/tuba/Downloads/UMB_Boston/lee/CORAL/CAH1609/archive/CAH1609_31001_Rrs.sb")

# 2. Read the file (using default optional arguments)
data = readSB(filename=str(filepath))  # convert Path to string

# 3. Convert data.data dictionary to a pandas DataFrame
df = pd.DataFrame(data.data)

# 4. Define the output path for the CSV file
output_csv_path = filepath.with_suffix(".csv")  # same path but .csv extension

# 5. Write the DataFrame to a CSV file
df.to_csv(output_csv_path, index=False)

print(f"Data written to CSV file at: {output_csv_path}")

sb_dir = Path("/Users/tuba/Downloads/UMB_Boston/lee/CORAL/")

# sub_dirs = list(sb_dir.iterdir())
# sub_dirs.pop(2)

sub_dirs = [Path(r'/Users/tuba/Downloads/UMB_Boston/lee/CORAL/CPA1705/')]

for dir in sub_dirs:
    sb_dir = dir / f"archive/"
    sb_files = sb_dir.glob("*.sb") 


    for sb_file in sb_files:
        print(f"Processing: {sb_file.name}")
        try:
            # Read .sb file
            data = readSB(filename=str(sb_file))

            # Convert data to DataFrame
            df = pd.DataFrame(data.data)

            # Define output CSV path
            csv_path = sb_file.with_suffix(".csv")
    # Write to CSV
            df.to_csv(csv_path, index=False)

            print(f"✅ Saved: {csv_path.name}")
        except Exception as e:
            print(f"❌ Failed to process {sb_file.name}: {e}")