buyukAlfabe=("ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ")
kucukAlfabe=("abcçdefgğhıijklmnoöprsştuüvyz")

def lower(text:str):
    newText=str()
    for i in text:
        if i in buyukAlfabe:
            index=buyukAlfabe.index(i)
            newText+=kucukAlfabe[index]
        else:
            newText+=i

    return newText

# pip install pipwin
# pipwin install pyaudio
# pip install SpeechRecognition

import speech_recognition as sr
from os import system


r=sr.Recognizer()
with sr.Microphone() as source:
    system("cls")
    print("Say Something!")
    audio=r.listen(source)

flag=False
try:
    text = r.recognize_google(audio,language="tr")
    print("Algılanan:"+text)
    flag=True
    text=lower(text)
except sr.UnknownValueError:
    print("Google Speech sesi anlayamadı")
except sr.RequestError as e:
    print("Google Speech servisinden cevap alınamadı: {0}".format(e))

if flag:
    if text=="hesap makinesi":
        system("calc")