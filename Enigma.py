"""
Enigma.py
Este módulo define la clase EnigmaMachine, que simula el funcionamiento completo de la máquina Enigma.
Incluye rotores, un reflector y el mecanismo de cifrado/descifrado.
"""

from Rotor import Rotor
from Reflector import Reflector

class EnigmaMachine:
    def __init__(self, rotors, reflector):
        """
        Inicializa la máquina Enigma con una lista de rotores y un reflector.

        :param rotors: Una lista de objetos de tipo Rotor.
        :param reflector: Un objeto de tipo Reflector.
        """
        self.rotors = rotors
        self.reflector = reflector

    def process_letter(self, letter):
        """
        Procesa una letra a través de la máquina Enigma.

        :param letter: La letra a procesar (de 'A' a 'Z').
        :return: La letra codificada/decodificada.
        """
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

        :param message: El mensaje a procesar (string de letras).
        :return: El mensaje procesado.
        """
        result = ''
        for letter in message:
            if letter.isalpha():
                result += self.process_letter(letter.upper())
        return result
