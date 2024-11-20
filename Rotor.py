"""
Rotor.py
Este módulo define la clase Rotor, que simula el comportamiento de un rotor en la máquina Enigma.
Cada rotor tiene un cableado (wiring) que define su mapeo interno, un punto de giro (notch) para avanzar el siguiente rotor, 
y una posición que se actualiza después de cada pulsación.
"""

class Rotor:
    def __init__(self, wiring, notch):
        """
        Inicializa un rotor con su cableado y posición de giro.

        :param wiring: Un string de 26 caracteres que define el mapeo de las letras.
        :param notch: Un número entero que indica la posición de giro del rotor (0-25).
        """
        self.wiring = wiring
        self.notch = notch
        self.position = 0

    def encode_forward(self, letter):
        """
        Mapea una letra en dirección hacia el reflector.

        :param letter: La letra a codificar (de 'A' a 'Z').
        :return: La letra codificada tras pasar por el rotor.
        """
        index = (ord(letter) - ord('A') + self.position) % 26
        return chr((ord(self.wiring[index]) - ord('A') - self.position) % 26 + ord('A'))

    def encode_backward(self, letter):
        """
        Mapea una letra en dirección opuesta desde el reflector.

        :param letter: La letra a decodificar (de 'A' a 'Z').
        :return: La letra decodificada tras pasar por el rotor.
        """
        index = (self.wiring.index(chr((ord(letter) - ord('A') + self.position) % 26 + ord('A'))) - self.position) % 26
        return chr(index + ord('A'))

    def rotate(self):
        """
        Rota el rotor una posición y verifica si llega al punto de giro.

        :return: True si alcanza el punto de giro; de lo contrario, False.
        """
        self.position = (self.position + 1) % 26
        return self.position == self.notch
