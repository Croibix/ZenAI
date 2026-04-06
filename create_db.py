from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

print("1. Lecture du RAG")
loader = TextLoader("RAG.txt", encoding="utf-8")
docs = loader.load()

print("2. Découpage du texte chunks")
# On découpe par blocs de 600 caractères, avec un chevauchement de 100 caractères pour ne pas couper une idée en deux.
text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=100)
splits = text_splitter.split_documents(docs)

print("3. Vectorisation et création de la base de données ChromaDB")
# On utilise le même modèle d'embedding que dans agent_cyber.py
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Cette commande crée les vecteurs et les sauvegarde dans le dossier local
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings, persist_directory="./chroma_db")

print(f"\n✅ Terminé ! La base de données contient désormais {len(splits)} segments.")
print("Le dossier './chroma_db' a été créé. Vous pouvez maintenant lancer agent_cyber.py !")