import os
from pipes import quote
import random
import string
import shutil
import uuid
import ctypes
import psutil
import platform
import winreg
import screen_brightness_control as sbc
import pywifi
from pywifi import const
import time
import re
import sqlite3
from bs4 import BeautifulSoup
import speedtest
import pywhatkit
import wikipedia
import datetime
import struct
import subprocess
from hugchat import hugchat
import time
import webbrowser
import eel
import pyaudio
import pyautogui
import requests

from engine.command import speak
from engine.config import ASSISTANT_NAME
# Playing assiatnt sound function
import pywhatkit as kit
import pvporcupine

from playsound import playsound
from engine.helper import extract_yt_term, remove_words


con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

    
# def openCommand(query):
#     query = query.replace(ASSISTANT_NAME, "")
#     query = query.replace("open", "")
#     query.lower()

#     app_name = query.strip()

#     if app_name != "":

#         try:
#             cursor.execute(
#                 'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
#             results = cursor.fetchall()

#             if len(results) != 0:
#                 speak("Opening "+query)
#                 os.startfile(results[0][0])

#             def len(results) == 0: 
#                 cursor.execute(
#                 'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
#                 results = cursor.fetchall()
                
#                 if len(results) != 0:
#                     speak("Opening "+query)
#                     webbrowser.open(results[0][0])

#                 else:
#                     speak("Opening "+query)
#                     try:
#                         os.system('start '+query)
#                     except:
#                         speak("not found")
#         except:
#             speak("some thing went wrong")

       

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)


# def hotword1():
#     from engine.command import takecommand
#     htword=None
#     try:
       
#         htword = takecommand()

#         while True:

#             if any(keyword in htword for keyword in ["jarvis", "alexa","jarvi","jarv","javis","avis","lexa","vis","jar","jars"]) :
#                 print("hotword detected")

#                 # pressing shorcut key win+j
#                 import pyautogui as autogui
#                 autogui.keyDown("win")
#                 autogui.press("j")
#                 time.sleep(2)
#                 autogui.keyUp("win")
                
#     except:
#         if htword is not None:
#             htword=None

def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=['jarvis','alexa']) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j
                # import pyautogui as autogui
                pyautogui.keyDown("win")
                pyautogui.press("j")
                time.sleep(2)
                pyautogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()






# chat bot 
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat('''Give reply in 2 sentence.
'''+user_input)
    print(response)
    speak(response)
    return response

#-------------------------------------00000000000000000000000----------
def openFile(query):
    query = query.lower()
    query = query.replace("open", "").replace("folder", "").replace("file", "").replace("directory", "").replace("the", "").replace(" ", "")

    print(query)
    try:
        subprocess.run(["explorer", "search:query=" + query], shell=True)
    except Exception as e:
        
        print(f"Error opening search results: {e}")




def createFolder(query):
    query = query.lower()
    query = query.replace("create", "").replace("folder", "").replace("file", "").replace("directory", "").replace("an", "").replace("a", "").replace("the", "").replace(" ", "")
    folder_name = query

    if not folder_name:  # If folder_name is an empty string after processing
        # Generate a random folder name if none is provided
        folder_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    # Modify the path to target the OneDrive Desktop folder
    desktop_path = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
    folder_path = os.path.join(desktop_path, folder_name)

    try:
        os.mkdir(folder_path)
        print(f"Folder '{folder_name}' created successfully at '{folder_path}'.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists at '{folder_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def openCommand3(query):
    query = query.lower()
    query = query.replace("open","").replace("the","").replace("app", "").replace("application","").replace("launch","").replace(" ","")
    
    try:

            # os.startfile('C:\\Path\\To\\Your\\Application.exe')
        if "edge" in query:
            os.startfile("msedge")    # Assuming Microsoft Edge is in the system's PATH
        elif "chrome" in query:
            os.startfile("chrome")    # Assuming Chrome is in the system's PATH
        elif "firefox" in query:
            os.startfile("firefox")   # Assuming Firefox is in the system's PATH
        elif "notepad" in query:
            os.startfile("notepad")   # Assuming Notepad is in the system's PATH
        elif "zoom" in query:
            os.startfile("zoom")      # Assuming Zoom is in the system's PATH
        elif "vlc" in query:
            os.startfile("vlc")       # Assuming VLC is in the system's PATH
        elif "word" in query:
            os.startfile("winword")   # Assuming Microsoft Word is in the system's PATH
        elif "excel" in query:
            os.startfile("excel")
        else:
            print(f"Opening {query}...")
            os.startfile(query)
       
    except FileNotFoundError:
        
        try:
            # If opening with os.startfile() fails, simulate key presses using pyautogui
            print(f"Error: Application '{query}' not found. Trying alternative method...")
            pyautogui.press("super")  # Press the "super" key (usually the Windows key)
            pyautogui.typewrite(query)  # Type the query
            pyautogui.sleep(2)  # Wait for 2 seconds
            pyautogui.press("enter")  # Press the "enter" key to execute the search
        except Exception as e:
            print(f"An error occurred: {e}")
    
# def openCommand3(query):
#     query = query.replace("open","")
#     query = query.replace("the","")
#     query = query.replace(" ","")

#     try:
#         # Open the specified application
#         print(f"Opening {query}...")
#         os.startfile(query)
#     except FileNotFoundError:
        
#         try:
#             # If opening with os.startfile() fails, simulate key presses using pyautogui
#             print(f"Error: Application '{query}' not found. Trying alternative method...")
#             pyautogui.press("super")  # Press the "super" key (usually the Windows key)
#             pyautogui.typewrite(query)  # Type the query
#             pyautogui.sleep(2)  # Wait for 2 seconds
#             pyautogui.press("enter")  # Press the "enter" key to execute the search
#         except Exception as e:
#             print(f"An error occurred: {e}")

def CloseCommand3(query):
    query = query.lower()
    query = query.replace("close","").replace("the","").replace("application","").replace("app","").replace("terminate","").replace(" ","")

    try:
        if "whatsapp" in query:
            os.system("taskkill /f /im whatsapp.exe")
        elif "microsoft edge" in query:
            os.system("taskkill /f /im msedge.exe")
        elif "chrome" in query:
            os.system("taskkill /f /im chrome.exe")
        elif "firefox" in query:
            os.system("taskkill /f /im firefox.exe")
        elif "notepad" in query:
            os.system("taskkill /f /im notepad.exe")
        elif "zoom" in query:
            os.system("taskkill /f /im zoom.exe")
        elif "vlc" in query:
            os.system("taskkill /f /im vlc.exe")
        elif "word" in query:
            os.system("taskkill /f /im winword.exe")
        elif "excel" in query:
            os.system("taskkill /f /im excel.exe")
    except FileNotFoundError:
        try:
            os.system(f"taskkill /f /im {query}")
        except FileNotFoundError:
            try:
                subprocess.call(["taskkill", "/f", "/im", query])
            except Exception as e:
                print(f"An error occurred: {e}")

# def CloseCommand3(query):
#     query = query.replace("close","")
#     query = query.replace("the","")
#     query = query.replace(" ","")
#     query = query.replace("app","")

#     try:
#         os.system(f"taskkill /f /im {query}")
#     except FileNotFoundError:
#         try:
#            subprocess.call(["taskkill", "/f", "/im", query])
#         except Exception as e:
#             print(f"An error occurred: {e}")


def temperature(query):
    search = query
    url = f"https://www.google.com/search?q={search}"
    r  = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div", class_ = "BNeawe").text
    print(f"current{search} is {temp}")
    speak(f"current{search} is {temp}")
    
def weather(query):
    search = query
    url = f"https://www.google.com/search?q={search}"
    # headers = {'User-Agent': 'Mozilla/5.0'}
    r  = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div", class_ = "BNeawe").text
    print(f"current{search} is {temp}")
    speak(f"current{search} is {temp}")

def timenow():
    strTime = datetime.datetime.now().strftime("%H:%M")    
    print(f"Time is {strTime}")
    speak(f"Time is {strTime}")

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(results)
        speak(results)

def internetSpeed():
    wifi  = speedtest.Speedtest()
    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
    download_net = wifi.download()/1048576
    upload_net = round(upload_net, 2)  # Round off to two decimal places
    download_net = round(download_net, 2)
    print("Wifi Upload Speed is", upload_net," MBps")
    speak(f"Wifi Upload speed is {upload_net} MBps")
    print("Wifi download speed is ",download_net," MBps")
    speak(f"Wifi download speed is {download_net} MBps")

def website(query):
    query = query.lower()
    query = query.replace("open","").replace("the","").replace("website", "").replace(".com","").replace("search","").replace(" ","")

    try:
        if "google" in query:
            webbrowser.open("https://www.google.com")
        elif "youtube" in query:
            webbrowser.open("https://www.youtube.com")
        elif "reddit" in query:
            webbrowser.open("https://www.reddit.com")
        elif "twitter" or "x" in query:
            webbrowser.open("https://www.twitter.com")
        elif "facebook" in query:
            webbrowser.open("https://www.facebook.com")
        elif "amazon" in query:
            webbrowser.open("https://www.amazon.com")
        elif "instagram" in query:
            webbrowser.open("https://www.instagram.com")
        elif "linkedin" in query:
            webbrowser.open("https://www.linkedin.com")
        elif "wikipedia" in query:
            webbrowser.open("https://www.wikipedia.org")
            
    except FileNotFoundError:
        domain = query
        try:
            url = 'https://www.' + domain+'.com'
            webbrowser.open(url)
            return True
        except Exception as e:
            print(e)
            return False


# def website(query):
#     query = query.replace("website ", "")
#     query = query.replace("open ", "")
#     query = query.replace(".com", "")
#     query = query.replace("search", "")
#     query = query.replace(" ", "")


#     def website_opener(domain):
#         try:
#             url = 'https://www.' + domain+'.com'
#             webbrowser.open(url)
#             return True
#         except Exception as e:
#             print(e)
#             return False
#     website_opener(query)

def pause():
    pyautogui.press("k")
    speak("video paused")

def play():
    pyautogui.press("k")
    speak("video played")
    
def mute():
    ctypes.windll.user32.keybd_event(0xAD, 0, 0, 0)
    speak("muted")
def volumeup():
    from engine.keyboard import volumeups
    speak("Turning volume up,sir")
    volumeups()

def volumedown():
    from engine.keyboard import volumedowns
    speak("Turning volume down, sir")
    volumedowns()

def news():
    from engine.NewsRead import latestnews
    latestnews()

import os

def clickmyphoto():
    # Open the default camera application
    os.system("start microsoft.windows.camera:")

    # Provide a delay to allow the camera application to open
    time.sleep(2)

    # Optionally, you can add code to capture the photo here using other libraries or tools.
    # For example, you can use the keyboard module to simulate pressing the capture button.




def screenshots():
    # Capture a screenshot
    img = pyautogui.screenshot()
    # Generate a unique file name using the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"screenshot_{timestamp}.png"
    # Construct the full path to the file
    file_path = os.path.join("C:\\Users\\YAZID\\OneDrive\\Desktop\\jarvis-main17\\screenshots", file_name)
    # Save the screenshot with the generated file name
    img.save(file_path)
def screenshots():
    # Capture a screenshot
    img = pyautogui.screenshot()
    # Generate a unique file name using random letters
    file_name = f"screenshot_{uuid.uuid4()}.png"
    # Construct the full path to the file
    file_path = os.path.join("C:\\Users\\YAZID\\OneDrive\\Desktop\\jarvis-main17\\screenshots", file_name)
    # Save the screenshot with the generated file name
    img.save(file_path)

def shutdown():
    os.system("shutdown /s /t 5")
def restart():
    os.system("shutdown /r /t 5")
def sleepmode():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


# -------------------------------0000000000000000000000000000000-----------



def create_file(file_path):
    try:
        with open(file_path, 'w') as f:
            pass
        print(f"File created: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File deleted: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# create_file('test.txt')
# delete_file('test.txt')




def delete_folder(folder_name):
    try:
        # Attempt to delete folder from the desktop
        desktop_folder_path = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop", folder_name)
        shutil.rmtree(desktop_folder_path)
        print(f"Folder deleted from desktop: {desktop_folder_path}")
        
    except FileNotFoundError:
           
        try:
            # Walk through the entire file system to search for the folder
            for root, dirs, files in os.walk("/", topdown=False):
                for name in dirs:
                    if name == folder_name:
                        folder_path = os.path.join(root, name)
                        shutil.rmtree(folder_path)
                        print(f"Folder deleted from system: {folder_path}")
                        return  # Stop searching after the first deletion
            print(f"Folder '{folder_name}' not found in the system.")
        except Exception as e:
            print(f"An error occurred while searching the system: {e}")



def empty_recycle_bin():
    try:
        SHEmptyRecycleBin = ctypes.windll.shell32.SHEmptyRecycleBinW
        if SHEmptyRecycleBin(None, None, 0) == 0:
            print("Recycle Bin emptied successfully.")
        else:
            print("Failed to empty Recycle Bin.")
    except Exception as e:
        print(f"An error occurred: {e}")




def get_system_uptime_hours():
    try:
        uptime_seconds = psutil.boot_time()
        uptime_hours = uptime_seconds / 3600  # Convert seconds to hours
        print(f"System Uptime: {uptime_hours:.2f} hours")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_system_information():
    try:
        system_info = platform.uname()
        print("System Information:")
        print(f"  System: {system_info.system}")
        print(f"  Node Name: {system_info.node}")
        print(f"  Release: {system_info.release}")
        print(f"  Version: {system_info.version}")
        print(f"  Machine: {system_info.machine}")
        print(f"  Processor: {system_info.processor}")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_process_list():
    try:
        process_list = psutil.process_iter()
        print("Process List:")
        for process in process_list:
            print(f"  Process ID: {process.pid} - {process.name()}")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_battery_info():
    try:
        battery_info = psutil.sensors_battery()
        if battery_info is not None:
            print("Battery Information:")
            print(f"  Charge Percentage: {battery_info.percent} %")
            print(f"  Power Plugged In: {battery_info.power_plugged}")
            print(f"  Time Left: {battery_info.secsleft} seconds")
        else:
            print("Battery information not available.")
    except Exception as e:
        print(f"An error occurred: {e}")


def switch_between_windows():
    try:
        pyautogui.hotkey('alt', 'tab')
        time.sleep(1)  

    except Exception as e:
        print(f"An error occurred: {e}")


def minimize_window():
    pyautogui.hotkey('win', 'down')

def maximize_window():
    pyautogui.hotkey('win', 'up')

def close_window():
    pyautogui.hotkey('alt', 'f4')

def refresh():
    pyautogui.press('f5')

def restore_down():
    pyautogui.hotkey('win', 'down')

def move_window_left():
    pyautogui.hotkey('win', 'left')

def move_window_right():
    pyautogui.hotkey('win', 'right')

def switch_to_next_window():
    pyautogui.hotkey('alt', 'tab')

def switch_to_previous_window():
    pyautogui.hotkey('alt', 'shift', 'tab')

def open_task_manager():
    pyautogui.hotkey('ctrl', 'shift', 'esc')

def lock_screen():
    try:
        # Use subprocess to run the rundll32.exe command to lock the workstation
        subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"])
        print("Screen locked successfully.")
    except Exception as e:
        print(f"Error locking screen: {e}")
def switch_virtual_desktop_left():
    pyautogui.hotkey('ctrl', 'win', 'left')

def switch_virtual_desktop_right():
    pyautogui.hotkey('ctrl', 'win', 'right')

def minimize_all_windows():
    try:
        pyautogui.hotkey('win', 'd')
    except Exception as e:
        print(f"An error occurred: {e}")

def show_desktop():
    try:
        pyautogui.hotkey('win', 'm')
    except Exception as e:
        print(f"An error occurred: {e}")

def open_file_explorer():
    try:
        pyautogui.hotkey('win', 'e')
    except Exception as e:
        print(f"An error occurred: {e}")

def toggle_full_screen_mode():
    try:
        pyautogui.press('f11')
    except Exception as e:
        print(f"An error occurred: {e}")

def open_run_dialog():
    try:
        pyautogui.hotkey('win', 'r')
    except Exception as e:
        print(f"An error occurred: {e}")

def open_action_center():
    try:
        pyautogui.hotkey('win', 'a')
    except Exception as e:
        print(f"An error occurred: {e}")

def open_settings():
    try:
        pyautogui.hotkey('win', 'i')
    except Exception as e:
        print(f"An error occurred: {e}")

def open_task_view():
    try:
        pyautogui.hotkey('win', 'tab')
    except Exception as e:
        print(f"An error occurred: {e}")

def open_cortana():
    try:
        pyautogui.hotkey('win', 's')
    except Exception as e:
        print(f"An error occurred: {e}")

def open_notification_center():
    try:
        pyautogui.hotkey('win', 'v')
    except Exception as e:
        print(f"An error occurred: {e}")

def open_clipboard_history():
    try:
        pyautogui.hotkey('win', 'v')  # for Windows 10 version 1809 and later
    except Exception as e:
        print(f"An error occurred: {e}")

def open_snipping_tool():
    try:
        pyautogui.hotkey('win', 'shift', 's')  # for Windows 10 version 1809 and later
    except Exception as e:
        print(f"An error occurred: {e}")

def open_magnifier():
    try:
        pyautogui.hotkey('win', '+')  # to zoom in
        pyautogui.hotkey('win', '-')  # to zoom out
    except Exception as e:
        print(f"An error occurred: {e}")

def open_narrator():
    try:
        pyautogui.hotkey('win', 'ctrl', 'enter')
    except Exception as e:
        print(f"An error occurred: {e}")

def open_on_screen_keyboard():
    try:
        pyautogui.hotkey('win', 'ctrl', 'o')
    except Exception as e:
        print(f"An error occurred: {e}")

def open_ease_of_access_center():
    try:
        pyautogui.hotkey('win', 'u')
    except Exception as e:
        print(f"An error occurred: {e}")

def open_high_contrast_settings():
    try:
        pyautogui.hotkey('shift', 'alt', 'printscreen')
    except Exception as e:
        print(f"An error occurred: {e}")

def open_control_panel():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('control')
    pyautogui.press('enter')

def open_device_manager():
    pyautogui.hotkey('win', 'x', 'm')

def open_disk_management():
    pyautogui.hotkey('win', 'x', 'k')

def open_event_viewer():
    pyautogui.hotkey('win', 'x', 'v')

def open_performance_monitor():
    pyautogui.hotkey('win', 'x', 'p')

def open_power_options():
    pyautogui.hotkey('win', 'x', 'o')

def open_programs_and_features():
    pyautogui.hotkey('win', 'x', 'f')

def open_system_information():
    pyautogui.hotkey('win', 'x', 's')

def open_task_scheduler():
    pyautogui.hotkey('win', 'x', 't')

def open_disk_cleanup():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('cleanmgr')
    pyautogui.press('enter')

def open_remote_desktop_connection():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('mstsc')
    pyautogui.press('enter')

def open_services():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('services.msc')
    pyautogui.press('enter')

def open_system_configuration():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('msconfig')
    pyautogui.press('enter')

def open_registry_editor():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('regedit')
    pyautogui.press('enter')

def open_windows_security():
    pyautogui.hotkey('win', 'x', 'w')

def open_resource_monitor():
    pyautogui.hotkey('ctrl', 'shift', 'esc')
    pyautogui.press('ctrl+alt+delete')  
    # then select Task Manager, and go to Performance tab

def open_command_prompt_as_admin():
    pyautogui.hotkey('win', 'x', 'a')

def open_powershell_as_admin():
    pyautogui.hotkey('win', 'x', 'i')

def open_taskbar_settings():
    pyautogui.hotkey('win', 'i', 'e')

def open_system_settings():
    pyautogui.hotkey('win', 'i', 's')

def open_network_settings():
    pyautogui.hotkey('win', 'i', 'n')

def open_personalization_settings():
    pyautogui.hotkey('win', 'i', 'p')

def open_time_and_language_settings():
    pyautogui.hotkey('win', 'i', 't')

def open_privacy_settings():
    pyautogui.hotkey('win', 'i', 'v')

def open_update_and_security_settings():
    pyautogui.hotkey('win', 'i', 'u')

def open_ease_of_access_settings():
    pyautogui.hotkey('win', 'i', 'a')

def open_devices_settings():
    pyautogui.hotkey('win', 'i', 'd')

def open_phone_settings():
    pyautogui.hotkey('win', 'i', 'o')

def open_apps_settings():
    pyautogui.hotkey('win', 'i', 'x')

def open_account_settings():
    pyautogui.hotkey('win', 'i', 'y')


def open_file_explorer():
    pyautogui.hotkey('win', 'e')

def open_task_manager():
    pyautogui.hotkey('ctrl', 'shift', 'esc')

def open_command_prompt():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('cmd')
    pyautogui.press('enter')

def open_powershell():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('powershell')
    pyautogui.press('enter')

def open_snipping_tool():
    pyautogui.hotkey('win', 'shift', 's')

def open_calculator():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('calc')
    pyautogui.press('enter')

def open_notepad():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('notepad')
    pyautogui.press('enter')

def open_paint():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('mspaint')
    pyautogui.press('enter')

def open_wordpad():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('wordpad')
    pyautogui.press('enter')

def open_command_prompt_as_admin():
    pyautogui.hotkey('win', 'x', 'a')

def open_powershell_as_admin():
    pyautogui.hotkey('win', 'x', 'i')

def open_control_panel():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('control')
    pyautogui.press('enter')

def open_system_settings():
    pyautogui.hotkey('win', 'i', 's')

def open_network_settings():
    pyautogui.hotkey('win', 'i', 'n')

def open_display_settings():
    pyautogui.hotkey('win', 'i', 'd')

def open_sound_settings():
    pyautogui.hotkey('win', 'i', 'a')

def open_date_and_time_settings():
    pyautogui.hotkey('win', 'i', 't')

def open_disk_management():
    pyautogui.hotkey('win', 'x')
    pyautogui.press('k')

def open_event_viewer():
    pyautogui.hotkey('win', 'x')
    pyautogui.press('v')

def open_system_information():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('msinfo32')
    pyautogui.press('enter')

def open_services():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('services.msc')
    pyautogui.press('enter')

def open_task_scheduler():
    pyautogui.hotkey('win', 'x')
    pyautogui.press('s')

def open_remote_desktop():
    pyautogui.hotkey('win', 's')
    pyautogui.write('remote desktop')
    pyautogui.press('enter')

def open_firewall_settings():
    pyautogui.hotkey('win', 's')
    pyautogui.write('firewall')
    pyautogui.press('enter')

def open_system_properties():
    pyautogui.hotkey('win', 'pause')

def open_user_accounts():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('control userpasswords2')
    pyautogui.press('enter')


def open_device_manager():
    pyautogui.hotkey('win', 'x')
    pyautogui.press('m')

def open_performance_monitor():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('perfmon')
    pyautogui.press('enter')

def open_power_options():
    pyautogui.hotkey('win', 'x')
    pyautogui.press('o')

def open_system_restore():
    pyautogui.hotkey('win', 'x')
    pyautogui.press('r')

def open_system_configuration():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('msconfig')
    pyautogui.press('enter')

def open_computer_management():
    pyautogui.hotkey('win', 'x')
    pyautogui.press('c')

def open_disk_cleanup():
    pyautogui.hotkey('win', 'x')
    pyautogui.press('d')

def open_network_connections():
    pyautogui.hotkey('win', 'x')
    pyautogui.press('n')

def open_system_settings():
    pyautogui.hotkey('win', 'i')

def open_default_apps():
    pyautogui.hotkey('win', 'i')
    pyautogui.press(['down', 'down', 'down', 'enter'])


def open_run_dialog():
    pyautogui.hotkey('win', 'r')

def open_action_center():
    pyautogui.hotkey('win', 'a')

def open_settings():
    pyautogui.hotkey('win', 'i')

def open_task_view():
    pyautogui.hotkey('win', 'tab')

def open_cortana():
    pyautogui.hotkey('win', 's')

def open_notification_center():
    pyautogui.hotkey('win', 'v')

def open_clipboard_history():
    pyautogui.hotkey('win', 'v')  # for Windows 10 version 1809 and later

def open_snipping_tool():
    pyautogui.hotkey('win', 'shift', 's')  # for Windows 10 version 1809 and later

def open_magnifier():
    pyautogui.hotkey('win', '+')  # to zoom in
    pyautogui.hotkey('win', '-')  # to zoom out

def open_narrator():
    pyautogui.hotkey('win', 'ctrl', 'enter')

def open_on_screen_keyboard():
    pyautogui.hotkey('win', 'ctrl', 'o')

def open_ease_of_access_center():
    pyautogui.hotkey('win', 'u')

def open_high_contrast_settings():
    pyautogui.hotkey('shift', 'alt', 'printscreen')

def toggle_wifi(enable):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    if enable:
        iface.scan()
        time.sleep(2)
        profile = pywifi.Profile()
        profile.ssid = "YOUR_WIFI_SSID"
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_NONE)
        profile.cipher = const.CIPHER_TYPE_CCMP
        iface.remove_all_network_profiles()
        temp_profile = iface.add_network_profile(profile)
        iface.connect(temp_profile)
    else:
        iface.disconnect()



def set_dark_mode(enable):
    try:
        # Open the registry key for Personalization settings
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", 0, winreg.KEY_WRITE)

        # Enable or disable dark mode by setting the AppModeLight key
        if enable:
            winreg.SetValueEx(key, "AppsUseLightTheme", 0, winreg.REG_DWORD, 0)
        else:
            winreg.SetValueEx(key, "AppsUseLightTheme", 0, winreg.REG_DWORD, 1)

        # Close the registry key
        winreg.CloseKey(key)

        print("Dark mode is enabled." if enable else "Dark mode is disabled.")
    except Exception as e:
        print("An error occurred:", e)


def set_display_brightness(query):
    # Define a list of keywords that may indicate the brightness percentage in the query
    percentage_keywords = ["brightness", "percentage", "%", "set", "to"]
    
    # Normalize the query by converting to lowercase and removing unnecessary words
    processed_query = query.lower()
    
    # Remove percentage-related keywords from the query
    for keyword in percentage_keywords:
        processed_query = processed_query.replace(keyword, "").strip()
    
    # Use regular expression to extract the percentage value from the processed query
    match = re.search(r'(\d{1,3})', processed_query)
    
    if match:
        brightness_str = match.group(1)  # Extract the matched digits as a string
        try:
            brightness = int(brightness_str)
            # Ensure brightness is within the valid range (0 to 100)
            brightness = min(max(brightness, 0), 100)
            # Set the display brightness using screen_brightness_control library
            sbc.set_brightness(brightness)
            print(f"Display brightness set to {brightness}%")
        except ValueError:
            print("Invalid brightness value. Please provide a valid percentage (0-100).")
        except sbc.ScreenBrightnessError as e:
            print(f"Error: {e}")
            print("Failed to set display brightness.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Failed to set display brightness.")
    else:
        print("Brightness percentage not found in the query. Please specify a valid percentage (0-100).")
def increase_display_brightness():
    current_brightness = sbc.get_brightness()
    new_brightness = min(current_brightness + 20, 100)
    set_display_brightness(new_brightness)

def decrease_display_brightness():
    current_brightness = sbc.get_brightness()
    new_brightness = max(current_brightness - 20, 0)
    set_display_brightness(new_brightness)