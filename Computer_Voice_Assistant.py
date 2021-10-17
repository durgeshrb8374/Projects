import datetime
import os
import sys

import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import pywhatkit as kit
import pyautogui
import time





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    # hour = int(datetime.datetime.now().hour)
    # if 0 <= hour < 12:
    #     speak('Good Morning!')
    # elif 12 <= hour < 17:
    #     speak('Good afternoon!')
    # elif 17 <= hour < 20:
    #     speak('good evening!')
    # else:
    #     speak('good night')
    speak('Hello sir!! Jarvis 2.0 is loaded')


def take_command():
    # it takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        r.energy_threshold = 1500
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print('user said: ', query, end='\n')
    except Exception as e:
        # print(e)
        # speak('say that again please!!!')
        return "None"
    return query


if __name__ == '__main__':

    wishme()
    while True:
        query = take_command().lower()
        if 'jarvis stop' in query:
            speak("are u sure sir...want to quit jarvis?")
            query = take_command().lower()
            if 'yes' in query:
                speak('have a nice day sir!!! bye bye')
                break

        elif 'jarvis' in query:
            speak("yes sir!")
            while True:
                query = take_command().lower()


        #logic for tasks based on query:
                if 'search for' in query:
                    speak('Searching sir...')   #insisde wikipedia
                    query = query.replace("search for", "")
                    # print(query)
                    results = wikipedia.summary(query,sentences=2)
                    speak("searching wikipedia")
                    speak('According to wikipedia')
                    speak(results)
                    break
                elif 'on youtube' in query:
                    results = query.replace("on youtube","")
                    #https://www.youtube.com/results?search_query=kalank
                    search = "www.youtube.com/results?search_query=" + results
                    webbrowser.open(search)
                    break
                elif 'open google' in query:

                    speak("what do you want to search sir?")
                    query = take_command().lower()
                    search = "https://www.google.com/search?q="+query
                    webbrowser.open(search)
                    break
                elif 'close google' in query:
                    speak("closing google")
                    os.system("taskkill /f /im chrome.exe")

                elif 'open notepad' in query:
                    codepath= "C:\\WINDOWS\\system32\\notepad.exe"
                    os.startfile(codepath)
                elif 'close notepad' in query:
                    speak('Ok sir, closing notepad')
                    os.system("taskkill /f /im notepad.exe")

                elif 'open command prompt' in query:
                    codepath = "start cmd"
                    os.startfile((codepath))
                elif 'close command prompt' in query:
                    speak("ok sir, closing command prompt")
                    os.system("taskkill /f /im notepad")

                elif 'play music' in query:
                    music_dir = "E:\\music"
                    songs = os.listdir(music_dir)
                    rd = random.choice(songs)
                    os.startfile(os.path.join(music_dir, rd))

                elif 'open hackerrank' in query:
                    webbrowser.open("www.hackerrank.com")

                elif 'open youtube' in query:
                    speak("what should I play on youtube")
                    query = take_command().lower()
                    speak("playing sir")
                    kit.playonyt(query)
                elif 'close youtube' in query:
                    speak("closing youtube")
                    os.system("taskkill /f /im chrome.exe")

                elif 'shutdown the system' in query:
                    os.system("shutdown /s /t 5")

                elif 'restart the system' in query:
                    os.system("restart /r /t 5")

                elif 'sleep the system' in query:
                    os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")

                elif 'switch the window' in query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")

                    time.sleep(1)
                    pyautogui.keyUp("alt")

                elif 'jarvis quit' in query:
                    sys.exit()






