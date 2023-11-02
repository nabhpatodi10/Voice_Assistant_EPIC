import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import subprocess as sp
import psutil
import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog as fd
import wolframalpha
import requests, json
import random
from time import strftime
from PIL import Image, ImageTk
from geopy.geocoders import Nominatim
import winsound
import pyjokes
import random_poem
import pickle
import platform
import keyboard

try:
    import mysql.connector
except:
    messagebox.showinfo("Error", "Please Install MySQL 5.0 or above.\nUse the following link to download the setup file:\nhttps://dev.mysql.com/downloads/installer/")

def Login_Function():

    cursor = db_connection.cursor()

    cursor.execute("create database if not exists epic")
    db_connection.commit()

    cursor.execute("use epic")

    cursor.execute("create table if not exists alarms (Time varchar(10), Monday varchar(3), Tuesday varchar(3), Wednesday varchar(3), Thursday varchar(3), Friday varchar(3), Saturday varchar(3), Sunday varchar(3))")
    db_connection.commit()

    cursor.execute("create table if not exists applications (Applications varchar(50), Path varchar(500))")
    db_connection.commit()

    cursor.execute("create table if not exists chat_history (Date varchar(12), Time varchar(15), Chat_User varchar(150), Chat_EPIC varchar(1000))")
    db_connection.commit()

    cursor.execute("create table if not exists login (User_Name varchar(25) not null primary key, Passwrd varchar(25) not null, Owner_Name varchar(25) not null)")
    db_connection.commit()

    if platform.system()=="Windows":
        cursor.execute("select * from applications")
        check=cursor.fetchall()
        if len(check)==0:
            cursor.execute("insert into applications values ('Notepad', 'Notepad.exe')")
            cursor.execute("insert into applications values ('Command Prompt', 'C:/WINDOWS/system32/cmd')")
            cursor.execute("insert into applications values ('cmd', 'C:/WINDOWS/system32/cmd')")
            cursor.execute("insert into applications values ('CMD', 'C:/WINDOWS/system32/cmd')")
            cursor.execute("insert into applications values ('Calculator', 'C:/WINDOWS/system32/calc')")
            db_connection.commit()

    sql_select="select * from login"
    cursor.execute(sql_select)
    records=cursor.fetchall()

    if len(records)==0:

        root_signup=Tk()
        root_signup.title("EPIC")
        root_signup.attributes('-fullscreen', True)

        class Example(Frame):
            def __init__(self, master, *pargs):
                Frame.__init__(self, master, *pargs)

                self.image = Image.open("SignUp_BG.png")
                self.img_copy= self.image.copy()

                self.background_image = ImageTk.PhotoImage(self.image)

                self.background = Label(self, image=self.background_image)
                self.background.pack(fill=BOTH, expand=YES)
                self.background.bind('<Configure>', self._resize_image)

            def _resize_image(self,event):

                new_width = event.width
                new_height = event.height

                self.image = self.img_copy.resize((new_width, new_height))

                self.background_image = ImageTk.PhotoImage(self.image)
                self.background.configure(image =  self.background_image)

        e = Example(root_signup)
        e.pack(fill=BOTH, expand=YES)

        new_username_var=StringVar()
        new_password_var=StringVar()
        new_ownername_var=StringVar()

        user_name_entry=Entry(root_signup, width=18, textvariable=new_username_var, font=("Avengeance Heroic Avenger Italic", 20), foreground="Cyan", background="Gray7", insertbackground="White")
        password_entry=Entry(root_signup, width=23, textvariable=new_password_var, font=("Avengeance Heroic Avenger Italic", 20), foreground="Cyan", background="Gray7", insertbackground="White", show="*")
        ownername_entry=Entry(root_signup, width=18, textvariable=new_ownername_var, font=("Avengeance Heroic Avenger Italic", 20), foreground="Cyan", background="Gray7", insertbackground="White")

        def SignUp():
            cursor.execute(f"INSERT INTO login VALUES ('{new_username_var.get()}', '{new_password_var.get()}', '{new_ownername_var.get()}');")
            db_connection.commit()
            root_signup.destroy()
            Login_Function()
            
        signup_button=Button(root_signup, text="Sign Up", font=("Avengero Regular", 18), foreground="Cyan", background="Gray7", command=SignUp)

        user_name_entry.place(relheight=0.043, relwidth=0.223, relx=0.462, rely=0.439)
        password_entry.place(relheight=0.043, relwidth=0.223, relx=0.462, rely=0.519)
        ownername_entry.place(relheight=0.043, relwidth=0.223, relx=0.462, rely=0.599)
        signup_button.place(relheight=0.045, relwidth=0.09, relx=0.45, rely=0.68)

        root_signup.mainloop()

    else:

        root=Tk()
        root.title("EPIC")
        root.attributes('-fullscreen', True)

        class Example(Frame):
            def __init__(self, master, *pargs):
                Frame.__init__(self, master, *pargs)

                self.image = Image.open("Login_BG.png")
                self.img_copy= self.image.copy()

                self.background_image = ImageTk.PhotoImage(self.image)

                self.background = Label(self, image=self.background_image)
                self.background.pack(fill=BOTH, expand=YES)
                self.background.bind('<Configure>', self._resize_image)

            def _resize_image(self,event):

                new_width = event.width
                new_height = event.height

                self.image = self.img_copy.resize((new_width, new_height))

                self.background_image = ImageTk.PhotoImage(self.image)
                self.background.configure(image =  self.background_image)

        e = Example(root)
        e.pack(fill=BOTH, expand=YES)

        username_var=StringVar()
        password_var=StringVar()

        def Login():
            for i in records:
                if username_var.get()==i[0] and password_var.get()==i[1]:
                    global owner
                    owner=i[2]
                    root.destroy()

                    def Main_Function():

                        root_1=Tk()
                        root_1.title("EPIC")
                        root_1.attributes('-fullscreen', True)

                        class Example(Frame):
                            def __init__(self, master, *pargs):
                                Frame.__init__(self, master, *pargs)
                                self.image = Image.open("Background_EPIC.png")
                                self.img_copy= self.image.copy()

                                self.background_image = ImageTk.PhotoImage(self.image)

                                self.background = Label(self, image=self.background_image)
                                self.background.pack(fill=BOTH, expand=YES)
                                self.background.bind('<Configure>', self._resize_image)

                            def _resize_image(self,event):

                                new_width = event.width
                                new_height = event.height

                                self.image = self.img_copy.resize((new_width, new_height))

                                self.background_image = ImageTk.PhotoImage(self.image)
                                self.background.configure(image =  self.background_image)

                        e = Example(root_1)
                        e.pack(fill=BOTH, expand=YES)

                        text_task_var=StringVar()

                        def TIME():
                            string = strftime('%H:%M:%S')
                            time_label.config(text = string)
                            time_label.after(1000, TIME)

                        time_label=Label(root_1, background="gray4", foreground="cyan", font=("Avengeance Heroic Avenger Italic", 20))
                        time_label.place(relheight=0.04, relwidth=0.08, relx=0.043, rely=0.16)
                        TIME()
                        
                        def Date():
                            now=datetime.datetime.now()
                            date_label.config(text=str(now.day)+"/"+str(now.month)+"/"+str(now.year))
                            date_label.after(1000, Date)

                        date_label=Label(root_1, background="gray4", foreground="cyan", font=("Avengeance Heroic Avenger Italic", 20))
                        date_label.place(relheight=0.04, relwidth=0.085, relx=0.043, rely=0.07)
                        Date()
                        TIME()

                        global week_days
                        week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

                        def Day():
                            now=datetime.datetime.now()
                            week_num=datetime.date(now.year, now.month, now.day).weekday()
                            DAY=week_days[week_num]
                            day_label.config(text=DAY)
                            day_label.after(1000, Day)

                        day_label=Label(root_1, background="gray4", foreground="cyan", font=("Avengeance Heroic Avenger Italic", 20))
                        day_label.place(relheight=0.04, relwidth=0.1, relx=0.034, rely=0.115)
                        Day()
                        TIME()

                        def Battery():
                            battery = psutil.sensors_battery()
                            BAT="Battery\n"+str(battery.percent)+"%"
                            bat_label.config(text=BAT)
                            bat_label.after(1000, Battery)

                        bat_label=Label(root_1, background="gray4", foreground="cyan", font=("Avengeance Heroic Avenger Italic", 15))
                        bat_label.place(relheight=0.07, relwidth=0.05, relx=0.057, rely=0.329)
                        Battery()
                        TIME()

                        def ram():
                            RAM="RAM\n"+str(psutil.virtual_memory()[2])+"%"
                            ram_label.config(text=RAM)
                            ram_label.after(1000, ram)

                        ram_label=Label(root_1, background="gray4", foreground="cyan", font=("Avengeance Heroic Avenger Italic", 13))
                        ram_label.place(relheight=0.05, relwidth=0.04, relx=0.0625, rely=0.555)
                        ram()
                        TIME()

                        def cpu():
                            CPU="CPU\n"+str(psutil.cpu_percent(1))+"%"
                            cpu_label.config(text=CPU)
                            cpu_label.after(350, cpu)

                        cpu_label=Label(root_1, background="gray4", foreground="cyan", font=("Avengeance Heroic Avenger Italic", 13))
                        cpu_label.place(relheight=0.05, relwidth=0.038, relx=0.063, rely=0.5)
                        cpu()
                        TIME()

                        def news():
                            url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=31b7582d2bbe45dcb3dd0c64cf978c08')
                                        
                            try:
                                response = requests.get(url)

                                global News
                                News = json.loads(response.text)
                                        
                                n=0
                                l=[]
                                for new in News['articles']:
                                    n+=1
                                    l.append(str(new['title']))
                                    l.append(str(new['description']))
                                    if n>=2:
                                        break
                                NEWS=l[0]+"\n"+l[1]+"\n\n"+l[2]+"\n"+l[3]
                                news_label.config(text=NEWS, font=("Avengeance Heroic Avenger Italic", 7))
                                news_label.place(relheight=0.12, relwidth=0.355, relx=0.6235, rely=0.839)
                                news_label.after(3600000, news)

                            except:
                                news_label.config(text="Please Check your Internet Connection!", font=("Avengeance Heroic Avenger Italic", 13))
                                news_label.place(relheight=0.04, relwidth=0.355, relx=0.6235, rely=0.88)
                                news_label.after(1000, news)

                        news_label=Label(root_1, background="gray5", foreground="cyan", font=("Avengeance Heroic Avenger Italic", 7), wraplength=545, justify=LEFT)
                        news_label.place(relheight=0.12, relwidth=0.355, relx=0.6235, rely=0.839)
                        news()
                        TIME()

                        def location():
                            try:
                                res = requests.get("https://ipinfo.io/")
                                data = res.json()

                                locate = data['loc']
                                locate1 = locate.split(',')

                                lat = str(locate1[1])
                                log = str(locate1[0])

                                geolocator = Nominatim(user_agent="geoapiExercises")

                                Location = geolocator.geocode(log+","+lat)

                                global loc_list
                                loc_list=str(Location).split(", ")
                                le=len(loc_list)-1

                                loc_label.config(text=loc_list[le-3]+", "+loc_list[le-2], font=("Avengeance Heroic Avenger Italic", 20))
                                loc_label.place(relheight=0.05, relwidth=0.23, relx=0.562, rely=0.06)
                                loc_label.after(600000, location)
                            
                            except:
                                loc_label.config(text="Please Check your Internet Connection!", font=("Avengeance Heroic Avenger Italic", 13))
                                loc_label.place(relheight=0.05, relwidth=0.23, relx=0.562, rely=0.06)
                                loc_label.after(1000, location)

                        info_label=Label(root_1, background="gray5", foreground="cyan", font=("Avengeance Heroic Avenger Italic", 10), wraplength=800, justify=LEFT)
                        info_label.place(relheight=0.12, relwidth=0.53, relx=0.0246, rely=0.839)

                        loc_label=Label(root_1, background="gray5", foreground="cyan", font=("Avengeance Heroic Avenger Italic", 20))
                        loc_label.place(relheight=0.05, relwidth=0.23, relx=0.562, rely=0.06)
                        location()
                        TIME()

                        def weather():
                            try:
                                le=len(loc_list)-3
                                w=loc_list[le]
                                w=w.lower()

                                url = "http://api.openweathermap.org/data/2.5/weather?appid=f9dfb38f333f20d990fe58bb4135575e&q="+w
                                response = requests.get(url)
                                x = response.json()

                                if x["cod"] != "404":
                                    y = x["main"]
                                    current_temperature = int(y["temp"])-273
                                    current_pressure = y["pressure"]
                                    current_humidiy = y["humidity"]
                                    z = x["weather"]
                                    weather_description = z[0]["description"]
                                
                                WEATHER="Weather\n\nTemperature:\n "+str(current_temperature)+"°C\n"+"\nPressure:\n "+str(current_pressure)+" Pa\n"+"\nHumidity:\n "+str(current_humidiy)+"%\n"+"\nCondition:\n "+str(weather_description)
                                weather_label.config(text=WEATHER, wraplength=300)
                                weather_label.after(600000, weather)
                            
                            except:
                                weather_label.config(text="Please Check your Internet Connection!", wraplength=150)        
                                weather_label.after(1000, weather)

                        weather_label=Label(root_1, background="gray5", foreground="cyan", font=("Avengeance Heroic Avenger Italic", 15))
                        weather_label.place(relheight=0.35, relwidth=0.115, relx=0.873, rely=0.046)
                        weather()
                        TIME()

                        def Alarm():
                            now=datetime.datetime.now()
                            week_num=datetime.date(now.year, now.month, now.day).weekday()
                            cursor.execute("SELECT * FROM alarms")
                            records_2=cursor.fetchall()
                            for i in records_2:
                                t=i[0].split(":")
                                if t[0]==str(datetime.datetime.now().hour) and t[1]==str(datetime.datetime.now().minute) and t[2]==str(datetime.datetime.now().second):
                                    if i[week_num+1]=="Yes":
                                        winsound.PlaySound("Alarm_Ringtone.wav", winsound.SND_FILENAME)
                                        messagebox.showinfo("Alarm", "Alarm")
                            hide_4.after(1000, Alarm)
                        TIME()

                        battery = psutil.sensors_battery()

                        engine = pyttsx3.init()
                        hearme = sr.Recognizer()

                        lang_dict={"Afrikaans":"af", "Irish":"ga", "Albanian":"sq", "Italian":"it", "Arabic":"ar", "Japanese":"ja", "Azerbaijani":"az",
                                "Kannada":"kn", "Basque":"eu", "Korean":"ko", "Bengali":"bn", "Latin":"la", "Belarusian":"be", "Latvian":"lv", "Bulgarian":"bg",
                                "Lithuanian":"lt", "Catalan":"ca", "Macedonian":"mk", "Chinese Simplified":"zh-CN", "Malay":"ms", "Chinese Traditional":"zh-TW",
                                "Maltese":"mt", "Croatian":"hr", "Norwegian":"no", "Czech":"cs", "Persian":"fa", "Danish":"da", "Polish":"pl", "Dutch":"nl",
                                "Portuguese":"pt", "English":"en", "Romanian":"ro", "Esperanto":"eo", "Russian":"ru", "Estonian":"et", "Serbian":"sr", 
                                "Filipino":"tl", "Slovak":"sk", "Finnish":"fi", "Slovenian":"sl", "French":"fr", "Spanish":"es", "Galician":"gl", "Swahili":"sw",
                                "Georgian":"ka", "Swedish":"sv", "German":"de", "Tamil":"ta", "Greek":"el", "Telugu":"te", "Gujarati":"gu", "Thai":"th", 
                                "Haitian Creole":"ht", "Turkish":"tr", "Hebrew":"iw", "Ukrainian":"uk", "Hindi":"hi", "Urdu":"ur", "Hungarian":"hu", "Vietnamese":"vi",
                                "Icelandic":"is", "Welsh":"cy", "Indonesian":"id", "Yiddish":"yi"}

                        def talktome(audio):
                            engine.say(audio)
                            engine.runAndWait()

                        def listentome():

                            if text_task_var.get()!="":
                                task=text_task_var.get()
                                text_task_var.set("")

                                now=datetime.datetime.now()
                                DATE=str(now.day)+"/"+str(now.month)+"/"+str(now.year)
                                TIME=strftime("%H:%M:%S")

                                cursor.execute(f"INSERT INTO chat_history (Date, Time, Chat_User) VALUES ('{DATE}', '{TIME}', '{task}')")
                                db_connection.commit()

                                try:
                                    cursor.execute("SELECT Path FROM applications where Applications='Default Browser'")
                                    browser_path=str(cursor.fetchall()[0][0])

                                except:
                                    t="Sir please give me the path of your Default Browser as it hasn't been fed into my Database"
                                    talktome(t)
                                    file = fd.askopenfile()

                                    if file: 
                                        browser_path=file.name
                                        PATH=f"INSERT INTO Applications VALUES ('Default Browser', '{browser_path}')"
                                        cursor.execute(PATH)
                                        db_connection.commit()
                                        talktome("Thank you sir, I have stored the path of Google Chrome, now you can proceed further.")
                                    
                                    else:
                                        talktome("Sorry sir, I could not find the File.")
                    
                                if "search" in task or "Search" in task:
                                    t="Searching"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()

                                    task=task.split()
                                    a=0
                                    for i in range(len(task)):
                                        if task[i]=="for" or task[i]=="about":
                                            a=i
                                            break
                                    task=" ".join(task[a+1:])
                                    
                                    url="https://google.com/search?q="+task
                                    webbrowser.get(browser_path).open(url)

                                elif "battery status" in task:
                                    t="the charge left is " + str(battery.percent) +" percent"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()

                                elif "timer" in task or "Timer" in task:
                                    t="Opening Timer"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                    
                                    root_2=Tk()
                                    root_2.title("Timer")
                                    root_2.geometry("400x150")
                                    root_2.config(background="Gray5")

                                    hour=IntVar()
                                    minute=IntVar()
                                    second=IntVar()

                                    heading=Label(root_2, text="TIMER", bg="Gray5", fg="Cyan", font=("Avengero Regular", 20))
                                    heading.place(x=150, y=0)

                                    line=Label(root_2, text="_"*100, font=("Arial", 6), bg="Gray5", fg="Cyan")
                                    line.place(x=0, y=33)

                                    hour_label=Label(root_2, text="Hours", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10))
                                    hour_label.place(x=10, y=60)

                                    hourEntry= Entry(root_2, width=3, textvariable=hour, bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), insertbackground="Cyan")
                                    hourEntry.place(x=73,y=61)

                                    minute_label=Label(root_2, text="Minutes", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10))
                                    minute_label.place(x=125, y=60)

                                    minuteEntry= Entry(root_2, width=3, textvariable=minute, bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), insertbackground="Cyan")
                                    minuteEntry.place(x=205,y=61)

                                    second_label=Label(root_2, text="Seconds", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10))
                                    second_label.place(x=260, y=60)

                                    secondEntry= Entry(root_2, width=3,textvariable=second, bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), insertbackground="Cyan")
                                    secondEntry.place(x=345,y=61)

                                    class Functions():
                                        global running
                                        global flag
                                        global flag_2
                                        running=False
                                        flag=0

                                        def Start_Main():
                                            global flag
                                            flag=0
                                            start.config(state="disabled")
                                            reset.config(state="normal")
                                            stop.config(state="normal")
                                            close.config(state="normal")

                                            def Start():
                                                global running
                                                global flag
                                                
                                                if flag==0:
                                                    running=True
                                                    flag=1

                                                if running==True:
                                                    time_label=Label(root_2, text="", bg="Gray5")
                                                    time_label.place(x=10, y=150)

                                                    for i in range(1):
                                                        if second.get()==0 and minute.get()==0 and hour.get()==0:
                                                            running=False
                                                            talktome("Time's up!")
                                                            messagebox.showinfo("Time Countdown", "Time's up ")
                                                        if minute.get()==0 and hour.get()>=1:
                                                            minute.set(60)
                                                            hour.set(hour.get()-1)
                                                        if second.get()==0 and minute.get()>=1:
                                                            second.set(60)
                                                            minute.set(minute.get()-1)
                                                        second.set(second.get()-1)
                                                        time_label.after(1000, Start)
                                            Start()
                                            
                                        def Stop():
                                            global running
                                            running=False

                                            start.config(state="normal")
                                            reset.config(state="normal")
                                            stop.config(state="disabled")
                                            close.config(state="normal")
                                            
                                        def Reset():
                                            global running

                                            running=False
                                            hour.set(00)
                                            minute.set(00)
                                            second.set(00)

                                            start.config(state="normal")
                                            reset.config(state="disabled")
                                            stop.config(state="disabled")
                                            close.config(state="normal")

                                        def Close():
                                            root_2.destroy()

                                    start=Button(root_2, text="Start", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), command=Functions.Start_Main)
                                    stop=Button(root_2, text="Stop", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), command=Functions.Stop, state="disabled")
                                    reset=Button(root_2, text="Reset", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), command=Functions.Reset, state="disabled")
                                    close=Button(root_2, text="Close", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), command=Functions.Close)

                                    start.place(x=77, y=100)
                                    stop.place(x=140, y=100)
                                    reset.place(x=192, y=100)
                                    close.place(x=253, y=100)

                                    root_2.resizable(False, False)
                                    root_2.mainloop()
                                        
                                elif "time" in task:
                                    Time = strftime("%H:%M:%S")
                                    t="the time is "+Time
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                        
                                elif "date" in task:
                                    Year = int(datetime.datetime.now().year)
                                    Month = int(datetime.datetime.now().month)
                                    Date = int(datetime.datetime.now().day)
                                    t="the date is "+Date+" "+Month+" "+Year
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                        
                                elif "shutdown" in task or "Shutdown" in task:
                                    t="Shutting Down"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                        
                                    os.system('shutdown -s -t 0')
                                                
                                elif "restart" in task or "Restart" in task:
                                    t="Restarting"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                        
                                    os.system('shutdown -r -t 0')
                                                
                                elif "log off" in task:
                                    t="Logging Off"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                        
                                    os.system('shutdown /l')
                                                
                                elif "exit" in task or "Bye" in task or "bye" in task:
                                    t="Bye bye, have a good day"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()

                                    root_1.destroy()
                                                
                                elif "who are you" in task or "your name" in task or "tell me something about you" in task:
                                    l=["I am Epic, your assistant", 
                                    "I am Epic, Extraodinarily Powerful and Intelligent Computer, in short, your assistant",
                                    "I am your assistant and you can call me Epic"]

                                    n=random.randint(0,2)
                                    t=l[n]
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                                    
                                elif "how are you" in task or "how do you do" in task:
                                    l=["I am fine, Thank you",
                                    "I am happy to serve you",
                                    "Excellent, Hope the same for you!"]
                                                    
                                    n=random.randint(0,2)
                                    t=l[n]
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                                    
                                elif "who am I" in task or "my name" in task:
                                    l=[owner+", am I right?",
                                    "You are "+owner,
                                    "My records say that you are "+owner,
                                    "Are you testing me? Well, I know you are "+owner]

                                    n=random.randint(0,3)
                                    t=l[n]
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                                    
                                elif "throw a dice" in task or "roll a dice" in task:
                                    l=[1,2,3,4,5,6]

                                    n=random.randint(0,5)
                                    t="It's "+str(l[n])
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                                    
                                elif "toss a coin" in task or "Toss a Coin" in task:
                                    l=["Heads", "Tails"]

                                    n=random.randint(0,1)
                                    t=l[n]+" it is"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                                    
                                elif "who do you work for" in task or "who is your boss" in task or "you are the assistant of" in task:
                                    l=["I work for "+owner,
                                    "I am the assistant of "+owner]

                                    n=random.randint(0,1)
                                    t=l[n]
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                                    
                                elif "what can you do" in task or "what are you capable of" in task or "what are your capabilities" in task:
                                    t="I can open applications, search for weather, search the net, tell the date and time, open stopwatch and timer, set alarms, tell jokes and tongue twisters, recite poems, give you our chat history and also, I can toss a coin and throw a dice."
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                    
                                elif "click" in task or "Click" in task or "Photo" in task or "photo" in task or "Photograph" in task or "photograph" in task or "Camera" in task or "camera" in task:
                                    t="Opening Camera"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()

                                    sp.run('start microsoft.windows.camera:', shell=True)
                                
                                elif "phone" in task or "Phone" in task or "mobile" in task or "Mobile" in task or "Screen" in task or "screen" in task:
                                    os.chdir("scrcpy-win64-v1.17")
                                    output = sp.getoutput('adb devices')
                                    output=output.split("\n")

                                    if len(output)==3:
                                        t="Mobile found, showing screen"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                        os.system("scrcpy")
                                    elif len(output)>3:
                                        t="More than one device is connected, please connect only one device"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                    else:
                                        t="No Devices Found, please connect a device"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                    
                                    root_1.update_idletasks()
                                
                                elif "chat history" in task or "Chat history" in task or "Chat History" in task or "chat History" in task:
                                    t="Fetching Chat History"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()

                                    cursor.execute("select * from chat_history")
                                    records_chat=cursor.fetchall()

                                    root_history=Tk()
                                    root_history.title("EPIC Chat History")
                                    root_history.geometry("750x750")
                                    root_history.config(background="Gray5")

                                    scrollbar = Scrollbar(root_history)
                                    scrollbar.pack( side = RIGHT, fill = Y)

                                    history_label=Text(root_history, bg="Gray5", fg="Cyan", font=("Arial", 17), yscrollcommand=scrollbar.set, wrap=WORD, bd=0)

                                    if len(records_chat)!=0:
                                        for j in range(len(records_chat)):
                                            DaTe="Date: "+str(records_chat[j][0])
                                            TiMe="Time: "+str(records_chat[j][1])
                                            user="User: "+str(records_chat[j][2])
                                            epic="EPIC: "+str(records_chat[j][3])
                                            chat=DaTe+", "+TiMe+"\n"+user+"\n"+epic+"\n\n"
                                            history_label.insert(END, chat)
                                    else:
                                        history_label.insert(END, "No Chat History Found")

                                    history_label.configure(state="disabled")
                                    history_label.place(relheight=1.0, relwidth=0.95, relx=0.03, rely=0.0)
                                    scrollbar.config(command=history_label.yview)

                                    root_1.update_idletasks()

                                    root_history.mainloop()
                                
                                elif "Poem" in task or "poem" in task or "Poems" in task or "poems" in task:
                                    t="Finding Poem"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()

                                    root_poems=Tk()
                                    root_poems.title("EPIC Poems")
                                    root_poems.geometry("750x750")
                                    root_poems.config(background="Gray5")

                                    scrollbar = Scrollbar(root_poems)
                                    scrollbar.pack( side = RIGHT, fill = Y)

                                    poem_label=Text(root_poems, bg="Gray5", fg="Cyan", font=("Arial", 17), yscrollcommand=scrollbar.set, wrap=WORD, bd=0)
                                    
                                    try:
                                        poem=random_poem.get_poem()
                                    except:
                                        poem="No Poem Found!"

                                    poem_label.insert(END, poem)
                                    poem_label.configure(state="disabled")
                                    poem_label.place(relheight=1.0, relwidth=0.95, relx=0.03, rely=0.0)

                                    scrollbar.config(command=poem_label.yview)

                                    root_poems.mainloop()

                                    talktome(poem)
                                    
                                elif "alarm" in task or "Alarm" in task:
                                    t="Opening Alarm Centre"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()

                                    root_3=Tk()
                                    root_3.title("Alarms")
                                    root_3.geometry("500x500")
                                    root_3.config(background="Gray5")

                                    hour_var=IntVar()
                                    minute_var=IntVar()
                                    second_var=IntVar()
                                    mon_var=IntVar()
                                    tues_var=IntVar()
                                    wed_var=IntVar()
                                    thurs_var=IntVar()
                                    fri_var=IntVar()
                                    sat_var=IntVar()
                                    sun_var=IntVar()

                                    hour=ttk.Combobox(root_3, textvariable=hour_var, state="readonly", font=("Avengero Regular", 20), background="Gray5", foreground="Cyan", width=3)
                                    hour["values"]=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
                                    hour.current(0)

                                    minute=ttk.Combobox(root_3, textvariable=minute_var, state="readonly", font=("Avengero Regular", 20), background="Gray5", foreground="Cyan", width=3)
                                    minute["values"]=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60)
                                    minute.current(0)

                                    second=ttk.Combobox(root_3, textvariable=second_var, state="readonly", font=("Avengero Regular", 20), background="Gray5", foreground="Cyan", width=3)
                                    second["values"]=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60)
                                    second.current(0)

                                    mon_check=ttk.Checkbutton(root_3, text="Monday", variable=mon_var)
                                    tues_check=ttk.Checkbutton(root_3, text="Tuesday", variable=tues_var)
                                    wed_check=ttk.Checkbutton(root_3, text="Wednesday", variable=wed_var)
                                    thurs_check=ttk.Checkbutton(root_3, text="Thursday", variable=thurs_var)
                                    fri_check=ttk.Checkbutton(root_3, text="Friday", variable=fri_var)
                                    sat_check=ttk.Checkbutton(root_3, text="Saturday", variable=sat_var)
                                    sun_check=ttk.Checkbutton(root_3, text="Sunday", variable=sun_var)

                                    hour_label=Label(root_3, text="Hour", bg="Gray5", fg="Cyan", font=("Avengeance Heroic Avenger Bold", 25), width=5)
                                    min_label=Label(root_3, text="Minute", bg="Gray5", fg="Cyan", font=("Avengeance Heroic Avenger Bold", 25), width=7)
                                    sec_label=Label(root_3, text="Second", bg="Gray5", fg="Cyan", font=("Avengeance Heroic Avenger Bold", 25), width=7)

                                    hour_label.place(x=30, y=30)
                                    min_label.place(x=188, y=30)
                                    sec_label.place(x=360, y=30)

                                    hour.place(x=35, y=90)
                                    minute.place(x=200, y=90)
                                    second.place(x=372, y=90)

                                    mon_check.place(x=0, y=150)
                                    tues_check.place(x=70, y=150)
                                    wed_check.place(x=140, y=150)
                                    thurs_check.place(x=228, y=150)
                                    fri_check.place(x=303, y=150)
                                    sat_check.place(x=363, y=150)
                                    sun_check.place(x=436, y=150)

                                    def add():
                                        TIME=f"{str(hour_var.get())}:{str(minute_var.get())}:{str(second_var.get())}"
                                        cursor.execute(f"INSERT INTO alarms (Time) VALUES ('{TIME}');")
                                        db_connection.commit()

                                        if mon_var.get()==0:
                                            cursor.execute(f"update alarms set Monday='No' where Time='{TIME}';")
                                            db_connection.commit()
                                        if mon_var.get()!=0:
                                            cursor.execute(f"update alarms set Monday='Yes' where Time='{TIME}';")
                                            db_connection.commit()

                                        if tues_var.get()==0:
                                            cursor.execute(f"update alarms set Tuesday='No' where Time='{TIME}';")
                                            db_connection.commit()
                                        if tues_var.get()!=0:
                                            cursor.execute(f"update alarms set Tuesday='Yes' where Time='{TIME}';")
                                            db_connection.commit()
                                                
                                        if wed_var.get()==0:
                                            cursor.execute(f"update alarms set Wednesday='No' where Time='{TIME}';")
                                            db_connection.commit()
                                        if wed_var.get()!=0:
                                            cursor.execute(f"update alarms set Wednesday='Yes' where Time='{TIME}';")
                                            db_connection.commit()
                                                
                                        if thurs_var.get()==0:
                                            cursor.execute(f"update alarms set Thursday='No' where Time='{TIME}';")
                                            db_connection.commit()
                                        if thurs_var.get()!=0:
                                            cursor.execute(f"update alarms set Thursday='Yes' where Time='{TIME}';")
                                            db_connection.commit()
                                                
                                        if fri_var.get()==0:
                                            cursor.execute(f"update alarms set Friday='No' where Time='{TIME}';")
                                            db_connection.commit()
                                        if fri_var.get()!=0:
                                            cursor.execute(f"update alarms set Friday='Yes' where Time='{TIME}';")
                                            db_connection.commit()
                                                
                                        if sat_var.get()==0:
                                            cursor.execute(f"update alarms set Saturday='No' where Time='{TIME}';")
                                            db_connection.commit()
                                        if sat_var.get()!=0:
                                            cursor.execute(f"update alarms set Saturday='Yes' where Time='{TIME}';")
                                            db_connection.commit()
                                                
                                        if sun_var.get()==0:
                                            cursor.execute(f"update alarms set Sunday='No' where Time='{TIME}';")
                                            db_connection.commit()
                                        if sun_var.get()!=0:
                                            cursor.execute(f"update alarms set Sunday='Yes' where Time='{TIME}';")
                                            db_connection.commit()

                                        done_label.config(text="Added")

                                    def delete():
                                        TIME=f"{str(hour_var.get())}:{str(minute_var.get())}:{str(second_var.get())}"
                                        cursor.execute(f"DELETE FROM alarms WHERE Time={TIME};")
                                        db_connection.commit()

                                        done_label.config(text="Deleted")
                                        
                                    def Close():
                                        root_3.destroy()

                                    done_button=Button(root_3, text="ADD", font=("Avengero Regular", 10), fg="Cyan", bg="Gray5", command=add)
                                    delete_button=Button(root_3, text="DELETE", font=("Avengero Regular", 10), fg="Cyan", bg="Gray5", command=delete)
                                    close_button=Button(root_3, text="CLOSE", font=("Avengero Regular", 10), fg="Cyan", bg="Gray5", command=Close)

                                    done_label=Label(root_3, bg="Gray5", fg="Cyan", font=("Avengero Regular", 10))

                                    done_button.place(x=155, y=200)
                                    delete_button.place(x=205, y=200)
                                    close_button.place(x=275, y=200)

                                    done_label.place(x=200, y=240)

                                    root_3.resizable(False, False)
                                    
                                    root_1.update_idletasks()
                                    
                                    root_3.mainloop()
                                                
                                elif "stopwatch" in task or "Stopwatch" in task:
                                    t="Opening Stopwatch"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()

                                    root=Tk()
                                    root.title("Stopwatch")
                                    root.geometry("300x200")
                                    root.config(background="Gray5")

                                    heading=Label(root, text="STOPWATCH", bg="Gray5", fg="Cyan", font=("Avengero Regular", 28))
                                    hour_label=Label(root, text="00", bg="Gray5", fg="Cyan", font=("Avengero Regular", 30))
                                    min_label=Label(root, text="00", bg="Gray5", fg="Cyan", font=("Avengero Regular", 30))
                                    sec_label=Label(root, text="00", bg="Gray5", fg="Cyan", font=("Avengero Regular", 30))
                                    col_label=Label(root, text=":", bg="Gray5", fg="Cyan", font=("Avengeance Heroic Avenger Italic", 30))
                                    col_label_1=Label(root, text=":", bg="Gray5", fg="Cyan", font=("Avengeance Heroic Avenger Italic", 30))

                                    heading.place(x=5, y=10)
                                    hour_label.place(x=20, y=80)
                                    min_label.place(x=110, y=80)
                                    sec_label.place(x=200, y=80)
                                    col_label.place(x=90, y=80)
                                    col_label_1.place(x=180, y=80)

                                    class Functions():

                                        global hour
                                        global minute
                                        global second
                                        global running
                                        global flag
                                        global flag_1
                                        hour=0
                                        minute=0
                                        second=0
                                        running=False
                                        flag=0

                                        def Start_Main():
                                            global flag
                                            flag=0
                                            start.config(state="disabled")
                                            reset.config(state="normal")
                                            stop.config(state="normal")
                                            close.config(state="normal")
                                            def Start():
                                                global hour
                                                global minute
                                                global second
                                                global running
                                                global flag
                                                    
                                                if flag==0:
                                                    running=True
                                                    flag=1

                                                if running==True:
                                                    if hour<10:
                                                        hour_label.config(text="0"+str(hour))
                                                    if minute<10:
                                                        min_label.config(text="0"+str(minute))
                                                    if second<10:
                                                        sec_label.config(text="0"+str(second))
                                                    if hour>=10:
                                                        hour_label.config(text=str(hour))
                                                    if minute>=10:
                                                        min_label.config(text=str(minute))
                                                    if second>=10:
                                                        sec_label.config(text=str(second))

                                                    second+=1
                                                        
                                                    if second>=60:
                                                        minute+=1
                                                        second=0
                                                    if minute>=60:
                                                        hour+=1
                                                        minute=0
                                                        
                                                    sec_label.after(1000, Start)
                                            Start()
                                            
                                        def Stop():
                                            global running
                                            running=False
                                            start.config(state="normal")
                                            reset.config(state="normal")
                                            stop.config(state="disabled")
                                            close.config(state="normal")

                                            
                                        def Reset():
                                            global hour
                                            global minute
                                            global second
                                            global running

                                            running=False
                                            hour=0
                                            minute=0
                                            second=0
                                            hour_label.config(text="00")
                                            min_label.config(text="00")
                                            sec_label.config(text="00")
                                            start.config(state="normal")
                                            reset.config(state="disabled")
                                            stop.config(state="disabled")
                                            close.config(state="normal")

                                        def Close():
                                            root.destroy()

                                    start=Button(root, text="Start", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), command=Functions.Start_Main)
                                    stop=Button(root, text="Stop", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), command=Functions.Stop, state="disabled")
                                    reset=Button(root, text="Reset", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), command=Functions.Reset, state="disabled")
                                    close=Button(root, text="Close", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), command=Functions.Close)

                                    start.place(x=30, y=150)
                                    stop.place(x=93, y=150)
                                    reset.place(x=147, y=150)
                                    close.place(x=208, y=150)

                                    root.resizable(False, False)
                                    
                                    root_1.update_idletasks()
                                    
                                    root.mainloop()
                                                                                    
                                elif "translate" in task or "Translate" in task:
                                    t="Translating"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()

                                    task=task.split()
                                    from_lang=""
                                    to_lang=""
                                    from_lang_1=""
                                    to_lang_1=""
                                    a=0
                                    b=0
                                    d=0
                                    for i in range(len(task)):
                                        if task[i]=="translate" or task[i]=="Translate":
                                            a=i
                                            break

                                    for j in range(len(task)):
                                        if task[j]=="from" or task[j]=="From":
                                            b=j
                                            break
                                                        
                                    for k in range(len(task)):
                                        if task[k]=="to" or task[k]=="To":
                                            d=k
                                            break

                                    from_lang="".join(task[b+1:d])

                                    to_lang="".join(task[d+1:])
                                                        
                                    task="".join(task[a+1:b])

                                    for l in lang_dict:
                                        if l==from_lang.title():
                                            from_lang_1=lang_dict[l]
                                        if l==to_lang.title():
                                            to_lang_1=lang_dict[l]

                                    url="https://translate.google.co.in/?sl="+from_lang_1+"&tl="+to_lang_1+"&text="+task+"&op=translate"
                                    webbrowser.get(browser_path).open(url)

                                elif "Google Drive" in task or "drive" in task:
                                    t="Opening Google Drive in Chrome"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()

                                    url = "https://drive.google.com/drive/my-drive"
                                    webbrowser.get(browser_path).open(url)
                                                
                                elif "Google" in task:
                                    t="Opening Google.com in Chrome"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                    url = "google.com"
                                    webbrowser.get(browser_path).open(url)
                                                
                                elif "YouTube" in task:
                                    t="Opening Youtube"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                    url = "https://www.youtube.com/"
                                    webbrowser.get(browser_path).open(url)
                                                
                                elif "mail" in task or "Gmail" in task:
                                    t="Opening Gmail"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                    url = "https://mail.google.com/mail/?tab=rm&ogbl"
                                    webbrowser.get(browser_path).open(url)
                                
                                elif "website" in task or "Website" in task:
                                    x=0
                                    task_web=task.split()
                                    for i in range(len(task_web)):
                                        if task_web[i]=="website" or task_web[i]=="Website":
                                            x=i
                                            break
                                    url=" ".join(task_web[x+1:])
                                    try:
                                        t="Opening Website"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                        webbrowser.get(browser_path).open(url)
                                    except:
                                        t="Searching Website"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                        base_url="https://google.com/search?q="
                                        final_url=base_url+url
                                        webbrowser.get(browser_path).open(final_url)
                                    
                                elif "Jokes" in task or "jokes" in task or "Joke" in task or "joke" in task:
                                    t="Finding Jokes"
                                    talktome(pyjokes.get_joke(language="en", category="all"))
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                
                                elif "play" in task or "Play" in task or "music" in task or "Music" in task or "song" in task or "Song" in task:
                                    t="Searching for Song in YouTube Music"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()

                                    url="https://music.youtube.com/search?q="
                                    if "Music" in task or "music" in task:
                                        task=task.split()
                                        for i in range(len(task)):
                                            if task[i]=="music" or task[i]=="Music":
                                                task=" ".join(task[i+1:])
                                        url=url+task
                                    
                                    elif "Song" in task or "song" in task:
                                        task=task.split()
                                        for i in range(len(task)):
                                            if task[i]=="song" or task[i]=="Song":
                                                task=" ".join(task[i+1:])
                                        url=url+task

                                    else:
                                        task=task.split()
                                        for i in range(len(task)):
                                            if task[i]=="play" or task[i]=="Play":
                                                task=" ".join(task[i+1:])
                                        url=url+task
                                    webbrowser.get(browser_path).open(url)
                                    
                                elif "Open" in task or "open" in task:
                                    x=0
                                    task=task.split()
                                    for i in range(len(task)):
                                        if task[i]=="open":
                                            x=i
                                    task=" ".join(task[x+1:])
                                    task=task.title()

                                    cursor.execute("SELECT * FROM Applications")
                                    records_1=cursor.fetchall()
                                    for i in records_1:
                                        if task.title() in i[0]:
                                            try:
                                                t="Opening "+task
                                                talktome(t)
                                                cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                                db_connection.commit()
                                                sp.Popen(i[1])
                                                break
                                            except:
                                                t="Sir I am not able to find the file in the given path, has this application been uninstalled?"
                                                talktome(t)
                                                cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                                db_connection.commit()
                                                with sr.Microphone() as source:
                                                    hearme.pause_threshold = 1
                                                    voice_2 = hearme.listen(source)
                                                    task_2 = hearme.recognize_google(voice_2, language='en-in')
                                                    if task_2.title()=="Yes":
                                                        cursor.execute(f"DELETE FROM Applications WHERE Path={i[1]}")
                                                        db_connection.commit()
                                                    else:
                                                        t="Ok sir, please tell me the path again so that I can match it with the path in my database."
                                                        talktome(t)
                                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                                        db_connection.commit()
                                                        file = fd.askopenfile()
                                                        if file: 
                                                            p=file.name
                                                            PATH=f"UPDATE Applications SET Path={p} WHERE Applications={task});"
                                                            cursor.execute(PATH)
                                                            db_connection.commit()
                                                            t="opening"+task
                                                            talktome(t)
                                                            cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                                            db_connection.commit()
                                                            sp.Popen(p)
                                                        else:
                                                            t="Sorry sir, I could not find the File."
                                                            talktome(t)
                                                            cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                                            db_connection.commit()

                                    else:
                                        t="It seems you are opening this application or file for the first time by commanding me, so please provide me with the path of this file."
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                        file = fd.askopenfile()
                                        if file: 
                                            p=file.name
                                            PATH=f"INSERT INTO Applications VALUES ('{task}', '{p}');"
                                            cursor.execute(PATH)
                                            db_connection.commit()
                                            talktome("opening"+task)
                                            sp.Popen(p)
                                        else:
                                            t="Sorry sir, I could not find the File."
                                            talktome(t)
                                            cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                            db_connection.commit()
                                                
                                elif "Current Location" in task or "current location" in task or "where am I" in task or "Where am I" in task:
                                    le=len(loc_list)-1

                                    t="You are currently in "+loc_list[le-3]+", "+loc_list[le-2]
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                        
                                elif "news" in task or "News" in task or "headline" in task or "Headline" in task or "headlines" in task or "Headlines" in task:
                                    if len(News)!=0:
                                        t="News Headlines"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                        n=0
                                        for new in News['articles']:
                                            n+=1
                                            new['title']=new['title'].split(" - ")
                                            talktome(str(new['title'][0]+", source, "+new['title'][1])+str(new['description']))
                                            if n>=7:
                                                break
                                    else:
                                        t="can't access link, please check you internet connection"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                        
                                elif "weather" in task or "Weather" in task or "temperature" in task or "Temperature" in task:
                                    base_url = "http://api.openweathermap.org/data/2.5/weather?appid=f9dfb38f333f20d990fe58bb4135575e&q="
                                    if "of" in task:
                                        task=task.split()
                                        a=0
                                        for i in range(len(task)):
                                            if task[i]=="of":
                                                a=i
                                                break
                                        task=" ".join(task[a+1:])
                                        complete_url = base_url+task

                                    elif "in" in task:
                                        task=task.split()
                                        a=0
                                        for i in range(len(task)):
                                            if task[i]=="in":
                                                a=i
                                                break
                                        task=" ".join(task[a+1:])
                                        complete_url = base_url+task

                                    else:
                                        le=len(loc_list)-4
                                        w=loc_list[le]
                                        w=w.lower()
                                        complete_url=base_url+w
                                    
                                    response = requests.get(complete_url)
                                    x = response.json()

                                    if x["cod"] != "404":
                                        y = x["main"]
                                        current_temperature = y["temp"]
                                        current_pressure = y["pressure"]
                                        current_humidiy = y["humidity"]
                                        z = x["weather"]
                                        weather_description = z[0]["description"]
                                                        
                                        t="The Current Temperature in Kelvin is: "+str(current_temperature)+", The Current pressure in hecto Pascal is: "+str(current_pressure)+", The Current humidity percentage is: "+str(current_humidiy)+", The Current Weather Description is: "+str(weather_description)
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                    else:
                                        t="City not Found"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                            
                                elif "about" in task or "About" in task or "who is" in task or "Who is" in task:
                                    try:
                                        if "about" in task or "About" in task:
                                            task=task.split()
                                            a=0
                                            for i in range(len(task)):
                                                if task[i]=="about" or task[i]=="About":
                                                    a=i
                                                    break
                                            task=" ".join(task[a+1:])
                                        elif "who is" in task or "Who is" in task:
                                            task=task.split()
                                            a=0
                                            for i in range(len(task)):
                                                if task[i]=="is":
                                                    a=i
                                                    break
                                            task=" ".join(task[a+1:])
                                        talktome("I am searching about" + task)
                                        info_label.config(text=wikipedia.summary(task,3))
                                        t=wikipedia.summary(task,3)
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                    except:
                                        t="Showing Results"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()

                                        url="https://google.com/search?q="+task
                                        webbrowser.get(browser_path).open(url)
                                    
                                elif "what" in task or "What" in task or "Calculate" in task or "calculate" in task or "where" in task or "location" in task or "when" in task or "When" in task or "who" in task or "Who" in task or "how" in task or "How" in task:
                                    app_id = 'RU483J-YU4YE46UQ4'
                                    client = wolframalpha.Client(app_id)
                                    try:
                                        res = client.query(task)
                                        answer = next(res.results).text
                                        t=answer
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                        info_label.config(text=answer)
                                    except:
                                        t="Showing Results"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                        url="https://google.com/search?q="+task
                                        webbrowser.get(browser_path).open(url)
                                
                                elif "hai" in task or "hello" in task or "Hello" in task or "Hi" in task or "hi" in task or "Hey" in task or "hey" in task:
                                    hour = datetime.datetime.now().hour
                                    
                                    if hour >= 6 and hour<12:
                                        g="Good Morning Boss"
                                    elif hour >=12 and hour< 18:
                                        g="Good Afternoon Boss"
                                    elif hour >=18 and hour <24:
                                        g="Good Evening Boss"
                                    else:
                                        g="Good Night Boss"

                                    t=g+", this is EPIC, what can I do for you?"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                        
                                else:
                                    t="Sorry sir, currently I am not capable of responding to "+task+", searching results on the net"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()
                                    url="https://google.com/search?q="+task
                                    webbrowser.get(browser_path).open(url)
                            
                            else:
                                with sr.Microphone() as source:
                                    hearme.pause_threshold = 1
                                    voice = hearme.listen(source)

                                    now=datetime.datetime.now()
                                    DATE=str(now.day)+"/"+str(now.month)+"/"+str(now.year)
                                    TIME=strftime("%H:%M:%S")

                                try:
                                    task = hearme.recognize_google(voice, language='en-in')

                                    cursor.execute(f"INSERT INTO chat_history (Date, Time, Chat_User) VALUES ('{DATE}', '{TIME}', '{task}')")
                                    db_connection.commit()

                                    try:
                                        cursor.execute("SELECT Path FROM applications where Applications='Default Browser'")
                                        browser_path=str(cursor.fetchall()[0][0])

                                    except:
                                        t="Sir please give me the path of your Default Browser as it hasn't been fed into my Database"
                                        talktome(t)
                                        file = fd.askopenfile()

                                        if file: 
                                            browser_path=file.name
                                            PATH=f"INSERT INTO Applications VALUES ('Default Browser', '{browser_path}')"
                                            cursor.execute(PATH)
                                            db_connection.commit()
                                            talktome("Thank you sir, I have stored the path of Google Chrome, now you can proceed further.")
                                        
                                        else:
                                            talktome("Sorry sir, I could not find the File.")
                        
                                    if "search" in task or "Search" in task:
                                        t="Searching"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()

                                        task=task.split()
                                        a=0
                                        for i in range(len(task)):
                                            if task[i]=="for" or task[i]=="about":
                                                a=i
                                                break
                                        task=" ".join(task[a+1:])
                                        
                                        url="https://google.com/search?q="+task
                                        webbrowser.get(browser_path).open(url)

                                    elif "battery status" in task:
                                        t="the charge left is " + str(battery.percent) +" percent"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()

                                    elif "timer" in task or "Timer" in task:
                                        t="Opening Timer"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                        
                                        root_2=Tk()
                                        root_2.title("Timer")
                                        root_2.geometry("400x150")
                                        root_2.config(background="Gray5")

                                        hour=IntVar()
                                        minute=IntVar()
                                        second=IntVar()

                                        heading=Label(root_2, text="TIMER", bg="Gray5", fg="Cyan", font=("Avengero Regular", 20))
                                        heading.place(x=150, y=0)

                                        line=Label(root_2, text="_"*100, font=("Arial", 6), bg="Gray5", fg="Cyan")
                                        line.place(x=0, y=33)

                                        hour_label=Label(root_2, text="Hours", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10))
                                        hour_label.place(x=10, y=60)

                                        hourEntry= Entry(root_2, width=3, textvariable=hour, bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), insertbackground="Cyan")
                                        hourEntry.place(x=73,y=61)

                                        minute_label=Label(root_2, text="Minutes", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10))
                                        minute_label.place(x=125, y=60)

                                        minuteEntry= Entry(root_2, width=3, textvariable=minute, bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), insertbackground="Cyan")
                                        minuteEntry.place(x=205,y=61)

                                        second_label=Label(root_2, text="Seconds", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10))
                                        second_label.place(x=260, y=60)

                                        secondEntry= Entry(root_2, width=3,textvariable=second, bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), insertbackground="Cyan")
                                        secondEntry.place(x=345,y=61)

                                        class Functions():
                                            global running
                                            global flag
                                            global flag_2
                                            running=False
                                            flag=0

                                            def Start_Main():
                                                global flag
                                                flag=0
                                                start.config(state="disabled")
                                                reset.config(state="normal")
                                                stop.config(state="normal")
                                                close.config(state="normal")

                                                def Start():
                                                    global running
                                                    global flag
                                                    
                                                    if flag==0:
                                                        running=True
                                                        flag=1

                                                    if running==True:
                                                        time_label=Label(root_2, text="", bg="Gray5")
                                                        time_label.place(x=10, y=150)

                                                        for i in range(1):
                                                            if second.get()==0 and minute.get()==0 and hour.get()==0:
                                                                running=False
                                                                talktome("Time's up!")
                                                                messagebox.showinfo("Time Countdown", "Time's up ")
                                                            if minute.get()==0 and hour.get()>=1:
                                                                minute.set(60)
                                                                hour.set(hour.get()-1)
                                                            if second.get()==0 and minute.get()>=1:
                                                                second.set(60)
                                                                minute.set(minute.get()-1)
                                                            second.set(second.get()-1)
                                                            time_label.after(1000, Start)
                                                Start()
                                                
                                            def Stop():
                                                global running
                                                running=False

                                                start.config(state="normal")
                                                reset.config(state="normal")
                                                stop.config(state="disabled")
                                                close.config(state="normal")
                                                
                                            def Reset():
                                                global running

                                                running=False
                                                hour.set(00)
                                                minute.set(00)
                                                second.set(00)

                                                start.config(state="normal")
                                                reset.config(state="disabled")
                                                stop.config(state="disabled")
                                                close.config(state="normal")

                                            def Close():
                                                root_2.destroy()

                                        start=Button(root_2, text="Start", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), command=Functions.Start_Main)
                                        stop=Button(root_2, text="Stop", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), command=Functions.Stop, state="disabled")
                                        reset=Button(root_2, text="Reset", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), command=Functions.Reset, state="disabled")
                                        close=Button(root_2, text="Close", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), command=Functions.Close)

                                        start.place(x=77, y=100)
                                        stop.place(x=140, y=100)
                                        reset.place(x=192, y=100)
                                        close.place(x=253, y=100)

                                        root_2.resizable(False, False)
                                        root_2.mainloop()
                                            
                                    elif "time" in task:
                                        Time = strftime("%H:%M:%S")
                                        t="the time is "+Time
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                            
                                    elif "date" in task:
                                        Year = int(datetime.datetime.now().year)
                                        Month = int(datetime.datetime.now().month)
                                        Date = int(datetime.datetime.now().day)
                                        t="the date is "+Date+" "+Month+" "+Year
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                            
                                    elif "shutdown" in task or "Shutdown" in task:
                                        t="Shutting Down"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                            
                                        os.system('shutdown -s -t 0')
                                                    
                                    elif "restart" in task or "Restart" in task:
                                        t="Restarting"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                            
                                        os.system('shutdown -r -t 0')
                                                    
                                    elif "log off" in task:
                                        t="Logging Off"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                            
                                        os.system('shutdown /l')
                                                    
                                    elif "exit" in task or "Bye" in task or "bye" in task:
                                        t="Bye bye, have a good day"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()

                                        root_1.destroy()
                                                    
                                    elif "who are you" in task or "your name" in task or "tell me something about you" in task:
                                        l=["I am Epic, your assistant", 
                                        "I am Epic, Extraodinarily Powerful and Intelligent Computer, in short, your assistant",
                                        "I am your assistant and you can call me Epic"]

                                        n=random.randint(0,2)
                                        t=l[n]
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                                        
                                    elif "how are you" in task or "how do you do" in task:
                                        l=["I am fine, Thank you",
                                        "I am happy to serve you",
                                        "Excellent, Hope the same for you!"]
                                                        
                                        n=random.randint(0,2)
                                        t=l[n]
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                                        
                                    elif "who am I" in task or "my name" in task:
                                        l=[owner+", am I right?",
                                        "You are "+owner,
                                        "My records say that you are "+owner,
                                        "Are you testing me? Well, I know you are "+owner]

                                        n=random.randint(0,3)
                                        t=l[n]
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                                        
                                    elif "throw a dice" in task or "roll a dice" in task:
                                        l=[1,2,3,4,5,6]

                                        n=random.randint(0,5)
                                        t="It's "+str(l[n])
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                                        
                                    elif "toss a coin" in task or "Toss a Coin" in task:
                                        l=["Heads", "Tails"]

                                        n=random.randint(0,1)
                                        t=l[n]+" it is"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                                        
                                    elif "who do you work for" in task or "who is your boss" in task or "you are the assistant of" in task:
                                        l=["I work for "+owner,
                                        "I am the assistant of "+owner]

                                        n=random.randint(0,1)
                                        t=l[n]
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                                        
                                    elif "what can you do" in task or "what are you capable of" in task or "what are your capabilities" in task:
                                        t="I can open applications, search for weather, search the net, tell the date and time, open stopwatch and timer, set alarms, tell jokes and tongue twisters, recite poems, give you our chat history and also, I can toss a coin and throw a dice."
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                        
                                    elif "click" in task or "Click" in task or "Photo" in task or "photo" in task or "Photograph" in task or "photograph" in task or "Camera" in task or "camera" in task:
                                        t="Opening Camera"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()

                                        sp.run('start microsoft.windows.camera:', shell=True)
                                    
                                    elif "phone" in task or "Phone" in task or "mobile" in task or "Mobile" in task or "Screen" in task or "screen" in task:
                                        os.chdir("scrcpy-win64-v1.17")
                                        output = sp.getoutput('adb devices')
                                        output=output.split("\n")

                                        if len(output)==3:
                                            t="Mobile found, showing screen"
                                            talktome(t)
                                            cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                            db_connection.commit()
                                            os.system("scrcpy")
                                        elif len(output)>3:
                                            t="More than one device is connected, please connect only one device"
                                            talktome(t)
                                            cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                            db_connection.commit()
                                        else:
                                            t="No Devices Found, please connect a device"
                                            talktome(t)
                                            cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                            db_connection.commit()
                                        
                                        root_1.update_idletasks()
                                    
                                    elif "chat history" in task or "Chat history" in task or "Chat History" in task or "chat History" in task:
                                        t="Fetching Chat History"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()

                                        cursor.execute("select * from chat_history")
                                        records_chat=cursor.fetchall()

                                        root_history=Tk()
                                        root_history.title("EPIC Chat History")
                                        root_history.geometry("750x750")
                                        root_history.config(background="Gray5")

                                        scrollbar = Scrollbar(root_history)
                                        scrollbar.pack( side = RIGHT, fill = Y)

                                        history_label=Text(root_history, bg="Gray5", fg="Cyan", font=("Arial", 17), yscrollcommand=scrollbar.set, wrap=WORD, bd=0)

                                        if len(records_chat)!=0:
                                            for j in range(len(records_chat)):
                                                DaTe="Date: "+str(records_chat[j][0])
                                                TiMe="Time: "+str(records_chat[j][1])
                                                user="User: "+str(records_chat[j][2])
                                                epic="EPIC: "+str(records_chat[j][3])
                                                chat=DaTe+", "+TiMe+"\n"+user+"\n"+epic+"\n\n"
                                                history_label.insert(END, chat)
                                        else:
                                            history_label.insert(END, "No Chat History Found")

                                        history_label.configure(state="disabled")
                                        history_label.place(relheight=1.0, relwidth=0.95, relx=0.03, rely=0.0)
                                        scrollbar.config(command=history_label.yview)

                                        root_1.update_idletasks()

                                        root_history.mainloop()
                                    
                                    elif "Poem" in task or "poem" in task or "Poems" in task or "poems" in task:
                                        t="Finding Poem"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()

                                        root_poems=Tk()
                                        root_poems.title("EPIC Poems")
                                        root_poems.geometry("750x750")
                                        root_poems.config(background="Gray5")

                                        scrollbar = Scrollbar(root_poems)
                                        scrollbar.pack( side = RIGHT, fill = Y)

                                        poem_label=Text(root_poems, bg="Gray5", fg="Cyan", font=("Arial", 17), yscrollcommand=scrollbar.set, wrap=WORD, bd=0)
                                        
                                        try:
                                            poem=random_poem.get_poem()
                                        except:
                                            poem="No Poem Found!"

                                        poem_label.insert(END, poem)
                                        poem_label.configure(state="disabled")
                                        poem_label.place(relheight=1.0, relwidth=0.95, relx=0.03, rely=0.0)

                                        scrollbar.config(command=poem_label.yview)

                                        root_poems.mainloop()

                                        talktome(poem)
                                        
                                    elif "alarm" in task or "Alarm" in task:
                                        t="Opening Alarm Centre"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()

                                        root_3=Tk()
                                        root_3.title("Alarms")
                                        root_3.geometry("500x500")
                                        root_3.config(background="Gray5")

                                        hour_var=IntVar()
                                        minute_var=IntVar()
                                        second_var=IntVar()
                                        mon_var=IntVar()
                                        tues_var=IntVar()
                                        wed_var=IntVar()
                                        thurs_var=IntVar()
                                        fri_var=IntVar()
                                        sat_var=IntVar()
                                        sun_var=IntVar()

                                        hour=ttk.Combobox(root_3, textvariable=hour_var, state="readonly", font=("Avengero Regular", 20), background="Gray5", foreground="Cyan", width=3)
                                        hour["values"]=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
                                        hour.current(0)

                                        minute=ttk.Combobox(root_3, textvariable=minute_var, state="readonly", font=("Avengero Regular", 20), background="Gray5", foreground="Cyan", width=3)
                                        minute["values"]=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60)
                                        minute.current(0)

                                        second=ttk.Combobox(root_3, textvariable=second_var, state="readonly", font=("Avengero Regular", 20), background="Gray5", foreground="Cyan", width=3)
                                        second["values"]=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60)
                                        second.current(0)

                                        mon_check=ttk.Checkbutton(root_3, text="Monday", variable=mon_var)
                                        tues_check=ttk.Checkbutton(root_3, text="Tuesday", variable=tues_var)
                                        wed_check=ttk.Checkbutton(root_3, text="Wednesday", variable=wed_var)
                                        thurs_check=ttk.Checkbutton(root_3, text="Thursday", variable=thurs_var)
                                        fri_check=ttk.Checkbutton(root_3, text="Friday", variable=fri_var)
                                        sat_check=ttk.Checkbutton(root_3, text="Saturday", variable=sat_var)
                                        sun_check=ttk.Checkbutton(root_3, text="Sunday", variable=sun_var)

                                        hour_label=Label(root_3, text="Hour", bg="Gray5", fg="Cyan", font=("Avengeance Heroic Avenger Bold", 25), width=5)
                                        min_label=Label(root_3, text="Minute", bg="Gray5", fg="Cyan", font=("Avengeance Heroic Avenger Bold", 25), width=7)
                                        sec_label=Label(root_3, text="Second", bg="Gray5", fg="Cyan", font=("Avengeance Heroic Avenger Bold", 25), width=7)

                                        hour_label.place(x=30, y=30)
                                        min_label.place(x=188, y=30)
                                        sec_label.place(x=360, y=30)

                                        hour.place(x=35, y=90)
                                        minute.place(x=200, y=90)
                                        second.place(x=372, y=90)

                                        mon_check.place(x=0, y=150)
                                        tues_check.place(x=70, y=150)
                                        wed_check.place(x=140, y=150)
                                        thurs_check.place(x=228, y=150)
                                        fri_check.place(x=303, y=150)
                                        sat_check.place(x=363, y=150)
                                        sun_check.place(x=436, y=150)

                                        def add():
                                            TIME=f"{str(hour_var.get())}:{str(minute_var.get())}:{str(second_var.get())}"
                                            cursor.execute(f"INSERT INTO alarms (Time) VALUES ('{TIME}');")
                                            db_connection.commit()

                                            if mon_var.get()==0:
                                                cursor.execute(f"update alarms set Monday='No' where Time='{TIME}';")
                                                db_connection.commit()
                                            if mon_var.get()!=0:
                                                cursor.execute(f"update alarms set Monday='Yes' where Time='{TIME}';")
                                                db_connection.commit()

                                            if tues_var.get()==0:
                                                cursor.execute(f"update alarms set Tuesday='No' where Time='{TIME}';")
                                                db_connection.commit()
                                            if tues_var.get()!=0:
                                                cursor.execute(f"update alarms set Tuesday='Yes' where Time='{TIME}';")
                                                db_connection.commit()
                                                    
                                            if wed_var.get()==0:
                                                cursor.execute(f"update alarms set Wednesday='No' where Time='{TIME}';")
                                                db_connection.commit()
                                            if wed_var.get()!=0:
                                                cursor.execute(f"update alarms set Wednesday='Yes' where Time='{TIME}';")
                                                db_connection.commit()
                                                    
                                            if thurs_var.get()==0:
                                                cursor.execute(f"update alarms set Thursday='No' where Time='{TIME}';")
                                                db_connection.commit()
                                            if thurs_var.get()!=0:
                                                cursor.execute(f"update alarms set Thursday='Yes' where Time='{TIME}';")
                                                db_connection.commit()
                                                    
                                            if fri_var.get()==0:
                                                cursor.execute(f"update alarms set Friday='No' where Time='{TIME}';")
                                                db_connection.commit()
                                            if fri_var.get()!=0:
                                                cursor.execute(f"update alarms set Friday='Yes' where Time='{TIME}';")
                                                db_connection.commit()
                                                    
                                            if sat_var.get()==0:
                                                cursor.execute(f"update alarms set Saturday='No' where Time='{TIME}';")
                                                db_connection.commit()
                                            if sat_var.get()!=0:
                                                cursor.execute(f"update alarms set Saturday='Yes' where Time='{TIME}';")
                                                db_connection.commit()
                                                    
                                            if sun_var.get()==0:
                                                cursor.execute(f"update alarms set Sunday='No' where Time='{TIME}';")
                                                db_connection.commit()
                                            if sun_var.get()!=0:
                                                cursor.execute(f"update alarms set Sunday='Yes' where Time='{TIME}';")
                                                db_connection.commit()

                                            done_label.config(text="Added")

                                        def delete():
                                            TIME=f"{str(hour_var.get())}:{str(minute_var.get())}:{str(second_var.get())}"
                                            cursor.execute(f"DELETE FROM alarms WHERE Time={TIME};")
                                            db_connection.commit()

                                            done_label.config(text="Deleted")
                                            
                                        def Close():
                                            root_3.destroy()

                                        done_button=Button(root_3, text="ADD", font=("Avengero Regular", 10), fg="Cyan", bg="Gray5", command=add)
                                        delete_button=Button(root_3, text="DELETE", font=("Avengero Regular", 10), fg="Cyan", bg="Gray5", command=delete)
                                        close_button=Button(root_3, text="CLOSE", font=("Avengero Regular", 10), fg="Cyan", bg="Gray5", command=Close)

                                        done_label=Label(root_3, bg="Gray5", fg="Cyan", font=("Avengero Regular", 10))

                                        done_button.place(x=155, y=200)
                                        delete_button.place(x=205, y=200)
                                        close_button.place(x=275, y=200)

                                        done_label.place(x=200, y=240)

                                        root_3.resizable(False, False)
                                        
                                        root_1.update_idletasks()
                                        
                                        root_3.mainloop()
                                                    
                                    elif "stopwatch" in task or "Stopwatch" in task:
                                        t="Opening Stopwatch"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()

                                        root=Tk()
                                        root.title("Stopwatch")
                                        root.geometry("300x200")
                                        root.config(background="Gray5")

                                        heading=Label(root, text="STOPWATCH", bg="Gray5", fg="Cyan", font=("Avengero Regular", 28))
                                        hour_label=Label(root, text="00", bg="Gray5", fg="Cyan", font=("Avengero Regular", 30))
                                        min_label=Label(root, text="00", bg="Gray5", fg="Cyan", font=("Avengero Regular", 30))
                                        sec_label=Label(root, text="00", bg="Gray5", fg="Cyan", font=("Avengero Regular", 30))
                                        col_label=Label(root, text=":", bg="Gray5", fg="Cyan", font=("Avengeance Heroic Avenger Italic", 30))
                                        col_label_1=Label(root, text=":", bg="Gray5", fg="Cyan", font=("Avengeance Heroic Avenger Italic", 30))

                                        heading.place(x=5, y=10)
                                        hour_label.place(x=20, y=80)
                                        min_label.place(x=110, y=80)
                                        sec_label.place(x=200, y=80)
                                        col_label.place(x=90, y=80)
                                        col_label_1.place(x=180, y=80)

                                        class Functions():

                                            global hour
                                            global minute
                                            global second
                                            global running
                                            global flag
                                            global flag_1
                                            hour=0
                                            minute=0
                                            second=0
                                            running=False
                                            flag=0

                                            def Start_Main():
                                                global flag
                                                flag=0
                                                start.config(state="disabled")
                                                reset.config(state="normal")
                                                stop.config(state="normal")
                                                close.config(state="normal")
                                                def Start():
                                                    global hour
                                                    global minute
                                                    global second
                                                    global running
                                                    global flag
                                                        
                                                    if flag==0:
                                                        running=True
                                                        flag=1

                                                    if running==True:
                                                        if hour<10:
                                                            hour_label.config(text="0"+str(hour))
                                                        if minute<10:
                                                            min_label.config(text="0"+str(minute))
                                                        if second<10:
                                                            sec_label.config(text="0"+str(second))
                                                        if hour>=10:
                                                            hour_label.config(text=str(hour))
                                                        if minute>=10:
                                                            min_label.config(text=str(minute))
                                                        if second>=10:
                                                            sec_label.config(text=str(second))

                                                        second+=1
                                                            
                                                        if second>=60:
                                                            minute+=1
                                                            second=0
                                                        if minute>=60:
                                                            hour+=1
                                                            minute=0
                                                            
                                                        sec_label.after(1000, Start)
                                                Start()
                                                
                                            def Stop():
                                                global running
                                                running=False
                                                start.config(state="normal")
                                                reset.config(state="normal")
                                                stop.config(state="disabled")
                                                close.config(state="normal")

                                                
                                            def Reset():
                                                global hour
                                                global minute
                                                global second
                                                global running

                                                running=False
                                                hour=0
                                                minute=0
                                                second=0
                                                hour_label.config(text="00")
                                                min_label.config(text="00")
                                                sec_label.config(text="00")
                                                start.config(state="normal")
                                                reset.config(state="disabled")
                                                stop.config(state="disabled")
                                                close.config(state="normal")

                                            def Close():
                                                root.destroy()

                                        start=Button(root, text="Start", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), command=Functions.Start_Main)
                                        stop=Button(root, text="Stop", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), command=Functions.Stop, state="disabled")
                                        reset=Button(root, text="Reset", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), command=Functions.Reset, state="disabled")
                                        close=Button(root, text="Close", bg="Gray5", fg="Cyan", font=("Avengero Regular", 10), command=Functions.Close)

                                        start.place(x=30, y=150)
                                        stop.place(x=93, y=150)
                                        reset.place(x=147, y=150)
                                        close.place(x=208, y=150)

                                        root.resizable(False, False)
                                        
                                        root_1.update_idletasks()
                                        
                                        root.mainloop()
                                                                                        
                                    elif "translate" in task or "Translate" in task:
                                        t="Translating"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()

                                        task=task.split()
                                        from_lang=""
                                        to_lang=""
                                        from_lang_1=""
                                        to_lang_1=""
                                        a=0
                                        b=0
                                        d=0
                                        for i in range(len(task)):
                                            if task[i]=="translate" or task[i]=="Translate":
                                                a=i
                                                break

                                        for j in range(len(task)):
                                            if task[j]=="from" or task[j]=="From":
                                                b=j
                                                break
                                                            
                                        for k in range(len(task)):
                                            if task[k]=="to" or task[k]=="To":
                                                d=k
                                                break

                                        from_lang="".join(task[b+1:d])

                                        to_lang="".join(task[d+1:])
                                                            
                                        task="".join(task[a+1:b])

                                        for l in lang_dict:
                                            if l==from_lang.title():
                                                from_lang_1=lang_dict[l]
                                            if l==to_lang.title():
                                                to_lang_1=lang_dict[l]

                                        url="https://translate.google.co.in/?sl="+from_lang_1+"&tl="+to_lang_1+"&text="+task+"&op=translate"
                                        webbrowser.get(browser_path).open(url)

                                    elif "Google Drive" in task or "drive" in task:
                                        t="Opening Google Drive in Chrome"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()

                                        url = "https://drive.google.com/drive/my-drive"
                                        webbrowser.get(browser_path).open(url)
                                                    
                                    elif "Google" in task:
                                        t="Opening Google.com in Chrome"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                        url = "google.com"
                                        webbrowser.get(browser_path).open(url)
                                                    
                                    elif "YouTube" in task:
                                        t="Opening Youtube"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                        url = "https://www.youtube.com/"
                                        webbrowser.get(browser_path).open(url)
                                                    
                                    elif "mail" in task or "Gmail" in task:
                                        t="Opening Gmail"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                        url = "https://mail.google.com/mail/?tab=rm&ogbl"
                                        webbrowser.get(browser_path).open(url)
                                    
                                    elif "website" in task or "Website" in task:
                                        x=0
                                        task_web=task.split()
                                        for i in range(len(task_web)):
                                            if task_web[i]=="website" or task_web[i]=="Website":
                                                x=i
                                                break
                                        url=" ".join(task_web[x+1:])
                                        try:
                                            t="Opening Website"
                                            talktome(t)
                                            cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                            db_connection.commit()
                                            webbrowser.get(browser_path).open(url)
                                        except:
                                            t="Searching Website"
                                            talktome(t)
                                            cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                            db_connection.commit()
                                            base_url="https://google.com/search?q="
                                            final_url=base_url+url
                                            webbrowser.get(browser_path).open(final_url)
                                        
                                    elif "Jokes" in task or "jokes" in task or "Joke" in task or "joke" in task:
                                        t=pyjokes.get_joke(language="en", category="all")
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                    
                                    elif "play" in task or "Play" in task or "music" in task or "Music" in task or "song" in task or "Song" in task:
                                        t="Searching for Song in YouTube Music"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()

                                        url="https://music.youtube.com/search?q="
                                        if "Music" in task or "music" in task:
                                            task=task.split()
                                            for i in range(len(task)):
                                                if task[i]=="music" or task[i]=="Music":
                                                    task=" ".join(task[i+1:])
                                            url=url+task
                                        
                                        elif "Song" in task or "song" in task:
                                            task=task.split()
                                            for i in range(len(task)):
                                                if task[i]=="song" or task[i]=="Song":
                                                    task=" ".join(task[i+1:])
                                            url=url+task

                                        else:
                                            task=task.split()
                                            for i in range(len(task)):
                                                if task[i]=="play" or task[i]=="Play":
                                                    task=" ".join(task[i+1:])
                                            url=url+task
                                        webbrowser.get(browser_path).open(url)
                                        
                                    elif "Open" in task or "open" in task:
                                        x=0
                                        task=task.split()
                                        for i in range(len(task)):
                                            if task[i]=="open":
                                                x=i
                                        task=" ".join(task[x+1:])
                                        task=task.title()

                                        cursor.execute("SELECT * FROM Applications")
                                        records_1=cursor.fetchall()
                                        for i in records_1:
                                            if task.title() in i[0]:
                                                try:
                                                    t="Opening "+task
                                                    talktome(t)
                                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                                    db_connection.commit()
                                                    sp.Popen(i[1])
                                                    break
                                                except:
                                                    t="Sir I am not able to find the file in the given path, has this application been uninstalled?"
                                                    talktome(t)
                                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                                    db_connection.commit()
                                                    with sr.Microphone() as source:
                                                        hearme.pause_threshold = 1
                                                        voice_2 = hearme.listen(source)
                                                        task_2 = hearme.recognize_google(voice_2, language='en-in')
                                                        if task_2.title()=="Yes":
                                                            cursor.execute(f"DELETE FROM Applications WHERE Path={i[1]}")
                                                            db_connection.commit()
                                                        else:
                                                            t="Ok sir, please tell me the path again so that I can match it with the path in my database."
                                                            talktome(t)
                                                            cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                                            db_connection.commit()
                                                            file = fd.askopenfile()
                                                            if file: 
                                                                p=file.name
                                                                PATH=f"UPDATE Applications SET Path={p} WHERE Applications={task});"
                                                                cursor.execute(PATH)
                                                                db_connection.commit()
                                                                t="opening"+task
                                                                talktome(t)
                                                                cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                                                db_connection.commit()
                                                                sp.Popen(p)
                                                            else:
                                                                t="Sorry sir, I could not find the File."
                                                                talktome(t)
                                                                cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                                                db_connection.commit()

                                        else:
                                            t="It seems you are opening this application or file for the first time by commanding me, so please provide me with the path of this file."
                                            talktome(t)
                                            cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                            db_connection.commit()
                                            file = fd.askopenfile()
                                            if file: 
                                                p=file.name
                                                PATH=f"INSERT INTO Applications VALUES ('{task}', '{p}');"
                                                cursor.execute(PATH)
                                                db_connection.commit()
                                                talktome("opening"+task)
                                                sp.Popen(p)
                                            else:
                                                t="Sorry sir, I could not find the File."
                                                talktome(t)
                                                cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                                db_connection.commit()
                                                    
                                    elif "Current Location" in task or "current location" in task or "where am I" in task or "Where am I" in task:
                                        le=len(loc_list)-1

                                        t="You are currently in "+loc_list[le-3]+", "+loc_list[le-2]
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                            
                                    elif "news" in task or "News" in task or "headline" in task or "Headline" in task or "headlines" in task or "Headlines" in task:
                                        if len(News)!=0:
                                            t="News Headlines"
                                            talktome(t)
                                            cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                            db_connection.commit()
                                            n=0
                                            for new in News['articles']:
                                                n+=1
                                                new['title']=new['title'].split(" - ")
                                                talktome(str(new['title'][0]+", source, "+new['title'][1])+str(new['description']))
                                                if n>=7:
                                                    break
                                        else:
                                            t="can't access link, please check you internet connection"
                                            talktome(t)
                                            cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                            db_connection.commit()
                                            
                                    elif "weather" in task or "Weather" in task or "temperature" in task or "Temperature" in task:
                                        base_url = "http://api.openweathermap.org/data/2.5/weather?appid=f9dfb38f333f20d990fe58bb4135575e&q="
                                        if "of" in task:
                                            task=task.split()
                                            a=0
                                            for i in range(len(task)):
                                                if task[i]=="of":
                                                    a=i
                                                    break
                                            task=" ".join(task[a+1:])
                                            complete_url = base_url+task

                                        elif "in" in task:
                                            task=task.split()
                                            a=0
                                            for i in range(len(task)):
                                                if task[i]=="in":
                                                    a=i
                                                    break
                                            task=" ".join(task[a+1:])
                                            complete_url = base_url+task

                                        else:
                                            le=len(loc_list)-4
                                            w=loc_list[le]
                                            w=w.lower()
                                            complete_url=base_url+w
                                        
                                        response = requests.get(complete_url)
                                        x = response.json()

                                        if x["cod"] != "404":
                                            y = x["main"]
                                            current_temperature = y["temp"]
                                            current_pressure = y["pressure"]
                                            current_humidiy = y["humidity"]
                                            z = x["weather"]
                                            weather_description = z[0]["description"]
                                                            
                                            t="The Current Temperature in Kelvin is: "+str(current_temperature)+", The Current pressure in hecto Pascal is: "+str(current_pressure)+", The Current humidity percentage is: "+str(current_humidiy)+", The Current Weather Description is: "+str(weather_description)
                                            talktome(t)
                                            cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                            db_connection.commit()
                                        else:
                                            t="City not Found"
                                            talktome(t)
                                            cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                            db_connection.commit()
                                                
                                    elif "about" in task or "About" in task or "who is" in task or "Who is" in task:
                                        try:
                                            if "about" in task or "About" in task:
                                                task=task.split()
                                                a=0
                                                for i in range(len(task)):
                                                    if task[i]=="about" or task[i]=="About":
                                                        a=i
                                                        break
                                                task=" ".join(task[a+1:])
                                            elif "who is" in task or "Who is" in task:
                                                task=task.split()
                                                a=0
                                                for i in range(len(task)):
                                                    if task[i]=="is":
                                                        a=i
                                                        break
                                                task=" ".join(task[a+1:])
                                            talktome("I am searching about" + task)
                                            info_label.config(text=wikipedia.summary(task,3))
                                            t=wikipedia.summary(task,3)
                                            talktome(t)
                                            cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                            db_connection.commit()
                                        except:
                                            t="Showing Results"
                                            talktome(t)
                                            cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                            db_connection.commit()

                                            url="https://google.com/search?q="+task
                                            webbrowser.get(browser_path).open(url)
                                        
                                    elif "what" in task or "What" in task or "Calculate" in task or "calculate" in task or "where" in task or "location" in task or "when" in task or "When" in task or "who" in task or "Who" in task or "how" in task or "How" in task:
                                        app_id = 'RU483J-YU4YE46UQ4'
                                        client = wolframalpha.Client(app_id)
                                        try:
                                            res = client.query(task)
                                            answer = next(res.results).text
                                            t=answer
                                            talktome(t)
                                            cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                            db_connection.commit()
                                            info_label.config(text=answer)
                                        except:
                                            t="Showing Results"
                                            talktome(t)
                                            cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                            db_connection.commit()
                                            url="https://google.com/search?q="+task
                                            webbrowser.get(browser_path).open(url)
                                    
                                    elif "hai" in task or "hello" in task or "Hello" in task or "Hi" in task or "hi" in task or "Hey" in task or "hey" in task:
                                        hour = datetime.datetime.now().hour
                                        
                                        if hour >= 6 and hour<12:
                                            g="Good Morning Boss"
                                        elif hour >=12 and hour< 18:
                                            g="Good Afternoon Boss"
                                        elif hour >=18 and hour <24:
                                            g="Good Evening Boss"
                                        else:
                                            g="Good Night Boss"

                                        t=g+", this is EPIC, what can I do for you?"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                            
                                    else:
                                        t="Sorry sir, currently I am not capable of responding to "+task+", Should I search it on the net?"
                                        talktome(t)
                                        cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                        db_connection.commit()
                                        with sr.Microphone() as source:
                                            hearme.pause_threshold = 1
                                            voice_1 = hearme.listen(source)
                                            task_1 = hearme.recognize_google(voice_1, language='en-in')
                                            if "yes" in task_1 or "Yes" in task_1:
                                                talktome("searching")
                                                url="https://google.com/search?q="+task
                                                webbrowser.get(browser_path).open(url)
                                            else:
                                                talktome("Ok sir")
                                                listentome()
                            
                                except:
                                    t="I couldn't understand that, please repeat"
                                    talktome(t)
                                    cursor.execute(f"UPDATE chat_history SET Chat_EPIC='{t}' WHERE Date='{DATE}' AND Chat_User='{task}' AND Chat_EPIC IS NULL;")
                                    db_connection.commit()

                        text_task=Entry(root_1, textvariable=text_task_var, font=("Avengeance Heroic Avenger Italic", 15), foreground="Cyan", background="Gray7", insertbackground="White")
                        text_task.place(relx=0.85, rely=0.5, relwidth=0.15, relheight=0.04)
                        img=PhotoImage(file="Mic.png")
                        voice_button=Button(root_1, image=img, command=listentome)
                        voice_button.place(relheight=0.059, relwidth=0.035, relx=0.9, rely=0.67)
                        hide_1=Label(root_1, background="gray5", font=("Avengeance Heroic Avenger Italic", 8), foreground="cyan", text="Speak")
                        hide_1.place(relheight=0.025, relwidth=0.037, relx=0.899, rely=0.723)
                        hide_2=Label(root_1, background="gray5")
                        hide_2.place(relheight=0.025, relwidth=0.037, relx=0.8995, rely=0.651)
                        hide_3=Label(root_1, background="gray5")
                        hide_3.place(relheight=0.052, relwidth=0.005, relx=0.898, rely=0.671)
                        hide_4=Label(root_1, background="gray5")
                        hide_4.place(relheight=0.052, relwidth=0.005, relx=0.93, rely=0.671)
                        Alarm()

                        def key_check_internal():
                            if keyboard.is_pressed("enter"):
                                listentome()
                            if keyboard.is_pressed("esc"):
                                root_1.destroy()
                            hide_4.after(100, key_check_internal)
                        
                        key_check_internal()

                        root_1.mainloop()

                    Main_Function()
                
                elif username_var.get()=="" and password_var.get()=="":
                    info.config(text="Please Enter Username and Password")
                    info.place(relx=0.37, rely=0.63)
                
                elif username_var.get()=="" and password_var.get()!="":
                    info.config(text="Please Enter Username")
                    info.place(relx=0.42, rely=0.63)
                
                elif username_var.get()!="" and password_var.get()=="":
                    info.config(text="Please Enter Password")
                    info.place(relx=0.42, rely=0.63)
                
                else:
                    info.config(text="Incorrect Username or Password")
                    info.place(relx=0.39, rely=0.63)
        
        info=Label(root, font=("Avengero Regular", 10), foreground="Red", background="Gray7")
        user_name_entry=Entry(root, textvariable=username_var, font=("Avengeance Heroic Avenger Italic", 20), foreground="Cyan", background="Gray7", insertbackground="White")
        password_entry=Entry(root, textvariable=password_var, font=("Avengeance Heroic Avenger Italic", 20), foreground="Cyan", background="Gray7", insertbackground="White", show="*")
        login_button=Button(root, text="Login", command=Login, font=("Avengero Regular", 18), foreground="Cyan", background="Gray7")

        user_name_entry.place(relheight=0.045, relwidth=0.2, relx=0.465, rely=0.49)
        password_entry.place(relheight=0.045, relwidth=0.2, relx=0.465, rely=0.57)
        login_button.place(relheight=0.045, relwidth=0.08, relx=0.45, rely=0.68)
        info.place(relx=0.37, rely=0.63)

        def key_check():
            if keyboard.is_pressed("enter"):
                Login()
            if keyboard.is_pressed("esc"):
                root.destroy()
            info.after(100, key_check)
        
        key_check()

        root.mainloop()

try:
    file=open("Password.dat", "rb")
    pswd=pickle.load(file)
    db_connection=mysql.connector.connect(host="localhost", user="root", password=pswd)
    Login_Function()
    
except:
    database_root=Tk()
    database_root.title("Database Info")
    database_root.attributes('-fullscreen', True)

    class Example(Frame):
        def __init__(self, master, *pargs):
            Frame.__init__(self, master, *pargs)

            self.image = Image.open("Database_BG.png")
            self.img_copy= self.image.copy()

            self.background_image = ImageTk.PhotoImage(self.image)

            self.background = Label(self, image=self.background_image)
            self.background.pack(fill=BOTH, expand=YES)
            self.background.bind('<Configure>', self._resize_image)

        def _resize_image(self,event):

            new_width = event.width
            new_height = event.height

            self.image = self.img_copy.resize((new_width, new_height))

            self.background_image = ImageTk.PhotoImage(self.image)
            self.background.configure(image =  self.background_image)

    e = Example(database_root)
    e.pack(fill=BOTH, expand=YES)

    password=StringVar()

    database_password=Entry(database_root, width=23, textvariable=password, font=("Avengeance Heroic Avenger Italic", 20), foreground="Cyan", background="Gray7", insertbackground="White", show="*")
    database_password.place(relheight=0.043, relwidth=0.223, relx=0.39, rely=0.519)

    def button_command():
        pswd=password.get()
        file=open("Password.dat", "wb")
        pickle.dump(pswd, file)
        file.close()
        database_root.destroy()
        try:
            global db_connection
            db_connection=mysql.connector.connect(host="localhost", user="root", password=pswd)
            Login_Function()
        except:
            messagebox.showinfo("Error", "Please Install MySQL 5.0 or above.\nUse the following link to download the setup file:\nhttps://dev.mysql.com/downloads/installer/")

    ok_button=Button(database_root, text="OK", font=("Avengero Regular", 18), foreground="Cyan", background="Gray7", command=button_command)
    ok_button.place(relheight=0.045, relwidth=0.06, relx=0.45, rely=0.68)

    database_root.mainloop()

db_connection.close()