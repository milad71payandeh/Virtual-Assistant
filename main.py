import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play','')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%m')
        print(time)
        talk('The current time is:' + time)
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        print('Please say the command again')
        talk('Please say the command again')
while True:
    run_alexa()