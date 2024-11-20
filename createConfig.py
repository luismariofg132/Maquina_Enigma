import random

# Alfabeto completo
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÑ0123456789 .,;!?()[]{}+-*/=_@#%&:$¡¿"

# Función para generar un reflector simétrico
def generate_symmetric_reflector(alphabet):
    # Convertimos el alfabeto en una lista
    alphabet_list = list(alphabet)
    # Mezclamos aleatoriamente los caracteres para generar una permutación
    random.shuffle(alphabet_list)

    # Creamos el reflector como un diccionario
    reflector_dict = {}
    for i in range(0, len(alphabet_list), 2):
        # Emparejamos los caracteres de manera simétrica
        reflector_dict[alphabet_list[i]] = alphabet_list[i + 1]
        reflector_dict[alphabet_list[i + 1]] = alphabet_list[i]

    # Generamos la salida del reflector en el formato requerido
    reflector_wiring = ''.join(reflector_dict[char] for char in alphabet)
    
    return reflector_wiring

# Función para generar una permutación aleatoria única del alfabeto (para los rotores)
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

# Generar el reflector simétrico
reflector_wiring = generate_symmetric_reflector(alphabet)

# Crear el JSON completo
config = {
    "alphabet": alphabet,
    "rotors": rotors,
    "reflector": {
        "wiring": reflector_wiring
    }
}

# Imprimir la configuración generada
import json
print(json.dumps(config, ensure_ascii=False, indent=2))
