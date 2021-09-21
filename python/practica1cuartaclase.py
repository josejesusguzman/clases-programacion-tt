import azure.cognitiveservices.speech as speechsdk

url = "https://eastus.api.cognitive.microsoft.com/sts/v1.0/issuetoken"
headers = {
    "Content-Type": "application/json"
}

speech_config = speechsdk.SpeechConfig(subscription="8adc9b19ae5b47d880a2b1c8947478a4", region="eastus")

brujeria = True

while brujeria:
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, language="es-MX")
    result = speech_recognizer.recognize_once()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Escuché: {}".format(result.text))
        if result.text == "No es brujeria, es tecnología.":
            print("Saliendo...")
            brujeria = False
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No te entendí nada")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Se canceló por {}: {}".format(cancellation_details.reason))

