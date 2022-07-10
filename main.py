import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import spotify
import pywhatkit
import random
import playsound

#---Initialisations & Attributes---
assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
assistant.setProperty('voice', voices[1].id)
name = "Lisa"


#---Speaking Method---
def speak(audio):
   assistant.say(audio)
   assistant.runAndWait()


#---Functions---
def greet():
   time = int(datetime.datetime.now().hour)
   
   if time > 5 and time < 12 or time == 5:
      speak('Good Morning, Bhaavy Soni')
   
   elif time > 12 and time < 18 or time == 12:
      speak('Good Afternoon, Bhaavy Soni')
   
   elif time > 18 and time < 20 or time == 6:
      speak('Good Evening, Bhaavy Soni')

   else:
      speak("hello bhaavya, It's Your Productive Period, wanna grab some coffee?")
      

# takes microphone input and returns string
def takeVoiceInput():
   r = sr.Recognizer()
   
   with sr.Microphone() as source:
      print('Listening...')
      r.energy_threshold = 450
      r.pause_threshold = 0.5
      r.adjust_for_ambient_noise(source, duration=1)
      audio = r.listen(source, phrase_time_limit=4)

   try:
      print('Recognising...')
      query = r.recognize_google(audio, language='en-in').lower()
      print('User-Said:', query)

   except Exception as e:
      print(e)
      print("Speak Again")
      speak("I Beg Your Pardon")
      return "None"

   return query


def keepListening():
   r = sr.Recognizer()
   
   with sr.Microphone() as source:
      print('Idle...')
      r.energy_threshold = 450
      r.pause_threshold = 0.5
      r.adjust_for_ambient_noise(source, duration=1)
      audio = r.listen(source, phrase_time_limit=4)
   
   try:
      print('Understanding...')
      query = r.recognize_google(audio, language='en-in').lower()
      print('User-Said:', query)
   
   except Exception as e:
      print(e)
      return "None"
   
   return query
   

#----Gets Called As Program Starts----
if __name__ == '__main__':
    greet()
    
    while True:
       
       idle = keepListening()
       
       if 'lisa' in idle or 'liza' in idle:
   
          speak('Hello!')
          query = takeVoiceInput()
      
          #---Logic for doing tasks---
          if 'wikipedia' in query:
         
             speak('Searching Wikipedia..')
             query = query.replace('wikipedia', '')
         
             try:
            
                results = wikipedia.summary(query, sentences=2)
                speak('Wikipedia says,')
                speak(results)
                print('According To Wikipedia')
                print(results)
         
             except Exception as e:
            
                print(e)
                speak("Wikipedia Has No Information Regarding That, Bhaavya")
      
          elif 'open youtube' in query or 'play youtube' in query or 'start youtube' in query:
             
             speak('What would you like watch?')
             query = takeVoiceInput()
             pywhatkit.playonyt(query)
      
          elif 'open google' in query:
             webbrowser.open("https://www.google.com")
      
          elif 'open stack overflow' in query:
             webbrowser.open('https://www.stackoverflow.com')
   
          elif 'search' in query or 'search google' in query or 'google' in query:
             
             speak('What Would You Like To Search?')
             query = str(takeVoiceInput().lower())
             pywhatkit.search(query)
             
          elif 'the time' in query:
             
             now = datetime.datetime.now()
             time = now.strftime("%I:%M %p")
             speak(f"Sir, Its {time}")
             print(time)
             
          elif 'pick a number' in query or 'choose a number' in query:
             number = str(random.randint(1, 10))
             speak("As you say sir!")
             speak(f"how about {number}")
             
          elif "what's your name" in query or 'what is your name' in query:
             speak(f"My name is {name}, i'm your personal assistant, always there to help at your fingertips!")
             print(f"My name is {name}, i'm your personal assistant, always there to help at your fingertips!")
             
          elif 'lisa' in query or 'hey lisa' in query:
             playsound.playsound()
             
          elif 'goodnight' in query or 'good night' in query:
             audio_file = os.path.dirname(__file__) + '\yawn.wav'
             playsound.playsound(audio_file)
             speak("Goodnight boss!, sleep well!")
             
          elif 'applause' in query or 'cheer me' in query:
             audio_file = os.path.dirname(__file__) + '/applause.wav'
             playsound.playsound(audio_file)
             
         #elif 'play music':
         
      
    