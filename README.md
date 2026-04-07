# 🛡️ Agent SOC IA (ZanAI) - Analyse de Logs & RAG Local

Ce projet est un agent d'intelligence artificielle spécialisé en cybersécurité (SOC). Il est capable d'analyser des journaux d'événements (logs) pour détecter des attaques (Bruteforce, SQLi, DoS) et de répondre à des questions techniques en s'appuyant sur une base de connaissances métier grâce à la technologie **RAG (Retrieval-Augmented Generation)**.

L'intégralité de l'analyse s'exécute **en local**, garantissant la confidentialité absolue des logs analysés.

## 🚀 Fonctionnalités principales

* **Routage intelligent :** L'agent détecte si l'utilisateur soumet des logs (analyse stricte et binaire) ou pose une question (mode expert cyber).
* **Analyse de Logs Automatisée :** Application stricte de règles de détection (R-001 à R-005) définies dans la base de connaissances.
* **Blacklist Dynamique :** Extraction automatique des adresses IP malveillantes (statut ALERTE) et ajout dans un fichier `blacklist.txt`.
* **100% Local :** Propulsé par Ollama (LLM & Embeddings) et ChromaDB (Base vectorielle).

## 🧠 Architecture et Fonctionnement

Le projet repose sur 3 composants clés :
1. **Ollama :** Fait tourner les modèles d'IA en local (`llama3.2` pour la réflexion et `nomic-embed-text` pour la vectorisation).
2. **LangChain :** Orchestre la logique du RAG, les prompts dynamiques et la communication entre les modèles et la base de données.
3. **ChromaDB :** Base de données vectorielle locale qui stocke le référentiel cyber (`RAG.txt`) pour permettre à l'IA de retrouver instantanément la bonne règle à appliquer.

### Structure des fichiers
* `agent_cyber.py` : Le script principal de l'agent interactif.
* `create_db.py` : Script d'ingestion pour transformer le fichier texte en base vectorielle ChromaDB.
* `RAG.txt` : La base de connaissances métier (Règles, normes, datasets d'exemples).
* `load_rag.py` : Script utilitaire pour vérifier la lisibilité du RAG.
* `blacklist.txt` : Fichier généré automatiquement contenant les IP bannies.

---

## 🛠️ Installation et Prérequis

### 1. Prérequis système
* **Python 3.9+**
* **Ollama** installé sur votre machine (disponible sur [ollama.com](https://ollama.com/)).

### 2. Téléchargement des modèles IA
Ouvrez un terminal et téléchargez les modèles requis par le projet :
```bash
ollama pull llama3.2
ollama pull nomic-embed-text