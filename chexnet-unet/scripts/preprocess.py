import os
from PIL import Image
from tqdm import tqdm

# Dossiers
INPUT_DIR = '../data/clean_images'
OUTPUT_DIR = '../data/preprocessed_images'
IMAGE_SIZE = (224, 224)

# Créer le dossier de sortie s'il n'existe pas
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Lister les fichiers image
image_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

print(f"📦 Nombre d'images à prétraiter : {len(image_files)}")

# Boucle de traitement
for filename in tqdm(image_files, desc="🛠️ Prétraitement"):
    img_path = os.path.join(INPUT_DIR, filename)
    out_path = os.path.join(OUTPUT_DIR, filename)

    try:
        with Image.open(img_path) as img:
            img = img.convert("RGB")
            img = img.resize(IMAGE_SIZE)
            img.save(out_path)
    except Exception as e:
        print(f"❌ Erreur avec {filename} : {e}")

print("✅ Toutes les images ont été prétraitées et sauvegardées.")
