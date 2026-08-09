from pathlib import Path

import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore


BASE_DIR = Path(__file__).resolve().parents[2]

CREDENTIALS_FILE = (
    BASE_DIR / "firebase-service-account.json"
)


def inicializar_firebase():

    if not firebase_admin._apps:

        credenciales = credentials.Certificate(
            str(CREDENTIALS_FILE)
        )

        firebase_admin.initialize_app(
            credenciales
        )

    return firestore.client()