from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

# Configuration identique à ton script
DB_PATH = "./chroma_db"
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)

# 1. Récupérer TOUTES les métadonnées de la base
all_data = vectorstore.get()
metadatas = all_data['metadatas']
documents = all_data['documents']

# 2. Compteur par extension
stats = {"pdf": 0, "csv": 0, "md": 0, "txt": 0}

print("🔎 ANALYSE DE LA BASE VECTORIELLE")
print("-" * 30)

for i, meta in enumerate(metadatas):
    source = meta.get('source', '').lower()
    if source.endswith('.pdf'): stats['pdf'] += 1
    elif source.endswith('.csv'): stats['csv'] += 1
    elif source.endswith('.md'): stats['md'] += 1
    elif source.endswith('.txt'): stats['txt'] += 1

for ext, count in stats.items():
    print(f"📄 Fichiers {ext.upper()} : {count} segments trouvés.")

# 3. Afficher un exemple de CSV (pour voir le formatage)
print("\n💡 Aperçu d'un segment CSV :")
for i, meta in enumerate(metadatas):
    if meta.get('source', '').lower().endswith('.csv'):
        print(f"Source: {meta['source']}")
        print(f"Contenu: {documents[i][:200]}...") # Affiche le début de la ligne
        break