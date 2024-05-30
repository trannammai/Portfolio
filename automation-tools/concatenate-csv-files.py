import pandas as pd
from pathlib import Path

folder_path = r'C:\Python\data'

# Get a list of all CSV files in the folder
csv_files = list(Path(folder_path).glob('*.csv'))

df_list = []

for csv in csv_files:
    try:
        # Try reading the file using default UTF-8 encoding
        with open(csv, 'r', encoding='utf-8') as file:
            df = pd.read_csv(file)
            df_list.append(df)
    except UnicodeDecodeError:
        try:
            with open(csv, 'r', encoding='utf-16') as file:
                df = pd.read_csv(file, sep='\t')
                df_list.append(df)
        except Exception as e:
            print(f"Could not read file {csv} because of error: {e}")
    except Exception as e:
        print(f"Could not read file {csv} because of error: {e}")

# Concatenate all data into one DataFrame
try:
    big_df = pd.concat(df_list, ignore_index=True)
except Exception as e:
    print(f"Could not concatenate dataframes because of error: {e}")

# Save the final result to a new CSV file
output_file = Path(folder_path) / 'combined_file.csv'
try:
    big_df.to_csv(output_file, index=False)
except Exception as e:
    print(f"Could not save the final result to {output_file} because of error: {e}")
