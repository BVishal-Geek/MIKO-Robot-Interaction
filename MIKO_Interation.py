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
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
        
        except Exception as e:  
            print("Say that again please...")
            return None
        
        # self.list = [i for i in query.split(" ")]
        # print(self.list)
        
        self.openai(query)
                          
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
            
          
if __name__ == '__main__':
    run = Engine()
    run.wishMe()
    
    while True:
        try:
            run.takeCommand()
        except KeyboardInterrupt:
            sys.exit()
            
    



