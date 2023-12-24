import datetime
from speak import speak
from s_r import takeCommand
import webbrowser
import os

chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register(
    'chrome', None, webbrowser.BackgroundBrowser(chrome_path))


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print('Good morning sir!')
        speak('Good morning sir')
    elif hour >= 12 and hour < 18:
        print('Good afternoon sir!')
        speak('Good afternoon sir')
    else:
        print('Good evening sir!')
        speak('Good evening sir')
    print('I am ready at your service How may i help you...')
    speak('I am ready at your service How may i help you')


if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
        if 'shut down' in query or 'shutdown' in query:
            speak('bye sir, have a good day')
            break
            exit()
        if 'open youtube' in query:
            speak('Opening youtube')
            webbrowser.get('chrome').open_new_tab('youtube.com')
        elif 'search music' in query:
            speak('hold a second...')
            query = query.split('search')
            print(query)
            webbrowser.get('chrome').open_new_tab(
                f"http://www.youtube.com/results?search_query={query[1].replace(' ', '+')}")
        elif 'open google' in query:
            speak('Opening google')
            webbrowser.get('chrome').open_new_tab('google.com')
        elif 'search google' in query:
            speak('Searching google')
            webbrowser.get('chrome').open_new_tab(
                f"https://www.google.com/search?q={query.replace(' ', '+')}")
        elif 'open stack overflow' in query:
            speak('Opening stack overflow')
            webbrowser.get('chrome').open_new_tab('stackoverflow.com')
        elif 'open digital peakers' in query or 'open digital speakers' in query or 'open digital speaker' in query:
            speak('Opening digital peakers')
            webbrowser.get('chrome').open_new_tab('digitalpeakers.com')
        elif 'open vs code' in query:
            speak('Opening vs code')
            vscode_path = "C:\\Users\\cypher\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscode_path)
        elif 'open cmd' in query:
            speak('Opening cmd')
            cmd_path = "C:\\Windows\\system32\\cmd.exe"
            os.startfile(cmd_path)
