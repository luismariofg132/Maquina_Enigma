"""
Rotor.py
Este módulo define la clase Rotor, que simula el comportamiento de un rotor en la máquina Enigma.
Cada rotor tiene un cableado (wiring) que define su mapeo interno, un punto de giro (notch) para avanzar el siguiente rotor, 
y una posición que se actualiza después de cada pulsación.
"""
class Rotor:
    def __init__(self, wiring, notch, alphabet):
        """
        Inicializa el rotor con el cableado, el carácter de muesca (notch) y el alfabeto utilizado.

        :param wiring: El cableado del rotor como un string que representa el mapeo interno de letras.
        :param notch: La posición de muesca que determina cuándo el rotor debe avanzar al siguiente.
        :param alphabet: El alfabeto utilizado para el mapeo, usualmente de la A a la Z.
        """
        self.wiring = wiring  # Define cómo las letras se mapean internamente dentro del rotor.
        self.notch = notch  # Posición específica que provoca el avance del siguiente rotor.
        self.alphabet = alphabet  # Alfabeto utilizado por la máquina Enigma.
        self.position = 0  # Posición inicial del rotor, equivalente al anillo en el rotor físico.

    def encode_forward(self, letter):
        """
        Codifica una letra cuando pasa a través del rotor en sentido directo (entrada -> salida).

        :param letter: La letra a procesar en su posición actual.
        :return: La letra codificada después de aplicar el mapeo del rotor.
        """
        index = self.alphabet.index(letter)  # Encuentra la posición de la letra en el alfabeto.
        # Aplica el desplazamiento según la posición actual del rotor y realiza el mapeo.
        return self.wiring[(index + self.position) % len(self.alphabet)]

    def encode_backward(self, letter):
        """
        Codifica una letra cuando pasa a través del rotor en sentido inverso (salida -> entrada).

        :param letter: La letra a procesar en su posición actual.
        :return: La letra codificada tras pasar por el rotor en sentido inverso.
        """
        index = self.wiring.index(letter)  # Encuentra la posición de la letra en el cableado del rotor.
        # Invierte el desplazamiento y devuelve la posición correspondiente en el alfabeto original.
        return self.alphabet[(index - self.position) % len(self.alphabet)]

    def rotate(self):
        """
        Avanza la posición del rotor en una unidad (simula la rotación del rotor tras una tecla).

        :return: True si el rotor alcanza su muesca (indicando que el siguiente rotor debe girar), 
                 False en caso contrario.
        """
        # Incrementa la posición actual del rotor y ajusta para mantenerse dentro del rango del alfabeto.
        self.position = (self.position + 1) % len(self.alphabet)
        # Devuelve True si la posición actual coincide con la muesca, permitiendo al próximo rotor girar.
        return self.position != self.notch
