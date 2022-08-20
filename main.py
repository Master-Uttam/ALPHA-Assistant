import os  # To access the files
import webbrowser  # To use the web-browser
import psutil  # To find the process and kill it. https://www.youtube.com/watch?v=P4Y8jl0A_LM&ab_channel=HowtoFixYourComputer
import pywhatkit as pwt  # To do YouTube search
import getpass  # used to hide input

print("Please wait...")
t = 0
'''
This Assistant can open your files and make things easier for you.
'''


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
    print("Press  get to get updates mit bot")
    print("Press to get the list of vocabulary")
    print("Press /s xyz to search on google")
    print("Press /y xyz to search on youtube")
    print("Press py to open pycharm")
    print("Press cs to close chrome.exe")



while True:
    print("Hey!!")
    key = str(input("Enter password \t"))
    #key = getpass.getpass("Enter the Password : ")
    key = str(key)
    if key == 'ut':

        while True:
            command = str(input("Command\t"))

            if command == "c":
                t += 1

                if t == 1:  # If c is pressed once call the key function too
                    os.startfile("C:\\Users\\Admin\\PycharmProjects\\auto_type_whatsapp_pyauto_key\\key.py")
                    path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                    os.startfile(path)
                else:
                    os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            elif command == "d":
                os.startfile("C:\\Users\\Admin\\Downloads")  # properties target or location

            elif command == "j":
                chrome_search(
                    "https://www.youtube.com/watch?v=Lp9Ftuq2sVI&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=121"
                    "&ab_channel=CodeWithHarry")

            elif command == "k":
                os.startfile("C:\\Users\\Admin\\PycharmProjects\\auto_type_whatsapp_pyauto_key\\key.py")

            elif command == "p":
                os.startfile("C:\\Users\\Admin\\PycharmProjects")

            elif command == "q":
                PROCNAME = "python.exe"
                for proc in psutil.process_iter():  # psutil to kill task
                    if proc.name() == PROCNAME:
                        proc.kill()

            elif command == "r":
                chrome_search("replit.com")

            elif command == "y":
                chrome_search("youtube.com")

            elif command == "h":
                print(commands_help())

            elif command == "cam":
                os.system("start microsoft.windows.camera:")

            elif command == "ccam":

                PROCNAME = "WindowsCamera.exe"
                for proc in psutil.process_iter():  # psutil to kill task
                    if proc.name() == PROCNAME:
                        proc.kill()

            elif command == "cs":
                PROCNAME = "chrome.exe"
                for proc in psutil.process_iter():  # psutil to kill task
                    if proc.name() == PROCNAME:
                        proc.kill()

            elif command == 'py':
                os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community Edition 2022.2.lnk")

            elif command == "tum":
                chrome_search("https://www.youtube.com/watch?v=W8We0tKTmQ0&ab_channel=TextaudioLyrics")

            elif command == "ref":
                chrome_search("https://replit.com/@HackerUttam/Refreshbot#main.py")

            elif command == "user":
                chrome_search("https://replit.com/@HackerUttam/Printusernamejson#data.py")

            elif command == "cod":
                chrome_search(
                    "https://docs.google.com/spreadsheets/d/1KWv3PbHbevcGElRCmWmtqQdvdx0SfbBd06KDYOe9JhM/edit#gid=0")

            elif command == "get":
                chrome_search("https://api.telegram.org/bot5525453528:AAE7SUtDLjH1pxHJRlWWHpCHsdkNjM4ehv8/getUpdates")

            elif '/s' in command:
                command = str(command.replace("/s ", ""))
                chrome_search('https://google.com/search?q=' + command)  # used for search

            elif '/y ' in command:
                command = command.replace("/y ", "")
                pwt.playonyt(command)

            elif '/yt' in command:
                command = command.replace("/yt ", "")
                # command = command.replace
                chrome_search("https://www.youtube.com/results?search_query=" + command)

            else:
                print("Wrong command")

    else:
        break
