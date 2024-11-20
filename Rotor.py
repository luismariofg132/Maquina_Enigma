"""
Rotor.py
Este módulo define la clase Rotor, que simula el comportamiento de un rotor en la máquina Enigma.
Cada rotor tiene un cableado (wiring) que define su mapeo interno, un punto de giro (notch) para avanzar el siguiente rotor, 
y una posición que se actualiza después de cada pulsación.
"""
class Rotor:
    def __init__(self, wiring, notch, alphabet):
        """
        Inicializa el rotor con el cableado y el carácter de muesca (notch).

        :param wiring: El cableado del rotor como un string (mapeo de letras).
        :param notch: La posición de muesca del rotor.
        :param alphabet: El alfabeto extendido utilizado en la máquina Enigma.
        """
        self.wiring = wiring
        self.notch = notch
        self.alphabet = alphabet
        self.position = 0  # Posición inicial del rotor

    def encode_forward(self, letter):
        """
        Codifica una letra en el sentido adelante (de izquierda a derecha) a través del rotor.

        :param letter: La letra a procesar.
        :return: La letra codificada.
        """
        index = self.alphabet.index(letter)
        return self.wiring[(index + self.position) % len(self.alphabet)]

    def encode_backward(self, letter):
        """
        Codifica una letra en el sentido inverso (de derecha a izquierda) a través del rotor.

        :param letter: La letra a procesar.
        :return: La letra codificada.
        """
        index = self.wiring.index(letter)
        return self.alphabet[(index - self.position) % len(self.alphabet)]

    def rotate(self):
        """
        Rota el rotor en su posición.

        :return: Verdadero si el rotor rota, falso si es la última muesca.
        """
        self.position = (self.position + 1) % len(self.alphabet)
        return self.position != self.notch
