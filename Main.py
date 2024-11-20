"""
main.py
Este archivo principal configura y ejecuta la simulación de la máquina Enigma.
"""

from Rotor import Rotor
from Reflector import Reflector
from Enigma import EnigmaMachine

# Configuración de ejemplo
rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 17)  # Rotor I
rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", 5)   # Rotor II
rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", 22)  # Rotor III
reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")  # Reflector B

# Crear la máquina Enigma
enigma = EnigmaMachine([rotor1, rotor2, rotor3], reflector)

# Cifrar un mensaje
message = "HELLO"
encrypted_message = enigma.encrypt_message(message)
print("Mensaje cifrado:", encrypted_message)

# Descifrar el mensaje
rotor1.position = rotor2.position = rotor3.position = 0
decrypted_message = enigma.encrypt_message(encrypted_message)
print("Mensaje descifrado:", decrypted_message)
