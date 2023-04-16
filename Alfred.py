import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty("voice" , voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    # this is a function used to make alfred speak audio

def wishMe():
    # this is a function used to make alfred wish me based on the time of the day
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")
        
    speak("I am your butler Alfred. How may i be of assistence, sir?")
    
def takeCommand():
    # this is to make alfred take a command
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to your command (⌐■_■)..")
        r.pause_threshold = 1
        r.energy_threshold = 50
        audio = r.listen(source)
    
    try:
        print("Processing..")
        query = r.recognize_google(audio, Language="en-in")
        print(f"You said: {query}\n")

    except Exception as e:
        print("Pardon?..")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    if 1:
        query = takeCommand().lower()
        
        if "wikipedia" in query:
         speak("Looking through Wikipedia..")
         query= query.replace("Wikipedia", " ")
         results= wikipedia.summary(query, sentences=3)
         speak("According to wikipedia")
         print(results)
         speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open spotify" in query:
            webbrowser.open("spotify.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "tell time" in query:
            strtime = datetime.datetime.now.strftime("%H:%M:%S")
            speak(f"The time is {strtime}")