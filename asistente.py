import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

import pyautogui, webbrowser
from time import sleep

name = 'jarvis'
# listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',150)

# for voice in voices:
#     print(voice)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    listener = sr.Recognizer()
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
            except:
                pass  
    except:
        pass
    return rec

def run():
    # r = listen()
    r = 'jarvis'

    re = r.split()

    if len(re) == 1:
        if re[0] == "jarvis":
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
        webbrowser.open('https://web.whatsapp.com/send?phone=+51940617299')
        sleep(10)
        r = r.replace('enviar', '')
        pyautogui.typewrite(r)
        pyautogui.press('enter')

    else:
        talk('Disculpe señor, no le entendi')

# while True:
run()