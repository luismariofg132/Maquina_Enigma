"""
Reflector.py
Este módulo define la clase Reflector, que simula el comportamiento del reflector en la máquina Enigma.
El reflector mapea las letras de forma simétrica y no tiene posición variable.
"""

class Reflector:
    def __init__(self, wiring, alphabet):
        """
        Inicializa el reflector con su cableado.

        :param wiring: El cableado del reflector como un string (mapeo de letras).
        :param alphabet: El alfabeto extendido utilizado en la máquina Enigma.
        """
        self.wiring = wiring
        self.alphabet = alphabet

    def reflect(self, letter):
        """
        Refleja una letra a través del reflector.

        :param letter: La letra a procesar.
        :return: La letra reflejada.
        """
        index = self.alphabet.index(letter)
        return self.wiring[index]

