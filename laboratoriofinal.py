from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI(title="Mini Combate RPG - Simple")

# Memoria donde se guarda una sola partida
partida = None

class Accion(BaseModel):
    accion: str  # atacar, defender, curar


@app.post("/start")
def iniciar_partida():
    global partida
    partida = {
        "hp_jugador": 100,
        "hp_enemigo": 100,
        "log": "Batalla iniciada"
    }
    return {"mensaje": "Partida iniciada", "estado": partida}


@app.post("/accion")
def accion_jugador(req: Accion):
    global partida
    if partida is None:
        raise HTTPException(400, "No hay partida iniciada")

    if req.accion not in ["atacar", "defender", "curar"]:
        raise HTTPException(400, "Acción inválida")

    log = []

    # --- ACCIÓN DEL JUGADOR ---
    if req.accion == "atacar":
        dano = random.randint(10, 25)
        partida["hp_enemigo"] -= dano
        log.append(f"Atacaste e hiciste {dano} de daño.")

    elif req.accion == "defender":
        log.append("Te defendiste. (En esta versión simple no reduce daño).")

    elif req.accion == "curar":
        cura = random.randint(8, 20)
        partida["hp_jugador"] += cura
        log.append(f"Te curaste {cura} puntos.")

    # Enemigo muere
    if partida["hp_enemigo"] <= 0:
        partida["log"] = " ".join(log) + " ¡Ganaste!"
        return partida

    # --- ACCIÓN DEL ENEMIGO ---
    dano_enemigo = random.randint(8, 18)
    partida["hp_jugador"] -= dano_enemigo
    log.append(f"El enemigo te golpeó y te hizo {dano_enemigo} de daño.")

    # Jugador muere
    if partida["hp_jugador"] <= 0:
        partida["log"] = " ".join(log) + " Perdiste..."
        return partida

    partida["log"] = " ".join(log)
    return partida


@app.get("/estado")
def estado():
    if partida is None:
        raise HTTPException(400, "No hay partida iniciada")
    return partida
