import pyttsx3

engine = pyttsx3.init('sapi5')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
