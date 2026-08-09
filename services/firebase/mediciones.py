from .firebase import inicializar_firebase


def obtener_mediciones(limite=20, firebase_id=None):

    db = inicializar_firebase()

    consulta = db.collection("mediciones")

    if firebase_id:

        consulta = consulta.where(
            "dispositivoId",
            "==",
            firebase_id
        )

    documentos = (
        consulta
        .limit(limite)
        .stream()
    )

    resultado = []

    for documento in documentos:

        datos = documento.to_dict()

        datos["id"] = documento.id

        resultado.append(datos)

    return resultado