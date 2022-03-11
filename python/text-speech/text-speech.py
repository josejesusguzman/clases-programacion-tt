from gtts import gTTS

texto = "yamede cudasai"
idioma = "zh-CN"

objeto = gTTS(text=texto, lang=idioma, slow=False)

objeto.save("audio.mp3")