import sched
import time
from datetime import datetime, timedelta

scheduler = sched.scheduler(time.time, time.sleep)

def recordatorio():
    print("Es hora de subir tu video a YouTube!")

hora = input("¿A que hora quieres el recordatorio? (HH:MM formato 24h): ")
hora_split = hora.split(":")
hora_recordatorio = int(hora_split[0])
minutos_recordatorio = int(hora_split[1])

now = datetime.now()

fecha_recordatorio = now.replace(hour=hora_recordatorio, minute=minutos_recordatorio, second=0, microsecond=0)

if fecha_recordatorio < now:
    fecha_recordatorio = fecha_recordatorio + timedelta(days=1)

def programar_recordatorio(fecha_hora):
    evento = scheduler.enterabs(fecha_hora.timestamp(), 1, recordatorio)
    print(f"Recordatorio programado para: {fecha_hora}")

programar_recordatorio(fecha_recordatorio)
print("Esperando recordatorio...")
scheduler.run()
