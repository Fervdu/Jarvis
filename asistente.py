import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

import pyautogui, webbrowser
from time import sleep

import os

name = 'alexa'

flag = 1
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',150)

# for voice in voices:
#     print(voice)

def talk(text):
    engine.say(text)
    engine.runAndWait()

rec = ''
def listen():
    # listener = sr.Recognizer()
    flag = 1
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            try:
                rec = listener.recognize_google(voice, language='es-MX')
                rec = rec.lower()
                if name in rec:
                    rec = rec.replace(name, '')
                    print(rec)
                    flag = run(rec)       
            except:
                pass  
    except:
        pass
    return flag

def run(r):

    # r = 'jarvis'

    re = r.split()

    if len(re) == 1:
        if re[0] == "alexa":
            talk("Digame en que lo ayudo")
    elif 'reproduce' in r:
        music = r.replace('reproduce', '')
        talk('Reproduciendo '+ music)
        pywhatkit.playonyt(music)
        print('Reproduciendo '+ music)
    elif 'hora' in r:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
        print(hora)
    elif 'enviar' in r:
        # hora = datetime.datetime.now().strftime('%H:%M')
        # horaArr = hora.split(':')
        # hr = horaArr[0]
        # m = horaArr[1]

        # print("hola july", hora)
        # print(hr)
        # print(m)
        # pywhatkit.sendwhatmsg("+51940617299", "hola bosha soy Jarvis", int(hr), int(m))
        contactos = ['bocha', 'mi']
        found = False
        for contacto in contactos:
            if contacto in r:
                if contacto == 'bocha':
                    found = True
                    webbrowser.open('https://web.whatsapp.com/send?phone=+51940617299')
                    sleep(10)
                    quitar = 'enviar a bosha'
                    r = r.replace(quitar, '')
                    print(r)
                    pyautogui.typewrite(r)
                    pyautogui.press('enter')
                elif contacto == 'yo':
                    found = True
                    webbrowser.open('https://web.whatsapp.com/send?phone=+51951972253')
                    sleep(10)
                    quitar = 'enviar a mi'
                    r = r.replace(quitar, '')
                    print(r)
                    pyautogui.typewrite(r)
                    pyautogui.press('enter')
        if found != True:
            talk("Contacto no encontrado")
    elif 'salir' in r:
        print("entro en salir")
        flag = 0
        talk('Hasta pronto señor')
    else:
        talk('Disculpe señor, no le entendi')
    return flag

while flag:
    flag = listen()