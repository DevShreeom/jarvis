
import sys
import time
import pyttsx3 #pip install pyttsx3
import speech_recognition   #pip install speechRecognition
import datetime
from playsound import playsound
import webbrowser
import os
import smtplib
import pywhatkit as kit
import requests
from bs4 import BeautifulSoup
import speedtest
import pyautogui  
import pyjokes
import wolframalpha
import random #for random choose
import wikipedia
import cv2
from PyPDF4 import PdfFileReader

from pdf import read_pdf


for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("tt.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")




# ================================ MEMORY ===========================================================================================================

GREETINGS = ["hello jarvis", "jarvis", "wake up jarvis", "you there jarvis", "time to work jarvis", "hey jarvis",
             "ok jarvis", "are you there"]
GREETINGS_RES = [ "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]
#=====================================================================================================================================================


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        speak(random.choice(GREETINGS_RES))

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
        speak(random.choice(GREETINGS_RES))

    else:
        speak("Good Evening!")  
        speak(random.choice(GREETINGS_RES))

def computational_intelligence(question):
    try:
        app_id = "38LYW4-K55X287QVJ"
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None



def takeCommand():
    #It takes microphone input from the user and returns string output

    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Understanding...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query




if __name__ == "__main__":
    wishMe()


while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube")

        elif 'exit' in query:
            speak("good bye sir have a good day")
            sys.exit()
                 
        elif "change password" in query:
            speak("What's the new password")
            new_pw = input("Enter the new password\n")
            new_password = open("password.txt","w")
            new_password.write(new_pw)
            new_password.close()
            speak("Done sir")
            speak(f"Your new password is{new_pw}")
            query = takeCommand().lower()
        
        elif "download"in query:
            speak ("paste the link sir")
            os.startfile('start.py')
                    
        elif ' google' in query:
            speak("opening, google ")
            webbrowser.open("google.com")

        elif ' stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'instagram' in query:
            webbrowser.open("www.instagram.com")
            speak("opening instagram") 

        elif ' facebook' in query:
            webbrowser.open("www.facebook.com")
            speak("opening facebook")

        elif 'thanks' in query:
            speak("it's my work sir")

        elif ' time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'gmail' in query:
            webbrowser.open('gmail.com')
            speak("opening GMAIL")

        elif 'fine'  in query:
            speak("IT's good to hear from you ,SIR")

        elif 'google search' in query:
           import wikipedia as googleScrap
           query = query.replace("jarvis","")
           query = query.replace("google search","")
           query = query.replace("google","")
           speak("THIS IS WHAT I FOUNDON THE WEB!")

           try:
               result = googleScrap.summary(query,3)
               speak(result)

           except:
                speak("no speakable data aviable")   
      
        elif 'instagram message' in query:
            speak("ok, SIR")
            webbrowser.open('instagram.com')

        elif 'alarm' in query:
            speak("Enter the Time!")
            time = input(": Enter the time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now =Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("time to wake up SIR")
                    playsound('alarm.mp3')
                    speak("Alarm closed!")


                elif now>time:
                    break    

        elif "remember " in query:
            rememberMessage = query.replace("jarvis","")
            rememberMessage = query.replace("remember that","")
            rememberMessage = query.replace("remember ","")
            speak("You told me to remember that"+rememberMessage)
            remember = open("Remember.txt","a")
            remember.write(rememberMessage)
            remember.close()

        elif "what do you remember" in query:
            remember = open("Remember.txt","r")
            speak("You told me to remember that" + remember.read())

        elif 'drive'in query:
            webbrowser.open("https://drive.google.com")
            speak("opening google drive")

        elif 'FEELING' in query:
            speak("i am felling good as regular")

        elif'like movie' in query:
            speak("Yes, but i only wahtch M C U movies")

        elif'scared' in query:
            speak("keep clam ,SIR")
            webbrowser.open('https://www.youtube.com/watch?v=D8hF5uSP3u8')
            
        
#YOUTUBE==================================================================================
        elif "pause video" in query:
             pyautogui.press("k")
             speak("video paused")
        elif "start " in query:
             pyautogui.press("k")
             speak("video played")

        elif "mute" in query:
             pyautogui.press("m")
             speak("video muted")

        elif"full screen"in query:
            pyautogui.press("f")
            speak("fullscrren mode ")

        elif"maximize"in query:
            pyautogui.press("f")
            speak("fullscrren mode ")

        elif"minimize"in query:
            pyautogui.press("f")
            speak("fullscrren mode ")


        elif "volume up" in query:
            from keyboard import volumeup
            speak("Turning volume up,sir")
            volumeup()
        elif "volume down" in query:
            from keyboard import volumedown
            speak("Turning volume down, sir")
            volumedown()
#==============================================================================================
        elif "calculate" in query:
            from Calculatenumbers import WolfRamAlpha
            from Calculatenumbers import Calc
            query = query.replace("calculate","")
            query = query.replace("jarvis","")
            Calc(query)
        
        elif "news" in query:
          from Newz_tell import latestnews
          latestnews()

        elif "shutdown" in query:
             speak("Are You sure you want to shutdown")
             shutdown = input("Do you wish to shutdown your computer? (yes/no)")
             if shutdown == "yes":
                os.system("shutdown /s /t 1")

             elif shutdown == "no":
              break
   
        elif "how are you" in query:
                    speak("Perfect, SIR")
                
        elif "thank you" in query:
                    speak("you are welcome, SIR")

        elif "weather" in query:
            search = "weather in beed"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")
  
        elif "temperature" in query:
            search = "temperature in beed"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")

        elif " photo" in query:
                    
                    speak("taking photo")
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    cap = cv2.VideoCapture(0)
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

        elif "ipl score" in query:
                    from plyer import notification  #pip install plyer
                    import requests #pip install requests
                    from bs4 import BeautifulSoup #pip install bs4
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )

        elif "internet speed" in query:
            import speedtest
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"Sir, we have{dl} bit per second downloading speed , And {up} bit per second uploading speed  ")
                    
        elif "change  window"  in query:
                speak("Okay SIR, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

        elif "youtube" in query:
            from Function import searchYoutube
            searchYoutube(query)

        elif "screenshot" in query:
                     speak("taking screenshot of current window")
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
        
        elif "game" in query:
                    from Function import game_play
                    game_play()

        elif "bored" in query:
            speak("lets'play a game")
            from Function import game_play
            game_play()

        elif "launch" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.press("enter")   
        
        elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)
        
        elif "switch the window" in query or "switch window" in query:
                speak("Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
            
        elif "where i am" in query or "current location" in query or "where am i" in query:
                try:
                    city, state, country = object.my_location()
                    print(city, state, country)
                    speak(
                        f"You are currently in {city} city which is in {state} state and country {country}")
                except Exception as e:
                    speak(
                        "Sorry sir, I coundn't fetch your current location. Please try again")

        elif "goodbye" in query or "offline" in query or "bye" in query:
                speak("Alright sir, going offline. It was nice working with you")
                sys.exit() 

        elif "ip address" in query:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                speak(f"Your ip address is {ip}")

        elif "joke" in query:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)
 
        elif "make a note" in query or "write this down" in query or "remember this" in query:
                speak("What would you like me to write down?")
                note_text = object.mic_input()
                object.take_note(note_text)
                speak("I've made a note of that")

        elif "close the note" in query or "close notepad" in query:
                speak("Okay sir, closing notepad")
                os.system("taskkill /f /im notepad++.exe")
        
        elif "what is" in query or "who is" in query:
                question = query
                answer = computational_intelligence(question)
                speak(answer)
       
        elif "tired" in query or " song" in query:
            speak("Playing your favourite songs, sir")
            a = (1,2,3,4,5,6,7,8,9,10,11,12,13) 
            b = random.choice(a)
            if b==1:
                webbrowser.open("https://www.youtube.com/watch?v=kTJczUoc26U&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=1")
            if b==2:
                webbrowser.open("https://www.youtube.com/watch?v=kffacxfA7G4&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=2")
            if b==3:
                webbrowser.open("https://www.youtube.com/watch?v=JGwWNGJdvx8&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=3")
            if b==4:
                webbrowser.open("https://www.youtube.com/watch?v=jzD_yyEcp0M&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=4")
            if b==5:
                webbrowser.open("https://www.youtube.com/watch?v=aJOTlE1K90k&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=5")
            if b==6:
                webbrowser.open("https://www.youtube.com/watch?v=q0hyYWKXF0Q&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=6")
            if b==7:
                webbrowser.open("https://www.youtube.com/watch?v=q0hyYWKXF0Q&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=7")
            if b==8:
                webbrowser.open("https://www.youtube.com/watch?v=q0hyYWKXF0Q&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=8")
            if b==9:
                webbrowser.open("https://www.youtube.com/watch?v=q0hyYWKXF0Q&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=9")
            if b==10:
                webbrowser.open("https://www.youtube.com/watch?v=q0hyYWKXF0Q&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=10")
            if b==11:
                webbrowser.open("https://www.youtube.com/watch?v=q0hyYWKXF0Q&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=11")
            if b==12:
                webbrowser.open("https://www.youtube.com/watch?v=q0hyYWKXF0Q&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=12")
            if b==13:
                webbrowser.open("https://www.youtube.com/watch?v=q0hyYWKXF0Q&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=13")

        elif "music" in query or " song" in query:
            speak("Playing your favourite songs, sir")
            a = (1,2,3,4,5,6,7,8,9,10,11,12,13) 
            b = random.choice(a)
            if b==1:
                webbrowser.open("https://www.youtube.com/watch?v=kTJczUoc26U&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=1")
            if b==2:
                webbrowser.open("https://www.youtube.com/watch?v=kffacxfA7G4&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=2")
            if b==3:
                webbrowser.open("https://www.youtube.com/watch?v=JGwWNGJdvx8&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=3")
            if b==4:
                webbrowser.open("https://www.youtube.com/watch?v=jzD_yyEcp0M&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=4")
            if b==5:
                webbrowser.open("https://www.youtube.com/watch?v=aJOTlE1K90k&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=5")
            if b==6:
                webbrowser.open("https://www.youtube.com/watch?v=q0hyYWKXF0Q&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=6")
            if b==7:
                webbrowser.open("https://www.youtube.com/watch?v=q0hyYWKXF0Q&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=7")
            if b==8:
                webbrowser.open("https://www.youtube.com/watch?v=q0hyYWKXF0Q&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=8")
            if b==9:
                webbrowser.open("https://www.youtube.com/watch?v=q0hyYWKXF0Q&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=9")
            if b==10:
                webbrowser.open("https://www.youtube.com/watch?v=q0hyYWKXF0Q&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=10")
            if b==11:
                webbrowser.open("https://www.youtube.com/watch?v=q0hyYWKXF0Q&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=11")
            if b==12:
                webbrowser.open("https://www.youtube.com/watch?v=q0hyYWKXF0Q&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=12")
            if b==13:
                webbrowser.open("https://www.youtube.com/watch?v=q0hyYWKXF0Q&list=PLiCyD_T8QEUIyKrakS1nuj7dT6qb_8MsC&index=13")

        elif "send massage" in query:
            speak("what should i say")
            msz = takeCommand()

            from twilio.rest import Client

            # and set the environment variables. See http://twil.io/secure
            account_sid = os.environ['AC9acb150c337ee36a5a9fcd148f1e0d8d']
            auth_token = os.environ['7b78f78dcac68b3b41cd2136488fc4fa']
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                    body='McAvoy or Stewart? These timelines can get so confusing.',
                    from_='+14055616707',
                    status_callback='http://postb.in/1234abcd',
                    to='+919561208409'
                )

            print(message.sid)

 
            

            

                