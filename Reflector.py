"""
Reflector.py
Este módulo define la clase Reflector, que simula el comportamiento del reflector en la máquina Enigma.
El reflector mapea las letras de forma simétrica y no tiene posición variable.
"""

class Reflector:
    def __init__(self, wiring):
        """
        Inicializa el reflector con su mapeo fijo.

        :param wiring: Un string de 26 caracteres que define el mapeo del reflector.
        """
        self.wiring = wiring

    def reflect(self, letter):
        """
        Mapea una letra según el mapeo del reflector.

        :param letter: La letra a reflejar (de 'A' a 'Z').
        :return: La letra reflejada.
        """
        index = ord(letter) - ord('A')
        return self.wiring[index]
