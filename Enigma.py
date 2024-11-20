"""
Enigma.py
Este módulo define la clase EnigmaMachine, que simula el funcionamiento completo de la máquina Enigma.
Incluye rotores, un reflector y el mecanismo de cifrado/descifrado.
"""

from Rotor import Rotor
from Reflector import Reflector

class EnigmaMachine:
    def __init__(self, rotors, reflector, alphabet):
        """
        Inicializa la máquina Enigma con una lista de rotores, un reflector y un alfabeto.
        
        :param rotors: Una lista de objetos de tipo Rotor.
        :param reflector: Un objeto de tipo Reflector.
        :param alphabet: El alfabeto completo que incluye letras, números y otros símbolos.
        """
        self.rotors = rotors
        self.reflector = reflector
        self.alphabet = alphabet
        self.alphabet_size = len(alphabet)

    def process_letter(self, letter):
        """
        Procesa una letra a través de la máquina Enigma.
        
        :param letter: La letra a procesar (puede ser un carácter especial, espacio, etc.)
        :return: La letra codificada o el mismo carácter si es un espacio o no está en el alfabeto.
        """
        # Si el carácter no está en el alfabeto, simplemente lo devolvemos tal cual
        if letter not in self.alphabet:
            print(f"Advertencia: El carácter '{letter}' no está en el alfabeto. Se procesará tal cual.")
            return letter

        # Paso adelante a través de los rotores
        for rotor in self.rotors:
            letter = rotor.encode_forward(letter)
        
        # Paso a través del reflector
        letter = self.reflector.reflect(letter)
        
        # Paso de regreso a través de los rotores (en orden inverso)
        for rotor in reversed(self.rotors):
            letter = rotor.encode_backward(letter)
        
        # Rotar los rotores
        for rotor in self.rotors:
            if not rotor.rotate():
                break
        
        return letter

    def encrypt_message(self, message):
        """
        Cifra o descifra un mensaje completo.
        
        :param message: El mensaje a procesar (string de letras y caracteres especiales).
        :return: El mensaje procesado.
        """
        result = ''
        for letter in message:
            # Convertir la letra a mayúsculas antes de procesarla
            result += self.process_letter(letter.upper())  # Convertimos a mayúsculas
        return result

