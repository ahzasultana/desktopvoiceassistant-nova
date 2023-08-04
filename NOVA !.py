import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am NOVA, a virtual voice assistant"  "Sir! How may I assist you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)
        return query.lower()

    except Exception as e:
        print("Say that again, please...")
        return "None"


wishme()

if __name__ == "__main__":
    while True:
        query = takecommand()

        if "wikipedia" in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
            break

        elif "your name" in query:
            speak("My name is NOVA")

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            break

        elif "open google" in query:
            webbrowser.open("https://www.google.com")
            break

        elif "exit" in query:
            speak("Thank you for using me as your assistant. You can call me anytime you need my help. Goodbye!")
            break

        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {time}")
            break

        elif "open notepad" in query:
            path = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(path)
            break
        
        elif "had your dinner" in query and "nova" in query:
            speak("No, I am a virtual assistant. I can't eat anything. But did you have your dinner?")
        
        elif "yes, I had my dinner" in query:
            speak("That's great to hear!")
        
        elif "no, I didn't have my dinner" in query:
            speak("Why not? You should have your food. It's important not to skip your meals.")

        elif "who is your best friend" in query and "nova" in query:
            speak("Zoya and Bushra")

        elif "tell me about yourself" in query and "nova" in query:
            speak("I am a virtual assistant (VA) that is a software agent capable of performing a range of tasks or services for you based on your input, such as commands or questions, including oral ones. These technologies often incorporate chatbot capabilities to simulate conversation, such as via online chat, to facilitate interaction with you.")

        elif "say hello to our respected guide" in query and "nova" in query:
            speak("")

        elif "what can you do" in query:
            speak("I can open YouTube, Notepad, tell you the date and time, search queries on Wikipedia, and provide information about myself. Feel free to ask!")

        else:
            speak("I'm sorry, I didn't understand. Can you please repeat your command?")
