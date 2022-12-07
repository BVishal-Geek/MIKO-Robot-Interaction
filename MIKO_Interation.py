import pyttsx3,os,openai
import json
import openai
import speech_recognition as sr
import datetime
import sys
class Engine:
    engine = pyttsx3.init('sapi5')
    
    def __init__(self):
        pass
    
    def speak(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()
        
    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            self.speak("Good Morning!")

        elif hour>=12 and hour<18:
            self.speak("Good Afternoon!")   

        else:
            self.speak("Good Evening!")  

        self.speak("I am Jarvis Sir. Please tell me how may I help you")
        
    def takeCommand(self):
        #It takes microphone input from the user and returns string output
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            # print(f"User said: {query}\n")
            
            # openai(self.query)
        except Exception as e:  
            print("Say that again please...")
            return None
        self.openai(query)
        
        # return query
                
   
      
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
        data_raw = response.get('choices')
        for i in data_raw:
            data = i.get('text')
            self.speak(data)
              
          

if __name__ == '__main__':
    run = Engine()
    run.wishMe()
    
    while True:
        try:
            run.takeCommand()
        except KeyboardInterrupt:
            sys.exit()
            
    



