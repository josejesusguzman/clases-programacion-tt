# Venganza a estafadores
# Author: @brujeriatech
import requests
import random

# Genera username y passwords random
def random_word():
    word = ''
    for i in range(10):
        word += random.choice('abcdefghijklmnopqrstuvwxyz1234567890._')
    return word

# Manda la petición
def send_post(url, username, password):
    data = {"password": password}
    try:
        r = requests.post(url, data=data)
        if r.status_code == 200:
            print('OK - Enviado: username ' + username + ' password ' + password)
        else:
            return "Error"
    except requests.exceptions.RequestException as e:
        return "Error"

# Lo hace hasta el infinito
while True:
    username = random_word()
    password = random_word()
    send_post("http://ig-livesmediachat.ml/double-check1.php?username=" + username, username, password)
