import pyttsx3,os,openai
import json
import openai
import speech_recognition as s
class Engine:
    engine = pyttsx3.init('sapi5')
    
    def __init__(self):
        pass
    
    def speak(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()
  
    def takeCommand(self):
          pass
    def openai(self):
        
        openai.api_key = os.getenv("OPENAI_API_KEY")

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt= "what is gender?",
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
    run.openai()
    



