"""
Enigma.py
Este módulo define la clase EnigmaMachine, que simula el funcionamiento completo de la máquina Enigma.
Incluye componentes esenciales como los rotores, el reflector y el mecanismo de cifrado/descifrado.
"""

from Rotor import Rotor
from Reflector import Reflector

class EnigmaMachine:
    def __init__(self, rotors, reflector, alphabet):
        """
        Inicializa la máquina Enigma con una lista de rotores, un reflector y un alfabeto.

        :param rotors: Lista de objetos de tipo Rotor que representan los rotores de la máquina.
        :param reflector: Objeto de tipo Reflector que refleja la señal antes de volver por los rotores.
        :param alphabet: El alfabeto utilizado por la máquina (por ejemplo, A-Z o un conjunto extendido).
        """
        self.rotors = rotors  # Lista de rotores que procesan la señal en secuencia.
        self.reflector = reflector  # Reflector que realiza el mapeo simétrico de las letras.
        self.alphabet = alphabet  # Alfabeto base utilizado en la codificación.
        self.alphabet_size = len(alphabet)  # Tamaño del alfabeto.

    def process_letter(self, letter):
        """
        Procesa una letra a través de la máquina Enigma, incluyendo rotores, reflector y rotaciones.

        :param letter: La letra a procesar (debe pertenecer al alfabeto definido).
        :return: La letra cifrada o el mismo carácter si no pertenece al alfabeto.
        """
        # Si el carácter no pertenece al alfabeto, no se procesa y se devuelve tal cual.
        if letter not in self.alphabet:
            return letter

        # Paso adelante: la señal pasa a través de los rotores en orden.
        for rotor in self.rotors:
            letter = rotor.encode_forward(letter)
        
        # La señal pasa por el reflector, que realiza el mapeo simétrico.
        letter = self.reflector.reflect(letter)
        
        # Paso inverso: la señal vuelve a través de los rotores en orden inverso.
        for rotor in reversed(self.rotors):
            letter = rotor.encode_backward(letter)
        
        # Rotar los rotores después de procesar la letra.
        # El primer rotor siempre rota; los siguientes sólo rotan si el anterior alcanza su muesca.
        for rotor in self.rotors:
            if not rotor.rotate():
                break  # Si el rotor no alcanza su muesca, se detiene la rotación.
        
        return letter

    def encrypt_message(self, message):
        """
        Cifra o descifra un mensaje completo procesando cada carácter individualmente.

        :param message: El mensaje a procesar (puede incluir caracteres no cifrables).
        :return: El mensaje cifrado/descifrado.
        """
        result = ''  # Almacena el mensaje cifrado/descifrado.
        for letter in message:
            # Convertir cada letra a mayúsculas antes de procesarla para mantener consistencia.
            result += self.process_letter(letter.upper())
        return result
