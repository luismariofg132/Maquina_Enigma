"""
main.py
Lee la configuración de la máquina Enigma desde un archivo JSON,
procesa un archivo de texto y guarda el resultado cifrado en otro archivo.
"""

import sys
import json
from Rotor import Rotor
from Reflector import Reflector
from Enigma import EnigmaMachine

def load_configuration(config_file):
    """
    Carga la configuración de la máquina Enigma desde un archivo JSON.

    :param config_file: Ruta al archivo JSON con la configuración.
    :return: Lista de rotores, reflector y alfabeto configurados.
    """
    try:
        # Leer el archivo JSON de configuración
        with open(config_file, 'r', encoding='utf-8') as file:
            config = json.load(file)

        # Obtener el alfabeto extendido
        alphabet = config.get("alphabet")
        if not alphabet:
            raise KeyError("alphabet")

        # Verificar unicidad del alfabeto
        if len(set(alphabet)) != len(alphabet):
            raise ValueError("El alfabeto contiene caracteres duplicados.")

        # Crear los rotores
        rotors = []
        for rotor in config["rotors"]:
            wiring = rotor.get("wiring")
            notch = rotor.get("notch")
            if not wiring or notch is None:
                raise KeyError("Cada rotor debe tener 'wiring' y 'notch'.")
            if len(wiring) != len(alphabet):
                raise ValueError(f"La configuración del rotor '{wiring}' no coincide con el alfabeto.")
            rotors.append(Rotor(wiring, notch, alphabet))

        # Crear el reflector
        reflector_wiring = config["reflector"].get("wiring")
        if not reflector_wiring:
            raise KeyError("reflector.wiring")
        if len(reflector_wiring) != len(alphabet):
            raise ValueError("La configuración del reflector no coincide con el alfabeto.")
        reflector = Reflector(reflector_wiring, alphabet)

        # Devolver los rotores, el reflector y el alfabeto
        return rotors, reflector, alphabet

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo de configuración '{config_file}'.")
        sys.exit(1)
    except KeyError as e:
        print(f"Error en el archivo de configuración: falta la clave {e}.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error en el archivo de configuración: {e}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: El archivo de configuración '{config_file}' no es un JSON válido.")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado al cargar la configuración: {e}")
        sys.exit(1)


def main():
    # Verificar argumentos de línea de comandos
    if len(sys.argv) != 4:
        print("Uso: python main.py <archivo_config> <archivo_entrada> <archivo_salida>")
        sys.exit(1)

    # Obtener rutas de los archivos
    config_file = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    # Cargar la configuración
    rotors, reflector, alphabet = load_configuration(config_file)

    # Crear la máquina Enigma
    enigma = EnigmaMachine(rotors, reflector, alphabet)

    try:
        # Leer el archivo de entrada
        with open(input_file, 'r', encoding='utf-8') as file:
            message = file.read()

        # Cifrar el mensaje
        encrypted_message = enigma.encrypt_message(message)

        # Guardar el mensaje cifrado
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(encrypted_message)

        print(f"El mensaje cifrado ha sido guardado en: {output_file}")

    except FileNotFoundError:
        print(f"Error: El archivo '{input_file}' no existe.")
        sys.exit(1)
    except Exception as e:
        print(f"Error al procesar los archivos: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
