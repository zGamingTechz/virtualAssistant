# ---Imports---
import datetime
import wikipedia
import os
import webbrowser
import pywhatkit
import random
import play_audio
from essential_functions import speak, name, take_voice_input
import ai_chat


# ---Functions---
def greet():
    current_time = datetime.datetime.now().hour

    if 5 <= current_time < 12:
        greeting = random.choice([
            'Good Morning, Bhaavy Soni! Ready to seize the day?',
            'Morning, Bhaavy Soni! Let’s make today amazing!',
            'Good Morning, Bhaavy! What’s on today’s agenda?'
        ])
    elif 12 <= current_time < 18:
        greeting = random.choice([
            'Good Afternoon, Bhavy Soni! Hope your day is going well.',
            'Afternoon, Bhavy! What can I assist you with?',
            'Good Afternoon, Bhavy! Let’s continue being productive.'
        ])
    elif 18 <= current_time < 20:
        greeting = random.choice([
            'Good Evening, Bhavy Soni! How was your day?',
            'Evening, Bhavy! Need help with anything tonight?',
            'Good Evening, Bhavy! Let’s wrap up the day’s tasks.'
        ])
    else:
        greeting = random.choice([
            'Hello Bhavy, it’s your productive period. Wanna grab some coffee?',
            'Hi Bhavy! It’s a great time to get things done. Need any help?',
            'Hello Bhavy! Let’s make the most of your productive period.'
        ])

    speak(greeting)


def lisa_functions(query):
    # ---Logic for doing tasks---

    # ---Wikipedia Search---
    if any(word in query.lower() for word in ['wikipedia', 'wiki']):

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
            speak("Wikipedia Has No Information Regarding That, Bhavy")

    # ---Searching Youtube---
    elif any(word in query.lower() for word in ['search youtube', 'play youtube']):

        speak('What would you like watch?')
        query = take_voice_input()
        pywhatkit.playonyt(query)

    # ---Opening Yt---
    elif 'open youtube' in query or 'start youtube' in query:
        webbrowser.open("https://www.youtube.com")

    # ---Opening Google---
    elif 'open google' in query or 'start google' in query:
        webbrowser.open("https://www.google.com")

    # ---Searching Google---
    elif any(word in query.lower() for word in ['google', 'search']):
        query = query.replace('google', '').replace('search', '')
        pywhatkit.search(query)

    # ---Opening Stackoverflow---
    elif 'open stack overflow' in query:
        webbrowser.open('https://www.stackoverflow.com')

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
        speak(f"Your name is Bhavy Soni, You're My Creator & Boss")

    # ---AI Chat---
    else:
        response = ai_chat.chat(query)
        speak(response)
        print("Lisa said: ", response)
