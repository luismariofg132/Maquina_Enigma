import random

# Alfabeto completo
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÑ0123456789 .,;!?()[]{}+-*/=_@#%&:$¡¿"

# Función para generar una permutación aleatoria única del alfabeto
def generate_random_wiring(alphabet):
    alphabet_list = list(alphabet)
    random.shuffle(alphabet_list)  # Mezclamos aleatoriamente los caracteres
    return ''.join(alphabet_list)

# Generar los 3 rotores con permutaciones únicas
rotor1_wiring = generate_random_wiring(alphabet)
rotor2_wiring = generate_random_wiring(alphabet)
rotor3_wiring = generate_random_wiring(alphabet)

# Crear el JSON para los rotores con notches
rotors = [
    {
        "wiring": rotor1_wiring,
        "notch": 30
    },
    {
        "wiring": rotor2_wiring,
        "notch": 45
    },
    {
        "wiring": rotor3_wiring,
        "notch": 60
    }
]

# Crear el JSON completo
config = {
    "alphabet": alphabet,
    "rotors": rotors,
    "reflector": {
        "wiring": "YRUHQSLDPXNGOKMIEBFZCWVJATÁÉÍÓÚÑ0123456789 .,;!?()[]{}+-*/=_@#%&:$¡¿"
    }
}

# Imprimir la configuración generada
import json
print(json.dumps(config, ensure_ascii=False, indent=2))
