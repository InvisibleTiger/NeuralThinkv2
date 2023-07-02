import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 0.8)  # Volume (0.0 to 1.0)
engine.setProperty('voice', voices[1].id)  # Voice
error = "error"

def output(text):
    engine.say(text)
    engine.runAndWait()

def input():
    with mic as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return error
    except sr.RequestError as e:
        return error