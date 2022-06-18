import pyttsx3
import datetime
import speech_recognition 
import webbrowser
import os
import time
import winsound
import wikipedia
eng=pyttsx3.init('sapi5')
eng.setProperty("rate", 350)
voices=eng.getProperty('voices')
# print(voices[2].id)
eng.setProperty('voice',voices[1].id)
class Jarvis:
    def speak(self,audio):
        eng.say(audio)
        #eng.runAndWait()#Without this command the speech will not be audible to us
    def wishMe(self):
        hour=int(datetime.datetime.now().hour)
        eng.setProperty("rate", 170)
        if(hour>=0 and hour<12):
            self.speak("Good Morning Boss")
        elif(hour>=12 and hour<18):
            self.speak("Good evening Boss")
        elif(hour>=18 and hour<24):
            if(hour>=22):
                self.speak("Hey boss, Clock Crossed the 10 PM")
                if(hour>=23):
                    self.speak("Boss,Please sleep now,Do remaining work tommorow!")
            
    def takeCommand(self):
        recogniz=speech_recognition.Recognizer()
        winsound.Beep(7000, 500)
        with speech_recognition.Microphone() as source:
            print("Listening  ....")
            recogniz.pause_threshold=0.5
            audio=recogniz.listen(source)
        try:
            print("Recognizing  ....")
            query=recogniz.recognize_google(audio,language='en-in')
            print(query,"\n")
        except :
            winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS) 
            self.speak("Can you repeat ?")
            return "Unknow"
            
        return query

    def takeCommandSleep(self):
        # This is the command function in case of sleep of program ,but it still listening!
        recogniz=speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            recogniz.pause_threshold=0.5
            recogniz.energy_threshold=450
            audio=recogniz.listen(source)
        try:
            query=recogniz.recognize_google(audio,language='en-in')
        except :
            return "Unknow"
            
        return query

    def webService(self):
        while(True):
            query=self.takeCommand()
            query=query.lower()
            reason="Link is not working. Please check" # If link is not working then this is the result
            if( "youtube" in query ):
                try:
                    webbrowser.open("https://www.youtube.com/")
                except:
                    self.speak(reason)
            if( "facebook" in query ):
                try:
                    webbrowser.open("https://www.facebook.com/")
                except:
                    self.speak(reason)
            if( "instagram" in query ):
                try:
                    webbrowser.open("https://www.instagram.com/")
                except:
                    self.speak(reason)
            if( "stack overflow" in query ):
                try:
                    webbrowser.open("https://stackoverflow.com/")
                except:
                    self.speak(reason)
            if( "geeks for geeks" in query ) or ( "gfg" in query ):
                try:
                    webbrowser.open("https://practice.geeksforgeeks.org/topic-tags/#")
                except:
                    self.speak(reason)

            if( "classroom" in query ):
                try:
                    webbrowser.open('https://classroom.google.com/u/1/h')
                except:
                    self.speak(reason)
            if( "code wars" in query ):
                try:
                    webbrowser.open("https://www.codewars.com/dashboard")
                except:
                    self.speak(reason)
            if("wikipedia" in query ):
                self.speak("Searching Wikipedia")
                try:
                    query=query.replace("wikipedia", "")
                    result=wikipedia.summary(query,sentences=3)
                    print(result)
                    self.speak("According to wikipedia " +result)
                    
                except:
                    self.speak("Info not found")

            if "www" in query or "com" in query:
                try:
                    webbrowser.open("http://"+query+"/")
                except:
                    self.speak(reason)
            if( "sleep jarvis" in query  or "sleep" in query):
                self.speak("Sleeping ....")
                while(True):
                    awake=self.takeCommandSleep()
                    awake=awake.lower()
                    if(("wake" in query) or ("active" in awake) or ("awake" in awake)):
                        speech_recognition.Recognizer().energy_threshold=300
                        self.speak("Active and ready sir! ")
                        break
            if "exit" in query or "quit" in query :
                self.speak("Quiting from Web Service ")
                winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
                break
            
        
            
    def systemService(self):
        while(True):
            query=self.takeCommand()
            query=query.lower()
            if "code" in query:
                winsound.Beep(700, 500)
                try:
                    os.startfile("C:\\Users\\HP\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe")
                except:
                    self.speak("Content is not present ,At specified addresss")
            if "whatsapp" in query:
                winsound.Beep(700, 500)
                try:
                    os.startfile("C:\\Users\\HP\\OneDrive\\Desktop\\WhatsApp Desktop.lnk")
                except:
                    self.speak("Content is not present ,At specified addresss")
                
            if ("prime video" in query) or ("open amazon prime" in query):
                winsound.Beep(700, 500)
                try:
                    os.startfile("C:\\Users\\HP\\OneDrive\\Desktop\\Amazon Prime Video for Windows.lnk")
                except:
                    self.speak("Content is not present ,At specified addresss")
            if "discord" in query:
                winsound.Beep(700, 500)
                try:
                    os.startfile("C:\\Users\\HP\\OneDrive\\Desktop\Discord.lnk")
                except:
                    self.speak("Content is not present ,At specified addresss")
            if ("node js" in query) or ("open node" in query):
                winsound.Beep(700, 500)
                try:
                    os.startfile("C:\\Program Files\\nodejs\\node.exe")
                except:
                    self.speak("Content is not present ,At specified addresss")
            if "terminal" in query :
                winsound.Beep(700, 500)
                try:
                    os.startfile("C:\\Users\\HP\\OneDrive\\Desktop\\Windows Terminal.lnk")
                except:
                    self.speak("Content is not present ,At specified addresss")
            if "ubuntu" in query or "linux" in query :
                winsound.Beep(700, 500)
                try:
                    os.startfile("C:\\Users\\HP\\OneDrive\\Desktop\\Ubuntu.lnk")
                except:
                    self.speak("Content is not present ,At specified addresss")
        
            if "music" in query :
                winsound.Beep(700, 500)
                try:
                    os.startfile("C:\\Users\\HP\\OneDrive\\Desktop\\Amazon Music.lnk")
                except:
                    self.speak("Content is not present ,At specified addresss")
            if "camera" in query:
                winsound.Beep(700, 500)
                try:
                    os.startfile("C:\\Users\\HP\\OneDrive\\Desktop\Camera.lnk")
                except:
                    self.speak("Content is not present ,At specified addresss")
            if "clock" in query :
                winsound.Beep(700, 500)
                try:
                    os.startfile("C:\\Users\\HP\\OneDrive\\Desktop\\Clock.lnk")
                except:
                    self.speak("Content is not present ,At specified addresss")
            if "calculator" in query :
                winsound.Beep(700, 500)
                try:
                    os.startfile("C:\\Users\\HP\\OneDrive\\Desktop\\Calculator.lnk")
                except:
                    self.speak("Content is not present ,At specified addresss")
            if "settings" in query :
                winsound.Beep(700, 500)
                try:
                    os.startfile("C:\\Users\\HP\\OneDrive\\Desktop\\Settings.lnk")
                except:
                    self.speak("Content is not present ,At specified addresss")
            if "www" in query or "com" in query:
                try:
                    webbrowser.open("http://"+query)
                except:
                    self.speak("Content is not present ,At specified addresss")
            
            if( "sleep jarvis" in query  or "sleep" in query):
                self.speak("Sleeping ....")
                while(True):
                    awake=self.takeCommandSleep()
                    awake=awake.lower()
                    if(("wake" in query) or ("active" in awake)or ("awake" in awake)):
                        speech_recognition.Recognizer().energy_threshold=300
                        self.speak("Active and ready sir! ")
                        break
            if "exit" in query or "quit" in query :
                self.speak("Quiting from System Service ")
                winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
                break
            

    def study(self):
        while(True):
            query=self.takeCommand()
            query=query.lower()
            if ("toc" in query) or ("theory of computation" in query):
                winsound.Beep(700, 500)
                os.startfile("C:\\Users\\HP\Downloads\\Introduction to automata theory.pdf")

            if ("data structures" in query) or("dsa" in query):
                winsound.Beep(700, 500)
                os.startfile("C:\\Users\\HP\Downloads\\Introduction to algorithms by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein (z-lib.org).pdf")
            if ("statistics" in query) or("math" in query):
                os.startfile("C:\\Users\\HP\\Downloads\\Fundamentals of Mathematical Statistics by S. C. Gupta and V.K. Kapoor.pdf")
            
            if ("os" in query) or ("operating system" in query):
                winsound.Beep(700, 500)
                if("notes" in query):
                    os.startfile("C:\\Users\\HP\\Downloads\\Mod 1_LN.pdf")
                else:
                    os.startfile("C:\\Users\\HP\\Downloads\\lecture1423726024.pdf")
            if( "sleep jarvis" in query  or "sleep" in query):
                self.speak("Sleeping ....")
                while(True):
                    awake=self.takeCommandSleep()
                    awake=awake.lower()
                    if(("wake" in query) or ("active" in awake)or ("awake" in awake)):
                        speech_recognition.Recognizer().energy_threshold=300
                        self.speak("Active and ready sir! ")
                        break
            if ("exit" in query) or ("quit" in query) :
                self.speak("Quiting from Study Service ")
                winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
                break




        
X=Jarvis()
if __name__=="__main__":
    X.wishMe()
    while(True):
        query=X.takeCommand()
        query=query.lower()

        if "study" in query:
            X.speak("Study service onnnnn ")
            X.study()
        if "system" in query:
            X.speak("system service onnnnn")
            X.systemService()
        if( "web service" in query) or ("internet" in query):
            X.speak("Web service onnnnnn")
            X.webService()
        if ("sleep" in query):
            X.speak("Sleep onnnnn")
            time.sleep(300)
            X.speak("Ready and Active")
        if "exit" in query or "quit" in query :
            X.speak("Closing myself")
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
            break
        
