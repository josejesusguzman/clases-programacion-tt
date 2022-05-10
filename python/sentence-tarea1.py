emoji_dict = {"feliz": "😃", "amo": "😍", "risa": "🤣", "sonrisa": "😊", "lorar": "😭", "beso": "😘", "aplauso": "👏", "reir": "😁", "fuego": "🔥", "roto": "💔", "pensando": "🤔", "maravillado": "🤩", "aburrido": "🙄", "güiño": "😉", "ok": "👌", "abrazo": "🤗", "cool": "😎", "enojado": "😠", "Python": "🐍", "programar": " 💻"}

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