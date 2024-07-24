#---Imports---
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import play_audio


# ---Initialisations & Attributes---
assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
assistant.setProperty('voice', voices[1].id)

name = "Lisa"


def speak(text):
    tts = gTTS(text=text, lang='en')
    audio_file = "output.mp3"
    tts.save(audio_file)

    # Play the sound
    play_audio.play_mp3(audio_file)


# ---Speaking Method---
'''def speak(audio):
    assistant.say(audio)
    assistant.runAndWait()'''


#---Takes microphone input and returns string---
def take_voice_input():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        r.energy_threshold = 450
        r.pause_threshold = 0.8
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
