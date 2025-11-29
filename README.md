# Plateforme de Traduction Sécurisée Fullstack - Backend
### 📋 Description

Ce backend REST sécurisé fournit un service interne de traduction destiné aux équipes Marketing (FR → EN) et Support Client (EN → FR) de TalAIt.
Il intègre :

- FastAPI (Python)

- Authentification JWT

- Base PostgreSQL

- Hugging Face Inference API

- Déploiement Docker

Les traductions exploitent les modèles :

    - Helsinki-NLP/opus-mt-fr-en

    - Helsinki-NLP/opus-mt-en-fr

### 🚀 Installation

**1. Prérequis**

- Docker + Docker Compose

- Hugging Face API Token (Read)

**2. Cloner & Configurer**

```bash
git clone https://github.com/SaidaAourras/Plateforme-de-Traduction-S-curis-e-Fullstack-backend.git
cd backend
cp .env.example .env
```

**3. Variables d’environnement**

```bash
DATABASE_URL=postgresql://talait:password123@db:5432/talait_db
SECRET_KEY=<clé JWT>

HF_API_TOKEN=hf_xxxxxxxxx
```

### ▶️ Lancer avec Docker

    docker-compose up -d --build

Vérifier :

    curl http://localhost:8000/health

Documentation API :

- Swagger : http://localhost:8000/docs

- Redoc : http://localhost:8000/redoc

### 🔌 Endpoints API

**1️⃣ POST /register**

Créer un utilisateur (username + password).

**2️⃣ POST /login**

Retourne un JWT :

        {
        "access_token": "...",
        "token_type": "bearer"
        }

**3️⃣ POST /translate (🔒 protégé)**

Exemple :

```bash
{
"text": "Bonjour le monde",
"choice": "fr-en"
}
```

Réponse :

```bash
{
"original_text": "...",
"translated_text": "...",
"direction": "fr-en",
"model": "Helsinki-NLP/opus-mt-fr-en"
}
```

### 🧪 Tests

Depuis le container :

```bash
docker-compose exec backend bash
pytest -v
``` 
Tests inclus :

- inscription

- login

- JWT invalide

- accès protégé refusé

- traduction validée

- gestion timeout HF

### 🚨 Limites du Modèle IA

| Limite        | Impact                     | Solution            |
| ------------- | -------------------------- | ------------------- |
| Cold start HF | 10-20s première requête    | Timeout + retry     |
| Quota HF      | 1000 req/jour              | Passer sur plan pro |
| Longueur max  | ~2000 caractères           | Découper le texte   |
| Erreurs 503   | indisponibilité temporaire | Retry automatique   |

### 📁 Structure

        api/
        └── v1/
            ├── routes/                      # Endpoints
            │   ├── auth.py                  # /auth (login, register)
            │   ├── users.py                 # /users
            │   └── translate.py             # /translate
            │
            ├── schemas/                     # Pydantic schemas
            │   ├── auth.py                  # AuthRequest, AuthResponse...
            │   ├── user.py                  # User, UserCreate...
            │   ├── translate.py             # TranslateRequest, TranslateResponse
            │   └── dependencies.py          # Dépendances globales
            │
            └── ... v2 (vide ou future version)
            

        core/
        ├── config.py                        # Configuration globale (env, settings)
        ├── db/
        │   └── frontend                     # (Dossier peut-être non utilisé)
        └── services/
            ├── auth_service.py              # Login, register, hash, JWT
            └── translate_services.py        # Appel HuggingFace ou autres modèles

        tests_unitaires/
        ├── test_endpoint_login.py           # Tests API login
        ├── test_endpoint_register.py        # Tests API register
        └── ... autres tests

        utils/
        ├── hashing.py                       # Hash bcrypt, verify password
        └── ... autres utilitaires

        main.py                               # Point d'entrée FastAPI
        dockerfile
        docker-compose.yml
        requirements.txt
        .env
        .env.docker
        README.md

## ✨ Author

**SAIDA AOURRAS**  

- 🐙 GitHub: [Aourras_Saida](https://github.com/SaidaAourras)  












