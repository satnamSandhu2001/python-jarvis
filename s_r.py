import speech_recognition as sr
from speak import speak


def takeCommand():
    # it takes microphone input from the user and returns string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listning...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='en-in')
        print('User said: ', query, '\n')
    except Exception as e:
        print(e)
        print("Pardon, i didn't heard that...")
        # speak("Pardon, i didn't heard that")
        return "None"
    return query
