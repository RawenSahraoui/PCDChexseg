import os
import pandas as pd
from shutil import move

# Chemins
CSV_PATH = '../data/Data_Entry_2017_v2020.csv'
IMAGES_DIR = '../data/images'
VALID_DIR = '../data/clean_images'
INVALID_DIR = '../data/invalid_images'

# Créer les dossiers de sortie
os.makedirs(VALID_DIR, exist_ok=True)
os.makedirs(INVALID_DIR, exist_ok=True)

# Charger le CSV
df = pd.read_csv(CSV_PATH)

# Liste des images valides
valid_images = set(df['Image Index'].values)

# Liste réelle des fichiers
all_files = os.listdir(IMAGES_DIR)

for filename in all_files:
    if filename.endswith('.png') or filename.endswith('.jpg'):
        src_path = os.path.join(IMAGES_DIR, filename)

        if filename in valid_images:
            move(src_path, os.path.join(VALID_DIR, filename))
        else:
            move(src_path, os.path.join(INVALID_DIR, filename))

print(f"✅ Nettoyage terminé. {len(valid_images)} images valides détectées.")
