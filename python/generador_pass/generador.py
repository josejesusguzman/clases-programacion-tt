from random import SystemRandom

longitud = int(input("Ingrese la longitud de la contraseña: "))

if longitud < 6 :
    print("la contraseña debe tener por lo menos 6 caracteres")
    exit()

valores = "0123456789qwertyuiopasdfghjklñzxcvbnm.-+/*_!?¿¡#$%:"

crypto = SystemRandom()
password = ""

while longitud > 0 :
    password = password + crypto.choice(valores)
    longitud = longitud - 1

print(password)
