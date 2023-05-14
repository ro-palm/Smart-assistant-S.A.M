import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import datetime
import wolframalpha

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voiceRate = 130
# engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.setProperty("rate",voiceRate)
    engine.say(text)
    engine.runAndWait()


def take_command():
    while True:
        try:
            with sr.Microphone() as source:
                print('sleeping')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'sam' in command:
                    hour=datetime.datetime.now().hour
                    if hour>=0 and hour<12:
                        talk("Good Morning , Sir i am old and deaf please speak slow and clear........what can I do for you")
                        print("Good Morning , Sir i am old and deaf please speak slow and clear........what can I do for you")
                    elif hour>=12 and hour<18:
                        talk("Good Afternoon , Sir i am old and deaf please speak slow and clear........what can I do for you")
                        print("Good Afternoon , Sir i am old and deaf please speak slow and clear........what can I do for you")
                    else:
                        talk("Good Evening , Sir i am old and deaf please speak slow and clear........what can I do for you")
                        print("Good Evening , Sir i am old and deaf please speak slow and clear........what can I do for you")
                    print('listening')
                    
                    
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice)
                    command = command.lower()
                    print(command)
                    run_sam(command)
                    # engine.say.stop()
                    False
        except:
            continue
        return command
    
    
    
    
    
    
 
                
    


def run_sam(command):
    # command = take_command()
    print(command)
    if "good bye" in command or "ok bye" in command or "stop" in command:
                        talk('Good bye sir, I am going to grab a cup of tea')
                        print('Good bye sir, I am going to grab a cup of tea')
    
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        
        
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        
        
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        
        
    elif 'you' in command:
        talk('I am a smart assistant created by roan palm, like jarvis from iron man but with more class')
        
    
        
    elif 'what is' in command:
            talk('please wait')
            song = command.replace('what is', '')
            
            question=command
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            talk(answer)
            print(answer)
        
        
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        
    else:
        talk('Please say the command again.')
            
    




while True:
    take_command()