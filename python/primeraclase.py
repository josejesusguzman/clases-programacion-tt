import random

def tiro_dado(cantidad_dados):
    for dado in range(cantidad_dados):
        print("El dado " + str(dado + 1) + " dio: " + str(random.randint(1,6)))

tiro_dado(5)

