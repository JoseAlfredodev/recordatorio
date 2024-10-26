# Recordatorio para Subir Video a YouTube

Este es un script en Python que permite configurar un recordatorio para subir un video a YouTube. Utiliza la biblioteca `sched` y `time` para programar la notificación en una hora específica ingresada por el usuario.

## Descripción

Este script pregunta al usuario a qué hora quiere el recordatorio y luego programa una alerta para esa hora. Si la hora ya pasó en el día actual, el recordatorio se programa para el día siguiente.

## Requisitos

- Python 3.x

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tuusuario/recordatorio-youtube.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd recordatorio-youtube
    ```

## Uso

1. Ejecuta el script principal:
    ```bash
    python recordatorio.py
    ```
2. Ingresa la hora en formato `HH:MM` cuando se te pregunte.
3. Espera a que aparezca el mensaje de recordatorio a la hora especificada.

## Código

```python
import sched
import time
from datetime import datetime, timedelta
