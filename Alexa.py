import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine =pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say('Hello Anupam')
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice= listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:

                command =command.replace('alexa','')
                print(command)
                #talk(command)
    except:
        pass
    return command
def run_alexa():
    command = take_command()
    #print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' +song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        #I for 12hr format, p for AM/PM
        print(time)
        talk('Current time is' +time)
    elif 'tell about' in command:
        person = command.replace('tell about','')
        info =wikipedia.summary(person,1)
        #here 1 represent the number of lines on the topic
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have boyfriend')
    elif 'are you single' in command:
        talk('NO, Google is my boyfriend')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')
#to keep alexa active
while True:
    run_alexa()
