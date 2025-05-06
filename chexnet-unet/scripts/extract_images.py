import os
import tarfile

input_dir = "../data/images"

for filename in os.listdir(input_dir):
    if filename.endswith(".tar.gz"):
        file_path = os.path.join(input_dir, filename)
        print(f"🔄 Extraction de {filename}...")

        try:
            with tarfile.open(file_path, 'r:gz') as tar:
                for member in tar.getmembers():
                    try:
                        tar.extract(member, path=input_dir)
                    except Exception as e:
                        print(f"❌ Erreur lors de l'extraction de {member.name} : {e}")
        except Exception as e:
            print(f"⚠️ Impossible d’ouvrir {filename} : {e}")
        else:
            print(f"✅ {filename} extrait avec succès.")
            # Supprimer le fichier une fois extrait si tu veux économiser de l'espace disque :
            # os.remove(file_path)

print("\n🎉 Tous les fichiers traités.")

