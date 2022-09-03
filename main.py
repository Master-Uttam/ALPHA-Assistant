import os  # To access the files
import webbrowser  # To use the web-browser
import tkinter
import customtkinter
import psutil
from playsound import playsound
playsound(r'C:\\Users\Admin\PycharmProjects\rough1\nice.mp3')
try:
    import pywhatkit as pwt  # To do YouTube search
except:
    print("Warning! not connected to the Internet")

def chrome_search(url):
    """
    Use to register and open the tabs in the desired browser.
    """

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
    print("Press p to open projects")
    print("Press k for password")
    print("Press j for jarvis project")
    print("Press ref for refresh bot")
    print("Press Tum to play Tum mile on yt")
    print("Press cod for coding")
    print("Press get to get updates mit bot")
    print("Press voc get the list of vocabulary")
    print("Press /s xyz to search on google")
    print("Press /y xyz to search on youtube")
    print("Press py to open pycharm")
    print("Press dr to open google drive")
    print("Press photo to open google photos")
    print("Press md for mail drafts")
    print("Press m for mails")
    print("Press res for res")
    print("Press nau for naukri")
    print("Press b to open bluetooth settings")
    print("Press task to see the To Do List")
    print("Press cs to close chrome.exe")


def init_commands(command):

    if command == "b":
        os.startfile(r'ms-settings:bluetooth')

    elif command == "c":
        os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

    elif command == "d":
        os.startfile("C:\\Users\\Admin\\Downloads")  # properties target or location

    elif command == "h":  # to get the help
        commands_help()

    elif command == "j":  # to open jarvis project video YoutTube
        chrome_search(
            "https://www.youtube.com/watch?v=Lp9Ftuq2sVI&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=121"
            "&ab_channel=CodeWithHarry")

    elif command == "k":  # to open key
        os.startfile("C:\\Users\\Admin\\PycharmProjects\\auto_type_whatsapp_pyauto_key\\key.py")

    elif command == "m":  # to open Gmail.com
        chrome_search("https://mail.google.com/mail/u/0/#inbox")

    elif command == "p":  # to open projects folder
        os.startfile("C:\\Users\\Admin\\PycharmProjects")

    elif command == "q":  # to quit the program
        quit()

    elif command == "r":  # to open replit.com
        chrome_search("replit.com")

    elif command == "u":  # to get the help
        os.startfile("D:\\Uttam")

    elif command == "y":  # to open YouTube
        chrome_search("youtube.com")

    elif command == "bot":  # To open Truth and dare bot
        os.startfile(r"C:\Users\Admin\PycharmProjects\telegrambot_json_username\Truth_Dare_bot.py")

    elif command == "cam":  # to open the camera
        os.system("start microsoft.windows.camera:")

    elif command == "ccam":  # to kill the camera task

        PROCNAME = "WindowsCamera.exe"
        for proc in psutil.process_iter():  # psutil to kill task
            if proc.name() == PROCNAME:
                proc.kill()

    elif command == "cs":  # close chrome
        PROCNAME = "chrome.exe"
        for proc in psutil.process_iter():  # psutil to kill task
            if proc.name() == PROCNAME:
                proc.kill()

    elif command == 'py':  # open pycharm
        os.startfile(
            "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community Edition 2022.2.lnk")

    elif command == "tum":  # open song tum mile slow and reverb
        chrome_search("https://www.youtube.com/watch?v=W8We0tKTmQ0&ab_channel=TextaudioLyrics")

    elif command == "ref":  # open refresh bot on replit.com
        chrome_search("https://replit.com/@HackerUttam/Refreshbot#main.py")

    elif command == "res":  # To open the resume file
        os.startfile(r"D:\Uttam\Resume\Resume.pdf")

    elif command == "nau":  # To open a naukri profile
        chrome_search("https://www.naukri.com/software-developer-python-developer-jobs?experience=0")

    elif command == "task":  # Notion
        chrome_search("https://www.notion.so/e07b78406c304fbebfae3bb29512dd16?v=230c07606c024623b6d063d9c495cc10")

    elif command == "user":  # open username bot on replit.com
        chrome_search("https://replit.com/@HackerUttam/Printusernamejson#data.py")

    elif command == "cod":  # open code file on Google
        chrome_search(
            "https://docs.google.com/spreadsheets/d/1KWv3PbHbevcGElRCmWmtqQdvdx0SfbBd06KDYOe9JhM/edit#gid=0")

    elif command == "get":  # to get the telegram get files
        chrome_search("https://api.telegram.org/bot5525453528:AAE7SUtDLjH1pxHJRlWWHpCHsdkNjM4ehv8/getUpdates")

    elif command == "voc":  # to open the vocabulary on Google Drive
        chrome_search(
            "https://docs.google.com/spreadsheets/d/1WeRiUk-6ifSue4scHxROqM4fxfMjVdcV8dLO5L8gTRY/edit#gid=0")

    elif command == "dr":  # to open Google Drive
        chrome_search("https://drive.google.com/drive/u/0/my-drive")

    elif command == "photo":  # to open Google Photos
        chrome_search(
            "https://photos.google.com/?utm_campaign=mainCTA&utm_medium=website&utm_source=marketingsite")

    elif command == "md":  # to open Gmail new draft
        chrome_search("https://mail.google.com/mail/u/0/#drafts?compose=new")

    elif command == "rese":  # to open Gmail.com
        os.startfile(r"D:\Uttam\Resume\Auto_update\Auto_resume.docx")

    elif '/s' in command:  # to search on google.com
        command = str(command.replace("/s ", ""))
        chrome_search('https://google.com/search?q=' + command)  # used for search

    elif '/y ' in command:  # to search on YouTube.com
        command = command.replace("/y ", "")
        try:
            pwt.playonyt(command)
        except:
            print("No Internet")

    elif '/yt' in command:  # to search on YouTube.com and play the first video
        command = command.replace("/yt ", "")
        # command = command.replace
        chrome_search("https://www.youtube.com/results?search_query=" + command)

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

# command = customtkinter.CTkEntry(app, textvariable = commandvar)
entry.place(relx=0.5, rely=0.5, anchor=tkinter.S)


def button_event(event):
    init_commands(commandvar.get())


app.bind('<Return>', button_event)

# button = customtkinter.CTkButton(master=app, text="Submit", command=button_event)
button = customtkinter.CTkButton(master=app,
                                 width=140,
                                 height=30,
                                 border_width=0.5,
                                 corner_radius=50,
                                 text="Submit",
                                 command=button_event)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.N)

app.mainloop()
