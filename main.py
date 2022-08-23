"""
This Assistant can open your files and make things easier for you.
"""
import os                               # To access the files
import webbrowser                       # To use the web-browser
import psutil                           # To find the process and kill it. https://www.youtube.com/watch?v=P4Y8jl0A_LM&ab_channel=HowtoFixYourComputer
import getpass                          # used to hide input
try:
    import pywhatkit as pwt  # To do YouTube search
except:
    print("Warning! not connected to the Internet")

t = 0


def chrome_search(url):
    """
    Use to register and open the tabs in the desired browser.
    """
    try:

       chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

       webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

       webbrowser.get('chrome').open_new_tab(url)

    except:
        return print("No Internet Connection")


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
    print("Press cs to close chrome.exe")


while True:
    print("Hey!!")
    key = str(input("Enter password \t"))
    # key = getpass.getpass("Enter the Password : ")
    key = str(key)
    if key == 'ut':

        while True:
            command = str(input("Command\t"))

            if command == "c":
                t += 1  # if c is pressed for the first time in the prog it will open the key file too

                if t == 1:  # If c is pressed once call the key function too
                    os.startfile("C:\\Users\\Admin\\PycharmProjects\\auto_type_whatsapp_pyauto_key\\key.py")
                    path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                    os.startfile(path)
                else:
                    os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            elif command == "d":
                os.startfile("C:\\Users\\Admin\\Downloads")  # properties target or location

            elif command == "h":  # to get the help
                print(commands_help())

            elif command == "j":  # to open jarvis project video youtube
                chrome_search(
                    "https://www.youtube.com/watch?v=Lp9Ftuq2sVI&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=121"
                    "&ab_channel=CodeWithHarry")

            elif command == "k":  # to open key
                os.startfile("C:\\Users\\Admin\\PycharmProjects\\auto_type_whatsapp_pyauto_key\\key.py")

            elif command == "p":  # to open projects folder
                os.startfile("C:\\Users\\Admin\\PycharmProjects")

            elif command == "q":  # to quit the program
                PROCNAME = "python.exe"
                for proc in psutil.process_iter():  # psutil to kill task
                    if proc.name() == PROCNAME:
                        proc.kill()

            elif command == "r":  # to open replit.com
                chrome_search("replit.com")

            elif command == "u":  # to get the help
                os.startfile("D:\\Uttam")

            elif command == "y":  # to open youtube
                chrome_search("youtube.com")

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

            elif command == "res":   # To open the resume file
                os.startfile(r"D:\Uttam\Resume\Resume.pdf")

            elif command == "nau": # To open a naukri profile
                chrome_search("https://www.naukri.com/software-developer-python-developer-jobs?experience=0")

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

            elif command == "m":  # to open Gmail.com
                chrome_search("https://mail.google.com/mail/u/0/#inbox")

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
                print("Wrong command")

    else:
        break
