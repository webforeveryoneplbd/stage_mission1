from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

# Créer la base de données et les tables
models.Base.metadata.create_all(bind=engine)

# Ouvrir une session de base de données
db = SessionLocal()

# Utilisateurs pré-définis
users = [
    schemas.UserCreate(
        username="user1",
        email="user1@example.com",
        matricule="123456",
        password="password1",
        
    ),
    schemas.UserCreate(
        username="user2",
        email="user2@example.com",
        matricule="654321",
        password="password2",
       
    ),
]

# Insérer les utilisateurs pré-définis dans la base de données
for user in users:
    crud.create_user(db=db, user=user)

# Fermer la session de base de données
db.close()
