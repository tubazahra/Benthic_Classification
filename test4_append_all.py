from pathlib import Path
import pandas as pd

# 🔹 1. Define the folder containing your CSVs
csv_folder = Path("/Users/tuba/Downloads/UMB_Boston/lee/CORAL/CAL1609/")

# 🔹 2. Find only CSV files with 'rrs' in the filename (case-insensitive)
csv_files = [f for f in csv_folder.rglob("*.csv") if "rrs" in f.name.lower()]

print(f"Found {len(csv_files)} RRS CSV files")

# 🔹 3. Define combined output file path
output_file = csv_folder / "combined_rrs.csv"

# 🔹 4. Read all CSVs and combine into a single DataFrame
all_data = []

for file in csv_files:
    try:
        df = pd.read_csv(file)
        
        # Add a column with the filename for identification
        df.insert(0, 'source_file', file.stem)
        
        all_data.append(df)
        print(f"✅ Loaded {file.name}")
        
    except Exception as e:
        print(f"❌ Failed to process {file.name}: {e}")

# 🔹 5. Concatenate all DataFrames into one
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    
    # 🔹 6. Write the combined DataFrame to CSV (single write operation)
    combined_df.to_csv(output_file, index=False)
    
    print(f"\n🎯 Combined RRS CSV saved at: {output_file.resolve()}")
    print(f"📊 Total rows: {len(combined_df)}")
else:
    print("⚠️ No data to combine")