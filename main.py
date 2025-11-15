from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API Mini Combate funcionando"}

@app.get("/combate")
def combate(nombre: str = "Jugador"):
    vida_jugador = 30
    vida_enemigo = 25

    while vida_jugador > 0 and vida_enemigo > 0:
        # Daño del jugador
        dano_jugador = random.randint(5, 10)
        vida_enemigo -= dano_jugador

        if vida_enemigo <= 0:
            break

        # Daño del enemigo
        dano_enemigo = random.randint(3, 8)
        vida_jugador -= dano_enemigo

    ganador = nombre if vida_jugador > 0 else "Enemigo"

    return {
        "jugador": nombre,
        "vida_final_jugador": vida_jugador,
        "vida_final_enemigo": vida_enemigo,
        "ganador": ganador
    }