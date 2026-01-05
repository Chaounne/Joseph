# Joseph — Discord AI Chat Bot avec MiMo

**Joseph** est un bot Discord alimenté par une intelligence artificielle utilisant le modèle **MiMo** pour générer des réponses naturelles aux messages des utilisateurs.  
Il est conçu pour intégrer une IA conversationnelle directement dans votre serveur Discord.  

Dépôt GitHub : https://github.com/Chaounne/Joseph

---

## Fonctionnalités

- Réponses intelligentes en langage naturel basées sur MiMo  
- Détection dynamique des messages et réponse aux mentions ou commandes  
- Configuration simple avec token Discord  
- Conversation contextuelle selon l’historique de messages  

---

## Prérequis

Avant de commencer, assurez-vous d’avoir :

- Python 3.10 ou plus
- Un bot Discord avec son token (https://discord.com/developers)
- Accès ou implémentation du modèle MiMo (via API ou localement)

Le modèle MiMo est un modèle d’IA orienté instruction et conversation, optimisé pour générer du texte naturel et des dialogues.

---

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/Chaounne/Joseph.git
    cd Joseph
    ```

2. Créez un environnement virtuel :
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS / Linux
    venv\Scripts\activate     # Windows
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

4. Créez un fichier `.env` à la racine du projet :
    ```env
    DISCORD_TOKEN=VOTRE_TOKEN_ICI
    MIMO_API_KEY=VOTRE_CLE_API_MIMO
    ```
5. Modifiez dans le fichier `main.py` les identifiants de canaux discords afin que le bot puisse parler dans ceux-ci :
   ```python
    TARGET_CHANNEL_IDS = [ID_CHANNELS_ICI] 
    ```

---

## Utilisation

Lancez le bot avec la commande suivante :

```bash
python main.py
```

Le bot se connectera à Discord et commencera à répondre aux messages selon la logique définie dans le projet.

## À propos de MiMo

MiMo est un modèle de langage conçu pour suivre des instructions et produire des conversations cohérentes et naturelles. Il est particulièrement adapté aux chatbots et assistants conversationnels.

