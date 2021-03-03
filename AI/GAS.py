import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def talk(text): 
    engine.say(text)
    engine.runAndWait()

def take_command():
    try :
        with sr.Microphone() as source:
            talk('hello master how can i help you ')
            print ("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', "")
        talk("playing song of" + song)
        pywhatkit.playonyt(song)
    elif 'time' in command :
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('waktu saat ini adalah' + time)
    elif "who is" in command:
        information = command.replace("who is", '')
        info = wikipedia.summary(information, 1)
        print(info)
        talk(info)
    else:
        talk('Please repeat the command. i cant understand ')






while True:
    run_alexa()