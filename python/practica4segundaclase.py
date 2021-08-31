# Uso de la Poke API en Python
import requests
from pprint import pprint
import matplotlib.pyplot as plt
import matplotlib.image as img

pokemon = input("Pon un pokemon: ")

url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
res = requests.get(url)

if res.status_code != 200 :
    print("Pokemon no encontrado")
    exit()

imagen = img.imread(res.json()['sprites']['front_default'])
plt.title(res.json()['name'])
imgplot = plt.imshow(imagen)
plt.show()

movimientos_ejex = []
poder_ataque_ejey = []

movimientos = res.json()['moves']
for i in range(int(len(movimientos) / 9)) :
    movimientos_ejex.append(movimientos[i]['move']['name'])
    ataque = requests.get(movimientos[i]['move']['url'])
    poder_ataque_ejey.append(ataque.json()['power'])

plt.bar(movimientos_ejex, poder_ataque_ejey)
plt.ylabel('Poder de ataque')
plt.xlabel('Movimiento')
plt.title('Ataques de ' + res.json()['name'])
plt.show()
