import pyttsx3,os,openai
import json
import speech_recognition as sr
import datetime
import sys
from text_to_speech import speak


class Engine:
    
    def __init__(self):
        pass
    
    def say(self,audio):
        speak(audio)
        
    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            self.say("Good Morning!")

        elif hour>=12 and hour<18:
            self.say("Good Afternoon!")   

        else:
            self.say("Good Evening!")  

        self.say("I am Vinny. Please tell me how may I help you")
        
    def takeCommand(self):
        #It takes microphone input from the user and returns string output
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration =1)
            audio = r.listen(source)
            r.pause_threshold = 1
            r.energy_threshold = 300
            
            try:    
                print("Recognizing...")    
                query = r.recognize_google(audio, language='en-in')
                print(f"User said: {query}\n")
            
            except Exception as e:  
                self.say("Say that again please...")
                return None
            return query
                     
    def openai(self,Text):
        print(f"User said: {Text}\n")
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt= Text,  
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
            )
        print(response)
        data_raw = response.get('choices')
        
        for i in data_raw:
            data = i.get('text')
            
            self.say(data)


class listen:
    recognize = Engine()
    def __init__(self) -> None:
        pass
    
    def listen(self):
        WAKE = "wake up"
        
        while True:
            
            text = self.recognize.takeCommand()
            
            if(text.count(WAKE)):
                speak("I am Ready")
                text = self.recognize.takeCommand()
                self.recognize.openai(text)
    
    
if __name__ == '__main__':
    run = Engine()
    run.wishMe()
    Hear = listen()
    
    while True:
        try:
            Hear.listen()
        except KeyboardInterrupt:
            sys.exit()