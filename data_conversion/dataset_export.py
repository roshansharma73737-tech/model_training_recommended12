import zipfile
from pathlib import Path
import warnings

import pandas as pd
import requests 
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Ignore the expired SSL warning only for this educational download
warnings.filterwarnings('ignore', category=InsecureRequestWarning)

# -------------------------------
# 1. Set project folders
# -------------------------------
project_root = Path(__file__).resolve().parent.parent
data_dir = project_root / 'data'
data_dir.mkdir(exist_ok=True)

zip_dir = data_dir / 'downloaded_dataset'
zip_dir.mkdir(exist_ok=True)

# -------------------------------
# 2. Download the ZIP file
# -------------------------------
url = 'https://files.grouplens.org/datasets/movielens/ml-1m.zip'
zip_path = zip_dir / 'ml-1m.zip'

response = requests.get(url, verify=False, timeout=60)
response.raise_for_status()

with open(zip_path, 'wb') as f:
    f.write(response.content)

# -------------------------------
# 3. Extract ZIP file
# -------------------------------
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(zip_dir)

# -------------------------------
# 4. Read the raw data file inside ZIP
# -------------------------------
# The dataset inside is typically 'ml-1m/u.data'
raw_file = zip_dir / 'ml-1m' / 'ratings.dat'

if not raw_file.exists():
    raise FileNotFoundError(f'Could not find raw data file: {raw_file}')

columns = ['user_id', 'item_id', 'rating', 'timestamp']
raw = pd.read_csv(raw_file, sep='\t', names=columns)

# -------------------------------
# 5. Save converted CSV
# -------------------------------
output_csv = data_dir / 'dataset.csv'
raw.to_csv(output_csv, index=False)

print('Dataset downloaded and extracted successfully.')
print(raw.head())
print(f'Saved file: {output_csv}')