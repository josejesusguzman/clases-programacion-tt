# -*- coding : utf-8 -*-
# Importar librerías
import pytz
import datetime

hora_local = pytz.timezone('America/Mexico_City')
hora_a_convertir = "2021-09-06 21:00:00"

hora_a_convertir = datetime.datetime.strptime(str(hora_a_convertir), "%Y-%m-%d %H:%M:%S")

print(hora_a_convertir)
print("Estás son las conversiones horarias: \n")

# Lista de zonas horarias
zonas = [
    ["🇲🇽", "America/Mexico_City"],
    ["🇨🇴", "America/Bogota"],
    ["🇵🇪", "America/Lima"],
    ["🇨🇱", "America/Santiago"],
    ["🇦🇷", "America/Buenos_Aires"],
    ["🇪🇸", "Europe/Madrid"],
    ["🇺🇾", "America/Montevideo"],
    ["🇪🇨", "America/Guayaquil"],
    ["🇬🇹", "America/Guatemala"],
    ["🇸🇻", "America/El_Salvador"],
    ["🇧🇴", "America/La_Paz"],
    ["🇵🇾", "America/Asuncion"],
    ["🇩🇴", "America/Santo_Domingo"],
    ["🇵🇦", "America/Panama"],
    ["🇨🇷", "America/Costa_Rica"],
    ["🇭🇳", "America/Tegucigalpa"],
    ["🇻🇪", "America/Caracas"],
    ["🇳🇮", "America/Managua"],
    ["🇨🇺", "Cuba"],
    ["🇧🇷", "America/Sao_Paulo"]
]

times = {"00pm": "X"}

hora_a_convertir = hora_local.localize(hora_a_convertir)

for pais in zonas:
    dtc = hora_a_convertir.astimezone(pytz.timezone(pais[1]))
    
    if pais[1] == "Europe/Madrid":
        dtc = dtc.strftime("%-HH")
    else:
        dtc = dtc.strftime("%-I%p")

    try:
        times[dtc] = times[dtc] + pais[0]
    except KeyError:
        times[dtc] = pais[0]

    times[dtc] = times[dtc] + " "

for tiempo, bandera in times.items():
    if bandera != "X":
        print(tiempo.lower(), bandera.strip())
