import pyttsx3
import speech_recognition as sr
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def startup():
    speak('Hello Sir!!! Good morning!!!')
    speak('which muscle part are You going to train today?')


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 1500
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language= 'en-in')
        print('user said: ', query, end='\n')
    except Exception as e:
        # print(e)
        # speak('say that again please!!!')
        return "None"
    return query


def warmup():
    speak('rotate your neck in clockwise')
    time.sleep(5)
    speak('rotate neck in anti-clockwise')
    time.sleep(5)
    speak('rotate head right and left for 5 seconds')
    time.sleep(5)
    speak('rotate heard backward and forward for 5 seconds')
    time.sleep(5)
    speak('Now shoulder rotation  for 10 seconds')
    time.sleep(10)

    lst=list(range(0,301))
    lst=lst[::-1]
    for i in lst:
        speak(i)


def rest(n):
    # lst=range(0,n+1)
    lst = list(range(0,6))
    lst = lst[::-1]
    time.sleep(n - 5)

    for i in lst:
        if i<10:
            speak(i)



def set_rep(n):
    set = n

    speak("Let's start")
    while True:
        query=take_command().lower()
        # pygame.mixer.music.set_volume(0.2)
        if 'done' in query:
            speak('take rest for 45 seconds.')
            rest(45)
            speak("let's go")
            set-=1
        if set==0:
            break


def chest():
    speak('There are 4 exercises we are going to do today. first Around the world fly, second DB press  and Neutral DB press superset, Third Unilateral static fly and at last push ups')

    speak("Lets start with Around the world fly 3 sets of 12 reps each")
    set_rep(3)
    speak("Great!!! we done with first exercise. Take a break for 1 min ")
    rest(60)

    speak("let's start with DB press and Neutral DB press superset")
    speak("3 sets of 12 reps each")
    set_rep(3)
    speak("Great!!! we done with second exercise...take a break for 1 minute")
    rest(60)

    speak("Let's start with our third exercise, Unilateral Static fly")
    speak("3 sets of 12 reps each")
    set_rep(3)
    speak("Great!!! we done with our third exercise. Take a break for 1 minute")
    rest(60)

    speak("Now the last exercise.Do push-ups as much as you can")
    query=take_command().lower()
    if 'done' in query:
        speak('Great sir!!! We done with our chest workout...now do streachase and cool down for 5 min')
        rest(300)
        speak('We done for today!!! ')


def shoulder():

    speak('There are 4 exercises we are going to do today. first is shoulder press, second is Front raises, third one is a super set of latteral raises, upright row, and reverse flyes  then last one is dumbell shrugs')

    speak("Lets start with Shoulder press, 3 sets of 12 reps each")
    set_rep(3)
    speak("Great!!! we done with shoulder press. Take a break for 1 min ")
    rest(60)

    speak("Lets start with our second exercise Front raises, 3 sets of 12 reps each")
    set_rep(3)
    speak("Great!!! we done with front raises. Take a break for 1 min ")
    rest(60)

    speak("now we are going to perform super set of latteral raises, upright row and reverse flyes each of 10 resps considered as one set")
    set_rep(3)
    speak("Great!!! we done with super set. Take a break for 1 min ")
    rest(60)

    speak("Great Sir!!! now last exercise dumbell shrugs, 3 sets of 12 reps each")
    set_rep(30)
    speak('Great sir!!! We done with our shoulder workout...now do streachase and cool down for 5 min')
    rest(300)
    speak('We done for today!!! ')


if __name__ == '__main__':
    speak("Good Morning sir!!! which muscle part you want to train today?")

    while True:
        query = take_command().lower()

        if 'chest' in query:

            speak("Great sir!!! Let's start with warmup")
            warmup()
            speak("nice sir!!! we just completed our warmup, Let's start with chest workout")
            chest()

        if 'shoulder' in query:
            speak("Great sir!!! Let's start with warmup")
            warmup()
            speak("nice sir!!! we just completed our warmup, Let's start with shoulder workout")
            shoulder()



