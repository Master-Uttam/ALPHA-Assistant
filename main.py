import os  
import webbrowser                                             # To use the web-browser
import tkinter                                                # For GUI software interface kit
import customtkinter                                          
import psutil                                                 # To kill the tasks
from playsound import playsound as ps                         # To play a relaxing sound everytime Alpha start.
try:
    import pywhatkit as pwt                                   # For YouTube search
except:
    print("Warning! not connected to the Internet")
    
ps(r'C:\\Users\Admin\PycharmProjects\rough1\nice.mp3')


def chrome_search(url):                                       # Use to register and open the tabs in the desired browser.

    chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(url)


def commands_help():
    print("Press cam for camera ")
    print("Press ccam to close camera ")
    print("Press y for youtube")
    print("Press c for chrome")
    print("Press q for quit ")
    print("Press r for replit ")
    print("Press d to open downloads")
    print("Press /s xyz to search on google")
    print("Press /y xyz to search on youtube")
    print("Press py to open pycharm")
    print("Press dr to open google drive")
    print("Press photo to open google photos")
    print("Press md for mail drafts")
    print("Press m for mails")
    print("Press b to open bluetooth settings")
    print("Press cs to close chrome.exe")


def init_commands(command):
    
    if '/s' in command:                                                 # To search on google.com
        command = str(command.replace("/s ", ""))
        chrome_search('https://google.com/search?q=' + command)         # used for search

    elif '/y ' in command:                                              # To search on YouTube.com
        command = command.replace("/y ", "")
        try:
            pwt.playonyt(command)
        except:
            print("No Internet")

    elif '/yt' in command:                                               # To search on YouTube.com and play the first video
        command = command.replace("/yt ", "")
        # command = command.replace
        chrome_search("https://www.youtube.com/results?search_query=" + command)
    
    elif command == "b":
        os.startfile(r'ms-settings:bluetooth')

    elif command == "c":
        os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

    elif command == "d":
        os.startfile("C:\\Users\\Admin\\Downloads")                     # properties target or location

    elif command == "h":                                                # to get the help
        commands_help()

    elif command == "m":                                                # to open Gmail.com
        chrome_search("https://mail.google.com/mail/u/0/#inbox")

    elif command == "p":                                                # to open projects folder
        os.startfile("C:\\Users\\Admin\\PycharmProjects")

    elif command == "q":                                                # to quit the program
        quit()

    elif command == "r":                                                # to open replit.com
        chrome_search("replit.com")

    elif command == "u":                                                # To open a specific folder
        os.startfile("D:\\Uttam")

    elif command == "y":                                                # To open YouTube
        chrome_search("youtube.com")     
  
    elif command == "cs":                                               # To close chrome
        PROCNAME = "chrome.exe"
        for proc in psutil.process_iter():  # psutil to kill task
            if proc.name() == PROCNAME:
                proc.kill()
                
    elif command == "cam":                                              # To open the camera
        os.system("start microsoft.windows.camera:")

    elif command == "ccam":                                             # To close the camera
        PROCNAME = "WindowsCamera.exe"
        for proc in psutil.process_iter():  
            if proc.name() == PROCNAME:
                proc.kill()

    elif command == 'py':                                               # To open pycharm
        os.startfile(
            "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community Edition 2022.2.lnk")

    elif command == "dr":                                               # To open Google Drive
        chrome_search("https://drive.google.com/drive/u/0/my-drive")

    elif command == "photo":                                            # To open Google Photos
        chrome_search(
            "https://photos.google.com/?utm_campaign=mainCTA&utm_medium=website&utm_source=marketingsite")

    elif command == "md":                                               # To open Gmail new draft
        chrome_search("https://mail.google.com/mail/u/0/#drafts?compose=new")

    else:
        pass

app = customtkinter.CTk()
app.title("Alpha Assistant")
app.geometry("900x400")

commandvar = tkinter.StringVar()

entry = customtkinter.CTkEntry(master=app,
                               textvariable=commandvar,
                               width=400,
                               height=25,
                               border_width=2,
                               corner_radius=10)

entry.place(relx=0.5, rely=0.5, anchor=tkinter.S)


def button_event(event):
    init_commands(commandvar.get())


app.bind('<Return>', button_event)

button = customtkinter.CTkButton(master=app,
                                 width=140,
                                 height=30,
                                 border_width=0.5,
                                 corner_radius=50,
                                 text="Submit",
                                 command=button_event)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.N)

app.mainloop()
