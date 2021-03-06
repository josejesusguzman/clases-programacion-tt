# -*- coding : utf-8 -*-
# Importar librerรญas
import pytz
import datetime

hora_local = pytz.timezone('America/Mexico_City')
hora_a_convertir = "2021-09-06 21:00:00"

hora_a_convertir = datetime.datetime.strptime(str(hora_a_convertir), "%Y-%m-%d %H:%M:%S")

print(hora_a_convertir)
print("Estรกs son las conversiones horarias: \n")

# Lista de zonas horarias
zonas = [
    ["๐ฒ๐ฝ", "America/Mexico_City"],
    ["๐จ๐ด", "America/Bogota"],
    ["๐ต๐ช", "America/Lima"],
    ["๐จ๐ฑ", "America/Santiago"],
    ["๐ฆ๐ท", "America/Buenos_Aires"],
    ["๐ช๐ธ", "Europe/Madrid"],
    ["๐บ๐พ", "America/Montevideo"],
    ["๐ช๐จ", "America/Guayaquil"],
    ["๐ฌ๐น", "America/Guatemala"],
    ["๐ธ๐ป", "America/El_Salvador"],
    ["๐ง๐ด", "America/La_Paz"],
    ["๐ต๐พ", "America/Asuncion"],
    ["๐ฉ๐ด", "America/Santo_Domingo"],
    ["๐ต๐ฆ", "America/Panama"],
    ["๐จ๐ท", "America/Costa_Rica"],
    ["๐ญ๐ณ", "America/Tegucigalpa"],
    ["๐ป๐ช", "America/Caracas"],
    ["๐ณ๐ฎ", "America/Managua"],
    ["๐จ๐บ", "Cuba"],
    ["๐ง๐ท", "America/Sao_Paulo"]
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
