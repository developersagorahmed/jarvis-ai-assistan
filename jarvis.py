import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser 
import os
import openai
openai.api_key="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"
model_engine="text-davinci-003"




engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening!")
    speak("I am Jarvis sir. Please Tell me how may i help you ")
    
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.
        

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
    
if __name__== "__main__":
    wishMe()
    #while True:
    if 1:
        query=takeCommand().lower()

        if 'wikipedia' in query:
          speak('Searching Wikipedia...')
          query = query.replace("wikipedia", "")
          results = wikipedia.summary(query, sentences=3)
          speak("According to wikipedia")
          print(results)
          speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "play a song" in query:
            webbrowser.open("https://www.youtube.com/watch?v=Qdv2YG9nOsY")
        elif "play a sad song" in query:
            webbrowser.open("https://www.youtube.com/watch?v=JziMpQ1sWo8")
        elif "play a trending song" in query:
            webbrowser.open("https://www.youtube.com/watch?v=ytsVXK1r1eA")
        elif "play a bangla song" in query:
            webbrowser.open("https://www.youtube.com/watch?v=E7PmYS5igP4&list=RDE7PmYS5igP4&start_radio=1")
        elif "play a hindi song" in query:
            webbrowser.open("https://www.youtube.com/watch?v=_iktURk0X-A")
        elif "open google" in query:
            webbrowser.open("www.google.com")
        elif "open stack overflow" in query:
            webbrowser.open("www.stackoverflow.com")
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif "open code" in query:
            codePath="C:\\Users\\Tech Point\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif "hey jarvis" in query:
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=query,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            response = completion.choices[0].text
            print(response)