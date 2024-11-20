"""
Reflector.py
Este módulo define la clase Reflector, que simula el comportamiento del reflector en la máquina Enigma.
El reflector mapea las letras de forma simétrica, lo que permite que la señal retroceda a través de los rotores.
A diferencia de los rotores, el reflector no tiene posición variable y no rota.
"""

class Reflector:
    def __init__(self, wiring, alphabet):
        """
        Inicializa el reflector con su cableado fijo y el alfabeto utilizado.

        :param wiring: El cableado del reflector como un string, define cómo cada letra se mapea a otra.
        :param alphabet: El alfabeto utilizado en la máquina Enigma, típicamente de la A a la Z.
        """
        self.wiring = wiring  # Define las conexiones fijas entre las letras en el reflector.
        self.alphabet = alphabet  # Alfabeto base utilizado para el mapeo.

    def reflect(self, letter):
        """
        Procesa una letra pasándola por el reflector, devolviendo su contraparte mapeada.

        :param letter: La letra que ingresa al reflector.
        :return: La letra reflejada según el cableado.
        """
        # Encuentra la posición de la letra en el alfabeto.
        index = self.alphabet.index(letter)
        # Devuelve la letra mapeada según el cableado del reflector.
        return self.wiring[index]
