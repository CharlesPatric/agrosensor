from services.dispositivos.resolver import (
    obtener_dispositivo_por_firebase_id,
    obtener_parcela_por_firebase_id,
)


def enriquecer_medicion(medicion):

    dispositivo = obtener_dispositivo_por_firebase_id(
        medicion.get("dispositivoId")
    )

    parcela = obtener_parcela_por_firebase_id(
        medicion.get("lugarId")
    )

    return {
        "id": medicion.get("id"),

        "dispositivo": {
            "id": dispositivo.id,
            "nombre": dispositivo.nombre,
            "codigo": dispositivo.codigo,
        } if dispositivo else None,

        "parcela": {
            "id": parcela.id,
            "nombre": parcela.nombre,
        } if parcela else None,

        "temperatura": medicion.get("temperatura"),
        "humedadAmbiente": medicion.get("humedadAmbiente"),
        "humedadSuelo": medicion.get("humedadSuelo"),
        "estado": medicion.get("estado"),
        "ts": medicion.get("ts"),
    }