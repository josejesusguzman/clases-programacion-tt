emoji_dict = {"feliz": "π", "amo": "π", "risa": "π€£", "sonrisa": "π", "lorar": "π­", "beso": "π", "aplauso": "π", "reir": "π", "fuego": "π₯", "roto": "π", "pensando": "π€", "maravillado": "π€©", "aburrido": "π", "gΓΌiΓ±o": "π", "ok": "π", "abrazo": "π€", "cool": "π", "enojado": "π ", "Python": "π", "programar": " π»"}

sentence = input("Por favor, introduce una frase: ") 
words = sentence.split() 
res = ""
for i in words: 
    if i in emoji_dict: 
        res = res + " " + emoji_dict[i]
    else :
        res = res + " " + i

print(res)

list = []
for i in range(11) :
    if i % 2 == 0:
        list.append(i)

print(list)


generador = (i for i in range(11) if i % 2 == 0)

for i in generador :
    print(i, end=" ")