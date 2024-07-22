# ---Imports---
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
#import spotify
import pywhatkit
import random
import play_audio

# ---Initialisations & Attributes---
assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
assistant.setProperty('voice', voices[1].id)
name = "Lisa"


# ---Speaking Method---
def speak(audio):
    assistant.say(audio)
    assistant.runAndWait()


# ---Functions---
def greet():
    current_time = int(datetime.datetime.now().hour)

    if 5 <= current_time < 12:
        speak('Good Morning, Bhaavy Soni')

    elif 12 <= current_time < 18:
        speak('Good Afternoon, Bhaavy Soni')

    elif 18 < current_time < 20 or current_time == 6:
        speak('Good Evening, Bhaavy Soni')

    else:
        speak("hello bhaavya, It's Your Productive Period, wanna grab some coffee?")


# takes microphone input and returns string
def take_voice_input():
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


# --keep listening/Idle
def keep_listening():
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


# ----Gets Called As Program Starts----
if __name__ == '__main__':
    greet()

    while True:

        idle = keep_listening()

        # ---Waking the Bot Up---
        if 'lisa' in idle or 'liza' in idle:

            speak('Hello!')
            query = take_voice_input()

            # ---Logic for doing tasks---
            # ---Wikipedia Search---
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

            # ---Searching Youtube---
            elif 'search youtube' in query or 'play youtube' in query:

                speak('What would you like watch?')
                query = take_voice_input()
                pywhatkit.playonyt(query)

            # ---Opening Yt---
            elif 'open youtube' in query or 'start youtube' in query:
                webbrowser.open("https://www.youtube.com")

            # ---Opening Google---
            elif 'open google' in query or 'start google' in query:
                webbrowser.open("https://www.google.com")

            # ---Opening Stackoverflow---
            elif 'open stack overflow' in query:
                webbrowser.open('https://www.stackoverflow.com')

            # ---Searching Google---
            elif 'search' in query or 'search google' in query or 'google' in query:

                speak('What Would You Like To Search?')
                query = str(take_voice_input().lower())
                pywhatkit.search(query)

            # ---Telling Time---
            elif 'the time' in query:

                now = datetime.datetime.now()
                time = now.strftime("%I:%M %p")
                speak(f"Sir, Its {time}")
                print(time)

            # ---Picking A Number---
            elif 'pick a number' in query or 'choose a number' in query:

                number = str(random.randint(1, 10))
                speak("As you say sir!")
                speak(f"how about {number}")

            # ---Her Name---
            elif "your name" in query or 'who are you' in query:
                speak(f"My name is {name}, i'm your personal assistant, always there to help at your fingertips!")
                print(f"My name is {name}, i'm your personal assistant, always there to help at your fingertips!")

            # ---Something---
            elif 'lisa' in query or 'hey lisa' in query or 'hello' in query:
                speak('Hello!')

            # ---Wishing Goodnight---
            elif 'goodnight' in query or 'good night' in query:
                audio_file = os.path.join(os.path.dirname(__file__), 'sounds', 'yawn.wav')
                play_audio.play_audio(audio_file)
                speak("Goodnight boss!, sleep well!")

            # ---Applause---
            elif 'applause' in query or 'cheer me' in query:
                audio_file = os.path.join(os.path.dirname(__file__), 'sounds', 'applause.wav')
                play_audio.play_audio(audio_file)

            # ---My Name---
            elif "my name" in query or 'who am i' in query:
                speak(f"Your name is Bhaavy Soni, You're My Creator & Boss")
