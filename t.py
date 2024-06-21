

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

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_path = os.path.join(desktop_path, folder_name)

    try:
        os.mkdir(folder_path)
        print(f"Folder '{folder_name}' created successfully at '{folder_path}'.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists at '{folder_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")



def delete_folder(folder_name):
    try:
        # Attempt to delete folder from the desktop
        desktop_folder_path = os.path.join(os.path.expanduser("~"), "Desktop", folder_name)
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

def openCommand3(query):
    query = query.lower()
    query = query.replace("open","").replace("the","").replace("app", "").replace("application","").replace("launch","").replace(" ","")
    
    try:

        if "whatsapp" in query:
            # os.startfile('C:\\Path\\To\\Your\\Application.exe')
            os.startfile("whatsapp")  # Assuming WhatsApp is in the system's PATH
        elif "microsoft edge" in query:
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

    except FileNotFoundError:
        try:
            # Open the specified application
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


if 'open chrome' in query: 
    os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
elif 'maximize this window' in query: 
    pyautogui.hotkey('alt', 'space') 
    time.sleep(1) 
    pyautogui.press('x') 
elif 'google search' in query: 
    query = query.replace("google search", "") 
    pyautogui.hotkey('alt', 'd') 
    pyautogui.write(f"{query}", 0.1) 
    pyautogui.press('enter') 
elif 'youtube search' in query: 
    query = query.replace("youtube search", "") 
    pyautogui.hotkey('alt', 'd') 
    time.sleep(1) 
    pyautogui.press('tab') 
    pyautogui.press('tab') 
    pyautogui.press('tab') 
    pyautogui.press('tab') 
    time.sleep(1) 
    pyautogui.write(f"{query}", 0.1) 
    pyautogui.press('enter') 
elif 'open new window' in query: 
    pyautogui.hotkey('ctrl', 'n')
elif 'open incognito window' in query: 
    pyautogui.hotkey('ctrl', 'shift', 'n') 
elif 'minimise this window' in query: 
    pyautogui.hotkey('alt', 'space') 
    time.sleep(1) 
    pyautogui.press('n') 
elif 'open history' in query: 
    pyautogui.hotkey('ctrl', 'h') 
elif 'open downloads' in query: 
    pyautogui.hotkey('ctrl', 'j') 
elif 'previous tab' in query: 
    pyautogui.hotkey('ctrl', 'shift', 'tab') 
elif 'next tab' in query: 
    pyautogui.hotkey('ctrl', 'tab') 
elif 'close tab' in query: 
     pyautogui.hotkey('ctrl', 'w') 
elif 'close window' in query: 
    pyautogui.hotkey('ctrl', 'shift', 'w')
elif 'clear browsing history' in query: 
     pyautogui.hotkey('ctrl', 'shift', 'delete') 
elif 'close chrome' in query: 
    os.system("taskkill /f /im chrome.exe")