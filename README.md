# Simulación de la Máquina Enigma

Este proyecto implementa una simulación de la máquina Enigma, un dispositivo utilizado durante la Segunda Guerra Mundial para cifrar y descifrar mensajes. La implementación se basa en Python e incluye la funcionalidad de los rotores, el reflector y el mecanismo completo de cifrado/descifrado.

## Estructura del Proyecto

El proyecto está organizado en los siguientes módulos:

- **`Rotor.py`**: Implementa la clase `Rotor`, que simula el comportamiento de un rotor en la máquina Enigma.
- **`Reflector.py`**: Implementa la clase `Reflector`, que mapea las letras de forma simétrica.
- **`Enigma.py`**: Implementa la clase `EnigmaMachine`, que combina rotores y reflector para simular la máquina completa.
- **`main.py`**: Script principal que carga la configuración desde un archivo JSON, procesa un archivo de entrada y guarda el resultado cifrado en un archivo de salida.
- **`createConfig.py`**: Script para generar configuraciones automáticas del archivo JSON requerido para la máquina Enigma.

## Requisitos

- **Python 3.7 o superior**
- Archivo de configuración en formato JSON (puedes generarlo con `createConfig.py`).
- Archivos de texto para entrada y salida.

## Instalación

1. Clona este repositorio en tu máquina local:
    ```bash
    git clone https://github.com/luismariofg132/Maquina_Enigma.git
    cd Maquina_Enigma
    ```

2. Asegúrate de tener Python 3.7 o superior instalado.

3. Instala las dependencias necesarias (si aplica, aunque este proyecto no tiene dependencias externas).

## Uso

### Generar Configuración Automática

El archivo `createConfig.py` genera un archivo JSON con la configuración requerida para los rotores, el reflector y el alfabeto. Este archivo se puede usar directamente como entrada para `main.py`.

1. Ejecuta el script:
    ```bash
    python createConfig.py
    ```

2. Copia la salida generada en un archivo llamado, por ejemplo, `config.json`.

3. Ejecuta el script principal con la configuración generada:
    ```bash
    python main.py config.json input.txt output.txt
    ```
    - `config.json`: Archivo de configuración generado por `createConfig.py`.
    - `input.txt`: Archivo de texto con el mensaje a cifrar.
    - `output.txt`: Archivo de texto donde se guardará el mensaje cifrado.

### Ejemplo de Uso

1. Genera un archivo de configuración:
    ```bash
    python createConfig.py > config.json
    ```

2. Cifra un mensaje de prueba:
    ```bash
    python main.py config.json input.txt output.txt
    ```
    - `input.txt`: Archivo de texto con el mensaje a cifrar.
    - `output.txt`: Archivo de texto donde se guardará el mensaje cifrado.

3. Descifra el mensaje cifrado:
    ```bash
    python main.py config.json output.txt decrypted.txt
    ```
    - `output.txt`: Archivo de texto con el mensaje cifrado.
    - `decrypted.txt`: Archivo de texto donde se guardará el mensaje descifrado.


### Archivo de Configuración

El archivo JSON contiene la configuración de los rotores, el reflector y el alfabeto. Ejemplo de salida generada por `generate_config.py`:

```json
{
  "alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÑ0123456789 .,;!?()[]{}+-*/=_@#%&:$¡¿",
  "rotors": [
    {
      "wiring": "PERMUTACIÓN_ALEATORIA_UNO",
      "notch": 30
    },
    {
      "wiring": "PERMUTACIÓN_ALEATORIA_DOS",
      "notch": 45
    },
    {
      "wiring": "PERMUTACIÓN_ALEATORIA_TRES",
      "notch": 60
    }
  ],
  "reflector": {
    "wiring": "REFLECTOR_SIMÉTRICO_GENERADO"
  }
}
