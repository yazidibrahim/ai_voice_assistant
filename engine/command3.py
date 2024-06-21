# import tensorflow as tf
import numpy as np
import nltk
# nltk.download('all')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pyttsx3
import speech_recognition as sr
import eel
import time
import datetime



commands = {
    ("time", "time","time is it now", "the time", "time please", "current time"): "time_now",
    ("wikipedia", "i need to search on wikipedia", "could you search on wikipedia", "search wikipedia please" ,"i want to look something up on wikipedia") : "wikipedia",
    ("play on youtube", "play something on youtube", "youtube please"): "youtube",
    ("search on google", "google search"): "google",
    ("check the internet speed", "test internet speed", "internet speed check"): "internet_speed",
    ("close the application", "quit the app"): "close",
    ("temperature in the city", "what's the temperature"): "temperature",
    ("weather", "current weather conditions"): "weather",
    ("take a photo", "click a picture", "capture an image"): "camera",
    ("latest news", "news updates"): "news",
    ("increase volume", "turn up the volume", "raise the volume"): "volume_up",
    ("decrease volume", "turn down the volume", "lower the volume"): "volume_down",
    ("mute sound", "mute audio", "silence"): "mute",
    ("start playing", "resume playback", "continue"): "play",
    ("pause playback", "stop playing"): "pause",
    ("open website", "navigate to website", "go to website"): "open_website",
    ("take screenshot", "capture screen", "screen grab"): "take_screenshot",
    ("shutdown", "turn off computer"): "shutdown",
    ("restart", "reboot system"): "restart",
    ("sleep mode", "put computer to sleep"): "sleep_mode",
    ("open folder", "explore directory", "navigate to folder"): "open_folder",
    ("create folder", "make directory", "new folder"): "create_folder",
    ("lock computer", "secure system"): "lock_computer",
    ("empty recyclebin", "clear recycle bin", "delete trash"): "empty_recycle_bin",
    ("system uptime", "how long system has been running", "uptime"): "get_system_uptime_hours",
    ("system information", "specs", "computer details"): "get_system_information",
    ("process list", "running programs", "current processes"): "get_process_list",
    ("battery info", "power status", "battery details"): "get_battery_info",
    ("switch between windows", "change active window", "switch application"): "switch_between_windows",
    ("minimize window", "hide window", "reduce window size"): "minimize_window",
    ("maximize window", "expand window", "enlarge window"): "maximize_window",
    ("close window", "close the window", "close this window"): "close_window",
    ("refresh", "refresh screen", "reload"): "refresh",
    ("restore down", "restore window down", "minimize and resize"): "restore_down",
    ("move window left", "shift window left"): "move_window_left",
    ("move window right", "shift window right"): "move_window_right",
    ("switch to next window", "next window", "move to next window"): "switch_to_next_window",
    ("switch to previous window", "previous window", "move to previous window"): "switch_to_previous_window",
    ("open task manager", "launch task manager", "start task manager"): "open_task_manager",
    ("lock screen", "lock workstation", "lock computer screen"): "lock_screen",
    ("switch virtual desktop left", "move to left virtual desktop", "go to left desktop"): "switch_virtual_desktop_left",
    ("switch virtual desktop right", "move to right virtual desktop", "go to right desktop"): "switch_virtual_desktop_right",
    ("minimize all windows", "minimize every window", "show desktop"): "minimize_all_windows",
    ("show desktop", "show all windows"): "show_desktop",
    ("open file explorer", "launch file explorer", "start file explorer"): "open_file_explorer",
    ("toggle full screen mode", "switch to full screen", "enter full screen"): "toggle_full_screen_mode",
    ("open run dialog", "launch run dialog", "start run dialog"): "open_run_dialog",
    ("open action center", "launch action center", "start action center"): "open_action_center",
    ("open settings", "launch settings", "start settings"): "open_settings",
    ("open task view", "launch task view", "start task view"): "open_task_view",
    ("open notification center", "launch notification center", "start notification center"): "open_notification_center",
    ("open clipboard history", "launch clipboard history", "start clipboard history"): "open_clipboard_history",
    ("open snipping tool", "launch snipping tool", "start snipping tool"): "open_snipping_tool",
    ("open magnifier", "launch magnifier", "start magnifier"): "open_magnifier",
    ("open narrator", "launch narrator", "start narrator"): "open_narrator",
    ("open on-screen keyboard", "launch on-screen keyboard", "start on-screen keyboard"): "open_on_screen_keyboard",
    ("open ease of access center", "launch ease of access center", "start ease of access center"): "open_ease_of_access_center",
    ("open high contrast settings", "launch high contrast settings", "start high contrast settings"): "open_high_contrast_settings",
    ("open control panel", "launch control panel", "start control panel"): "open_control_panel",
    ("open device manager", "launch device manager", "start device manager"): "open_device_manager",
    ("open disk management", "launch disk management", "start disk management"): "open_disk_management",
    ("open event viewer", "launch event viewer", "start event viewer"): "open_event_viewer",
    ("open performance monitor", "launch performance monitor", "start performance monitor"): "open_performance_monitor",
    ("open power options", "launch power options", "start power options"): "open_power_options",
    ("open programs and features", "launch programs and features", "start programs and features"): "open_programs_and_features",
    ("open system information", "launch system information", "start system information"): "open_system_information",
    ("open task scheduler", "launch task scheduler", "start task scheduler"): "open_task_scheduler",
    ("open disk cleanup", "launch disk cleanup", "start disk cleanup"): "open_disk_cleanup",
    ("open remote desktop connection", "launch remote desktop connection", "start remote desktop connection"): "open_remote_desktop_connection",
    ("open services", "launch services", "start services"): "open_services",
    ("open system configuration", "launch system configuration", "start system configuration"): "open_system_configuration",
    ("open registry editor", "launch registry editor", "start registry editor"): "open_registry_editor",
    ("open windows security", "launch windows security", "start windows security"): "open_windows_security",
    ("open resource monitor", "launch resource monitor", "start resource monitor"): "open_resource_monitor",
    ("open command prompt as admin", "launch command prompt as admin", "start command prompt as admin"): "open_command_prompt_as_admin",
    ("open taskbar settings", "launch taskbar settings", "start taskbar settings"): "open_taskbar_settings",
    ("open system settings", "launch system settings", "start system settings"): "open_system_settings",
    ("open network settings", "launch network settings", "start network settings"): "open_network_settings",
    ("open personalization settings", "launch personalization settings", "start personalization settings"): "open_personalization_settings",
    ("open time and language settings", "launch time and language settings", "start time and language settings"): "open_time_and_language_settings",
    ("open privacy settings", "launch privacy settings", "start privacy settings"): "open_privacy_settings",
    ("open update and security settings", "launch update and security settings", "start update and security settings"): "open_update_and_security_settings",
    ("open ease of access settings", "launch ease of access settings", "start ease of access settings"): "open_ease_of_access_settings",
    ("open devices settings", "launch devices settings", "start devices settings"): "open_devices_settings",
    ("open phone settings", "launch phone settings", "start phone settings"): "open_phone_settings",
    ("open apps settings", "launch apps settings", "start apps settings"): "open_apps_settings",
    ("open account settings", "launch account settings", "start account settings"): "open_account_settings",
    ("open powershell", "launch powershell", "start powershell"): "open_powershell",
    ("open calculator", "launch calculator", "start calculator"): "open_calculator",
    ("open notepad", "launch notepad", "start notepad"): "open_notepad",
    ("open paint", "launch paint", "start paint"): "open_paint",
    ("open wordpad", "launch wordpad", "start wordpad"): "open_wordpad",
    ("open system properties", "launch system properties", "start system properties"): "open_system_properties",
    ("open user accounts", "launch user accounts", "start user accounts"): "open_user_accounts",
    ("open network connections", "launch network connections", "start network connections"): "open_network_connections",
    ("open system restore", "launch system restore", "start system restore"): "open_system_restore",
    ("open computer management", "launch computer management", "start computer management"): "open_computer_management",
    ("open firewall settings", "launch firewall settings", "start firewall settings"): "open_firewall_settings",
    ("open display settings", "launch display settings", "start display settings"): "open_display_settings",
    ("open sound settings", "launch sound settings", "start sound settings"): "open_sound_settings",
    ("open date and time settings", "launch date and time settings", "start date and time settings"): "open_date_and_time_settings",
    ("open default apps", "launch default apps", "start default apps"): "open_default_apps",
    ("turn on wifi", "enable wifi", "activate wifi"): "turn_on_wifi",
    ("turn off wifi", "disable wifi", "deactivate wifi"): "turn_off_wifi",
    ("turn on darkmode", "enable dark mode", "activate dark mode"): "turn_on_darkmode",
    ("turn off darkmode", "disable dark mode", "deactivate dark mode"): "turn_off_darkmode",
    ("brightness to", "set brightness to"): "set_display_brightness",
    ("increase brightness", "raise brightness", "brighten display"): "increase_display_brightness",   
    ("decrease brightness", "lower brightness", "dim display"): "decrease_display_brightness",
    ("open", "launch", "start"): "openCommand3",
}



def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(lemmatized_tokens)

# Prepare data for training the intent classifier
X_train = []
y_train = []

for phrases, intent in commands.items():
    for phrase in phrases:
        X_train.append(preprocess_text(phrase))
        y_train.append(intent)

# Create TF-IDF vectorizer and Logistic Regression classifier pipeline
tfidf_vectorizer = TfidfVectorizer()
classifier = LogisticRegression(max_iter=1000)

model = Pipeline([
    ('tfidf', tfidf_vectorizer),
    ('clf', classifier)
])

# Fit the model on training data
model.fit(X_train, y_train)

# Function to recognize intent based on user query
def recognize_intent(query):
    preprocessed_query = preprocess_text(query)
    predicted_intent = model.predict([preprocessed_query])[0]
    return predicted_intent



# Updated allCommands function to include fuzzy matching and intent recognition
def allCommands(message=1):
    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
        





def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()


def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
       
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message=1):

    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    try:
        # Recognize intent based on the query
        intent = recognize_intent(query)
        print(intent)
        
        if intent == "time_now" and "time" in query:
            from engine.features import timenow
            timenow()
        elif intent == "wikipedia" and "wikipedia" in query:
            from engine.features import searchWikipedia
            searchWikipedia(query)
        elif intent == "youtube" and "youtube" in query:
            from engine.features import searchYoutube
            searchYoutube(query)
        elif intent == "google" and "google" in query:
            from engine.features import searchGoogle
            searchGoogle(query)
        elif intent == "internet_speed" and "internet speed" in query:
            from engine.features import internetSpeed
            internetSpeed()
        elif intent == "close" and "close" in query:
            from engine.features import CloseCommand3
            CloseCommand3()
        elif intent == "temperature" and "temperature" in query:
            from engine.features import temperature
            temperature(query)
        elif intent == "weather" and "weather" in query:
            from engine.features import weather
            weather(query)
        elif intent == "camera" and any(keyword in query for keyword in ["camera","photo","selfie"]) in query:
            from engine.features import clickmyphoto
            clickmyphoto()
        elif intent == "news" and "news" in query:
            from engine.features import news
            news(query)
        elif intent == "volume_up" and "volume" in query:
            from engine.features import volumeup
            volumeup()
        elif intent == "volume_down" and "volume" in query:
            from engine.features import volumedown
            volumedown()
        elif intent == "mute" and "mute" in  query:
            from engine.features import mute
            mute()
        elif intent == "play" and "play" in  query:
            from engine.features import play
            play()
        elif intent == "pause"  and "pause" in query:
            from engine.features import pause
            pause()
        elif intent == "open_website"  and "website" in query:
            from engine.features import website
            website(query)
        elif intent == "take_screenshot" and "screenshot" in query:
            from engine.features import screenshots
            screenshots()
        elif intent == "shutdown" and "shutdown" in query:
            from engine.features import shutdown
            shutdown()
        elif intent == "restart" and "restart" in query:
            from engine.features import restart
            restart()

        elif intent == "sleep_mode" and "sleep" in query:
            from engine.features import sleepmode
            sleepmode()

        elif intent == "open_folder" and "open folder" in query:
            from engine.features import openFile
            openFile(query)


        elif intent == "create_folder" and  "create folder" in query:
            from engine.features import createFolder
            print("Give folder name")
            speak("Give folder name")
            query=takecommand()
            createFolder(query)


        elif intent == "lock_computer" and "lock" in query:
            from engine.features import lock_computer
            lock_computer()

        elif intent == "empty_recycle_bin" and "recyclebin" in query:
            from engine.features import empty_recycle_bin
            empty_recycle_bin()

        elif intent == "get_system_uptime_hours" and "system uptime" in query:
            from engine.features import get_system_uptime_hours
            get_system_uptime_hours()

        elif intent == "get_system_information" and "system information" in query:
            from engine.features import get_system_information
            get_system_information()

        elif intent == "get_process_list" and "process list" in query:
            from engine.features import get_process_list
            get_process_list()

        elif intent == "get_battery_info"  and "battery" in query:
            from engine.features import get_battery_info
            get_battery_info()

        elif intent == "switch_between_windows"  and "switch" in query:
            from engine.features import switch_between_windows
            switch_between_windows()

        elif intent == "minimize_window" and "minimize" in query:
            from engine.features import minimize_window
            minimize_window()

        elif intent == "maximize_window" and "maximize" in query:
            from engine.features import maximize_window
            maximize_window()

        elif intent == "close_window" and "close" in query:
            from engine.features import close_window
            close_window()

        elif intent == "refresh" and "refresh" in query:
            from engine.features import refresh
            refresh()

        elif intent == "restore_down" and "restore down" in query:
            from engine.features import restore_down
            restore_down()
            
        elif intent == "move_window_left"  and "window left" in query:
            from engine.features import move_window_left
            move_window_left()

        elif intent == "move_window_right"  and "window right" in query:
            from engine.features import move_window_right
            move_window_right()

        elif intent == "switch_to_next_window" and "next window" in query:
            from engine.features import switch_to_next_window
            switch_to_next_window()

        elif intent == "switch_to_previous_window" and "previous window" in query:
            from engine.features import switch_to_previous_window
            switch_to_previous_window()

        elif intent == "open_task_manager" and "task manager" in query:
            from engine.features import open_task_manager
            open_task_manager()

        elif intent == "lock_screen" and "lock screen" in query:
            from engine.features import lock_screen
            lock_screen()

        elif intent == "switch_virtual_desktop_left" and  "vitrual desktop" in query:
            from engine.features import switch_virtual_desktop_left
            switch_virtual_desktop_left()

        elif intent == "switch_virtual_desktop_right"  and "virtual desktop" in query:
            from engine.features import switch_virtual_desktop_right
            switch_virtual_desktop_right()

        elif intent == "minimize_all_windows" and "minimise all windows" in query:
            from engine.features import minimize_all_windows
            minimize_all_windows()

        elif intent == "show_desktop" and "show desktop" in query:
            from engine.features import show_desktop
            show_desktop()

        elif intent == "open_file_explorer" and "open file explorer" in query:
            from engine.features import open_file_explorer
            open_file_explorer()

        elif intent == "toggle_full_screen_mode" and "toggle full screen mode" in query:
            from engine.features import toggle_full_screen_mode
            toggle_full_screen_mode()

        elif intent == "open_run_dialog"  and "open run" in query:
            from engine.features import open_run_dialog
            open_run_dialog()

        elif intent == "open_action_center"  and "open action center" in query:
            from engine.features import open_action_center
            open_action_center()

        elif intent == "open_settings" and "open settings" in query :
            from engine.features import open_settings
            open_settings()

        elif intent == "open_task_view" and "open task view" in query:
            from engine.features import open_task_view
            open_task_view()

        elif intent == "open_notification_center" and "open notification center" in query:
            from engine.features import open_notification_center
            open_notification_center()

        elif intent == "open_clipboard_history" and "open clipboard history" in query:
            from engine.features import open_clipboard_history
            open_clipboard_history()

        elif intent == "open_snipping_tool"  and "open snipping tool" in query:
            from engine.features import open_snipping_tool
            open_snipping_tool()
        elif intent == "open_magnifier" and  "open magnifier" in query:
            from engine.features import open_magnifier
            open_magnifier()

        elif intent ==  "open_narrator" and "open narrator" in query:
            from engine.features import open_narrator
            open_narrator()

        elif intent ==  "open_on_screen_keyboard" and "open on screen keyboard" in query:
            from engine.features import open_on_screen_keyboard
            open_on_screen_keyboard()

        elif intent ==  "open_ease_of_access_center" and "open ease of access center" in query:
            from engine.features import open_ease_of_access_center
            open_ease_of_access_center()

        elif intent ==  "open_high_contrast_settings" and "open high contrast settings" in query:
            from engine.features import open_high_contrast_settings
            open_high_contrast_settings()

        elif intent ==  "open_control_panel"  and "open control panel" in query:
            from engine.features import open_control_panel
            open_control_panel()

        elif intent ==  "open_device_manager"  and "open device manager" in query:
            from engine.features import open_device_manager
            open_device_manager()

        elif intent ==  "open_event_viewer" and "open event viewer" in query:
            from engine.features import open_event_viewer
            open_event_viewer()

        elif intent ==  "open_power_options" and "open power options" in query:
            from engine.features import open_power_options
            open_power_options()

        elif intent ==  "open_programs_and_features" and "open programs and features" in query:
            from engine.features import open_programs_and_features
            open_programs_and_features()

        elif intent ==  "open_system_information" and "open system information" in query:
            from engine.features import open_system_information
            open_system_information()

        elif intent ==  "open_task_scheduler"  and "open task scheduler" in query:
            from engine.features import open_task_scheduler
            open_task_scheduler()

        elif intent ==  "open_disk_cleanup"  and "open disk clean up" in query:
            from engine.features import open_disk_cleanup
            open_disk_cleanup()

        elif intent ==  "open_remote_desktop_connection" and "open remote desktop connection" in query:
            from engine.features import open_remote_desktop_connection
            open_remote_desktop_connection()

        elif intent ==  "open_services" and "open services" in query:
            from engine.features import open_services
            open_services()

        elif intent ==  "open_system_configuration" and "open system configuration" in query:
            from engine.features import open_system_configuration
            open_system_configuration()

        elif intent ==  "open_registry_editor" and "open registry editor" in query:
            from engine.features import open_registry_editor
            open_registry_editor()

        elif intent ==  "open_windows_security"  and "open windows security" in query:
            from engine.features import open_windows_security
            open_windows_security()

        elif intent ==  "open_resource_monitor" and  "open resource monitor" in query:
            from engine.features import open_resource_monitor
            open_resource_monitor()

        elif intent ==  "open_command_prompt_as_admin" and "open command prompt as admin" in query:
            from engine.features import open_command_prompt_as_admin
            open_command_prompt_as_admin()



        elif intent ==  "open_taskbar_settings" and "open taskbar settings" in query :
            from engine.features import open_taskbar_settings
            open_taskbar_settings()

        elif intent ==  "open_system_settings" and "open system settings" in query:
            from engine.features import open_system_settings
            open_system_settings()

        elif intent ==  "open_network_settings" and "open network settings" in query:
            from engine.features import open_network_settings
            open_network_settings()

        elif intent ==  "open_personalization_settings" and  "open personalization settings" in query:
            from engine.features import open_personalization_settings
            open_personalization_settings()

        elif intent ==  "open_time_and_language_settings" and "open time and language" in query:
            from engine.features import open_time_and_language_settings
            open_time_and_language_settings()

        elif intent ==  "open_privacy_settings" and "open privacy settings" in query:
            from engine.features import open_privacy_settings
            open_privacy_settings()

        elif intent ==  "open_update_and_security_settings" and "update and security settings" in query:
            from engine.features import open_update_and_security_settings
            open_update_and_security_settings()

        elif intent ==  "open_ease_of_access_settings" and "ease of access settings" in query:
            from engine.features import open_ease_of_access_settings
            open_ease_of_access_settings()

        elif intent ==  "open_devices_settings" and "devices settings" in query:
            from engine.features import open_devices_settings
            open_devices_settings()

        elif intent ==  "open_phone_settings"  and "phone settings" in query:
            from engine.features import open_phone_settings
            open_phone_settings()

        elif intent ==  "open_apps_settings" and "apps settings" in query:
            from engine.features import open_apps_settings
            open_apps_settings()

        elif intent ==  "open_account_settings" and "account settings" in query :
            from engine.features import open_account_settings
            open_account_settings()

        elif intent ==  "open_powershell" and "powershell" in query:
            from engine.features import open_powershell
            open_powershell()

        elif intent ==  "open_calculator" and "calculator" in query:
            from engine.features import open_calculator
            open_calculator()

        elif intent ==  "open_notepad" and "notepad" in query:
            from engine.features import open_notepad
            open_notepad()

        elif intent ==  "open_paint" and "paint" in query:
            from engine.features import open_paint
            open_paint()

        elif intent ==  "open_wordpad" and "wordpad" in query:
            from engine.features import open_wordpad
            open_wordpad()

        elif intent ==  "open_system_properties" and "system properties" in query:
            from engine.features import open_system_properties
            open_system_properties()

        elif intent ==  "open_user_accounts" and  "user accounts" in query:
            from engine.features import open_user_accounts
            open_user_accounts()

        elif intent ==  "open_network_connections"  and "network connections" in query:
            from engine.features import open_network_connections
            open_network_connections()
        elif intent ==  "open_system_restore" and "system restore" in query:
            from engine.features import open_system_restore
            open_system_restore()

        elif intent ==  "open_computer_management" and "computer management" in query:
            from engine.features import open_computer_management
            open_computer_management()

        elif intent ==  "open_default_apps" and "default apps" in query:
            from engine.features import open_default_apps
            open_default_apps()

        elif intent ==  "open_firewall_settings" and "firewall" in query:
            from engine.features import open_firewall_settings
            open_firewall_settings()

        elif intent ==  "open_display_settings"  and "display settings" in query:
            from engine.features import open_display_settings
            open_display_settings()

        elif intent ==  "open_sound_settings"  and "sound settings" in query:
            from engine.features import open_sound_settings
            open_sound_settings()

        elif intent ==  "open_date_and_time_settings" and "date and time settings" in query:
            from engine.features import open_date_and_time_settings
            open_date_and_time_settings()

        elif intent ==  "open_disk_management" and "disk management" in query :
            from engine.features import open_disk_management
            open_disk_management()

        elif intent ==  "open_performance_monitor" and "performance" in query:
            from engine.features import open_performance_monitor
            open_performance_monitor()

        elif intent ==  "turn_on_wifi" and "wifi" in query:
            from engine.features import toggle_wifi
            toggle_wifi(True)

        elif intent ==  "turn_off_wifi"  and "wifi" in query:
            from engine.features import toggle_wifi
            toggle_wifi(False)

        elif intent ==  "turn_on_darkmode"  and "dark mode" in query:
            from engine.features import set_dark_mode
            set_dark_mode(True)

        elif intent ==  "turn_off_darkmode" and "dark mode" in query:
            from engine.features import set_dark_mode
            set_dark_mode(False)

        elif intent ==  "set_display_brightness" and "brightness" in query:
            from engine.features import set_display_brightness
            set_display_brightness(query)

        elif intent ==  "increase_display_brightness" and "brightness" in query:
            from engine.features import increase_display_brightness
            increase_display_brightness()

        elif intent ==  "decrease_display_brightness" and "brightness" in query:
            from engine.features import decrease_display_brightness
            decrease_display_brightness()

        elif "open" in query:
            # from engine.features import openCommand2
            # openCommand2(query)
            from engine.features import openCommand3
            openCommand3(query)

        else:
            from engine.features import chatBot
            chatBot(query)
    except:
        print("error")
    
    eel.ShowHood()






