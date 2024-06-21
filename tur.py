import pyttsx3
import speech_recognition as sr
import eel
import time
import datetime

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

        if any(keyword in query for keyword in ["time", "the time"]) :
            from engine.features import timenow
            timenow()
        
        elif "wikipedia" in query:
            from engine.features import searchWikipedia
            searchWikipedia(query)

        elif "youtube" in query:
            from engine.features import searchYoutube
            searchYoutube(query)

        elif "google" in query:
            from engine.features import searchGoogle
            searchGoogle(query)
        
        elif any(keyword in query for keyword in ["internet speed", "internetspeed"]) :
            from engine.features import internetSpeed
            internetSpeed()

        elif any(keyword in query for keyword in ["close", "close the","close application"]) :
            from engine.features import CloseCommand3
            CloseCommand3()
        
        elif "temperature" in query:
            from engine.features import temperature
            temperature(query)

        elif "weather" in query:
            from engine.features import weather
            weather(query)
        
        elif any(keyword in query for keyword in ["camera", "photo","snap","selfie"]) :
            from engine.features import clickmyphoto
            clickmyphoto()

        elif "news" in query:
            from engine.features import news
            news(query)

        elif any(keyword in query.lower() for keyword in ["volume up", "increase volume","volumeup","increasevolume"]) :
            from engine.features import volumeup
            volumeup()

        elif any(keyword in query for keyword in ["volume down", "decrease volume","volumedown","decreasevolume"]) :
            from engine.features import volumedown
            volumedown()

        elif "mute" in query:
            from engine.features import mute
            mute()

        elif "play" in query:
            from engine.features import play
            play()

        elif "pause" in query:
            from engine.features import pause
            pause()

        elif any(keyword in query for keyword in ["website", ".com","com"]) :
            from engine.features import website
            website(query)

        elif any(keyword in query for keyword in ['screenshot', 'screen shot','take screenshot']) :
            from engine.features import screenshots
            screenshots()

        elif any(keyword in query for keyword in ["shutdown", "shut down","system shutdown"]) :
            from engine.features import shutdown
            shutdown()

        elif any(keyword in query for keyword in ["restart", "restart system","restartsystem"]) :
            from engine.features import restart
            restart()

        elif any(keyword in query for keyword in ["sleep", "sleep mode","sleepmode"]) :
            from engine.features import sleepmode
            sleepmode()

        elif any(keyword in query for keyword in ["file","folder","directory","openfolder"]) :
            from engine.features import openFile
            openFile(query)

        
        elif any(keyword in query for keyword in ["create file","create folder","create directory","createfolder"]) :
            from engine.features import createFolder
            print("Give folder name")
            speak("Give folder name")
            query=takecommand()
            createFolder(query)

# ----------------------------------00000000000000000000000000000000--------------------------------
        
        elif any(keyword in query for keyword in ["lock computer", "lock system", "lock pc", "lock screen", "lock the screen"]):
            from engine.features import lock_computer
            lock_computer()

        elif any(keyword in query for keyword in ["empty recyclebin", "empty bin", "recyclebin empty", "bin empty", "empty the bin"]):
            from engine.features import empty_recycle_bin
            empty_recycle_bin()

        # elif any(keyword in query for keyword in ["create file", "make file", "generate file", "file creation"]):
        #     from engine.features import create_file
        #     create_file('test.txt')

        # elif any(keyword in query for keyword in ["delete file", "remove file", "erase file", "file deletion"]):
        #     from engine.features import delete_file
        #     delete_file('test.txt')

        # elif any(keyword in query for keyword in ["create folder", "make folder", "generate folder", "folder creation"]):
        #     from engine.features import create_folder
        #     create_folder('new_folder')

        # elif any(keyword in query for keyword in ["delete folder", "remove folder", "erase folder", "folder deletion"]):
        #     from engine.features import delete_folder
        #     delete_folder('new_folder')

        elif any(keyword in query for keyword in ["system uptime", "uptime"]):
            from engine.features import get_system_uptime_hours
            get_system_uptime_hours()

        elif any(keyword in query for keyword in ["system information", "system info"]):
            from engine.features import get_system_information
            get_system_information()

        elif any(keyword in query for keyword in ["process list", "list processes"]):
            from engine.features import get_process_list
            get_process_list()

        elif any(keyword in query for keyword in ["battery info", "battery information", "battery status"]):
            from engine.features import get_battery_info
            get_battery_info()

        elif any(keyword in query for keyword in ["switch between windows", "switch windows", "window switch"]):
            from engine.features import switch_between_windows
            switch_between_windows()

        elif any(keyword in query for keyword in ["minimize window", "minimize"]):
            from engine.features import minimize_window
            minimize_window()

        elif any(keyword in query for keyword in ["maximize window", "maximize"]):
            from engine.features import maximize_window
            maximize_window()

        elif any(keyword in query for keyword in ["close window", "close"]):
            from engine.features import close_window
            close_window()

        elif any(keyword in query for keyword in ["refresh", "refresh page"]):
            from engine.features import refresh
            refresh()

        elif any(keyword in query for keyword in ["restore down", "restore"]):
            from engine.features import restore_down
            restore_down()
            
        elif any(keyword in query for keyword in ["move window left", "move left", "move window"]) :
            from engine.features import move_window_left
            move_window_left()

        elif any(keyword in query for keyword in ["move window right", "move right"]) :
            from engine.features import move_window_right
            move_window_right()

        elif any(keyword in query for keyword in ["switch to next window", "next window", "next"]) :
            from engine.features import switch_to_next_window
            switch_to_next_window()

        elif any(keyword in query for keyword in ["switch to previous window", "previous window", "previous"]) :
            from engine.features import switch_to_previous_window
            switch_to_previous_window()

        elif any(keyword in query for keyword in ["open task manager", "task manager"]) :
            from engine.features import open_task_manager
            open_task_manager()

        elif any(keyword in query for keyword in ["lock screen", "lock"]) :
            from engine.features import lock_screen
            lock_screen()

        elif any(keyword in query for keyword in ["switch virtual desktop left", "virtual desktop left"]) :
            from engine.features import switch_virtual_desktop_left
            switch_virtual_desktop_left()

        elif any(keyword in query for keyword in ["switch virtual desktop right", "virtual desktop right"]) :
            from engine.features import switch_virtual_desktop_right
            switch_virtual_desktop_right()

        elif any(keyword in query for keyword in ["minimize all windows", "minimize all", "show desktop"]) :
            from engine.features import minimize_all_windows
            minimize_all_windows()

        elif any(keyword in query for keyword in ["show desktop", "show"]) :
            from engine.features import show_desktop
            show_desktop()

        elif any(keyword in query for keyword in ["open file explorer", "file explorer"]) :
            from engine.features import open_file_explorer
            open_file_explorer()

        elif any(keyword in query for keyword in ["toggle full screen mode", "full screen mode"]) :
            from engine.features import toggle_full_screen_mode
            toggle_full_screen_mode()

        elif any(keyword in query for keyword in ["open run dialog", "run dialog"]) :
            from engine.features import open_run_dialog
            open_run_dialog()

        elif any(keyword in query for keyword in ["open action center", "action center"]) :
            from engine.features import open_action_center
            open_action_center()

        elif any(keyword in query for keyword in ["open settings", "settings"]) :
            from engine.features import open_settings
            open_settings()

        elif any(keyword in query for keyword in ["open task view", "task view"]) :
            from engine.features import open_task_view
            open_task_view()

        # elif any(keyword in query for keyword in ["open cortana"]) :
        #     from engine.features import open_cortana
        #     open_cortana()

        elif any(keyword in query for keyword in ["open notification center", "notification center"]) :
            from engine.features import open_notification_center
            open_notification_center()

        elif any(keyword in query for keyword in ["open clipboard history", "clipboard history"]) :
            from engine.features import open_clipboard_history
            open_clipboard_history()

        elif any(keyword in query for keyword in ["open snipping tool", "snipping tool"]) :
            from engine.features import open_snipping_tool
            open_snipping_tool()
        elif any(keyword in query for keyword in ["open magnifier"]) :
            from engine.features import open_magnifier
            open_magnifier()

        elif any(keyword in query for keyword in ["open narrator"]) :
            from engine.features import open_narrator
            open_narrator()

        elif any(keyword in query for keyword in ["open on-screen keyboard", "on-screen keyboard"]) :
            from engine.features import open_on_screen_keyboard
            open_on_screen_keyboard()

        elif any(keyword in query for keyword in ["open ease of access center", "ease of access center"]) :
            from engine.features import open_ease_of_access_center
            open_ease_of_access_center()

        elif any(keyword in query for keyword in ["open high contrast settings", "high contrast settings"]) :
            from engine.features import open_high_contrast_settings
            open_high_contrast_settings()

        elif any(keyword in query for keyword in ["open control panel", "control panel"]) :
            from engine.features import open_control_panel
            open_control_panel()

        elif any(keyword in query for keyword in ["open device manager", "device manager"]) :
            from engine.features import open_device_manager
            open_device_manager()

        elif any(keyword in query for keyword in ["open disk management", "disk management"]) :
            from engine.features import open_disk_management
            open_disk_management()

        elif any(keyword in query for keyword in ["open event viewer", "event viewer"]) :
            from engine.features import open_event_viewer
            open_event_viewer()

        elif any(keyword in query for keyword in ["open performance monitor", "performance monitor"]) :
            from engine.features import open_performance_monitor
            open_performance_monitor()

        elif any(keyword in query for keyword in ["open power options", "power options"]) :
            from engine.features import open_power_options
            open_power_options()

        elif any(keyword in query for keyword in ["open programs and features", "programs and features"]) :
            from engine.features import open_programs_and_features
            open_programs_and_features()

        elif any(keyword in query for keyword in ["open system information", "system information"]) :
            from engine.features import open_system_information
            open_system_information()

        elif any(keyword in query for keyword in ["open task scheduler", "task scheduler"]) :
            from engine.features import open_task_scheduler
            open_task_scheduler()

        elif any(keyword in query for keyword in ["open disk cleanup", "disk cleanup"]) :
            from engine.features import open_disk_cleanup
            open_disk_cleanup()

        elif any(keyword in query for keyword in ["open remote desktop connection", "remote desktop connection"]) :
            from engine.features import open_remote_desktop_connection
            open_remote_desktop_connection()

        elif any(keyword in query for keyword in ["open services", "services"]) :
            from engine.features import open_services
            open_services()

        elif any(keyword in query for keyword in ["open system configuration", "system configuration"]) :
            from engine.features import open_system_configuration
            open_system_configuration()

        elif any(keyword in query for keyword in ["open registry editor", "registry editor"]) :
            from engine.features import open_registry_editor
            open_registry_editor()

        elif any(keyword in query for keyword in ["open windows security", "windows security"]) :
            from engine.features import open_windows_security
            open_windows_security()

        elif any(keyword in query for keyword in ["open resource monitor", "resource monitor"]) :
            from engine.features import open_resource_monitor
            open_resource_monitor()

        elif any(keyword in query for keyword in ["open command prompt as admin", "command prompt as admin"]) :
            from engine.features import open_command_prompt_as_admin
            open_command_prompt_as_admin()

        elif any(keyword in query for keyword in ["open powershell as admin", "powershell as admin"]) :
            from engine.features import open_powershell_as_admin
            open_powershell_as_admin()

        elif any(keyword in query for keyword in ["open taskbar settings", "taskbar settings"]) :
            from engine.features import open_taskbar_settings
            open_taskbar_settings()

        elif any(keyword in query for keyword in ["open system settings", "system settings"]) :
            from engine.features import open_system_settings
            open_system_settings()

        elif any(keyword in query for keyword in ["open network settings", "network settings"]) :
            from engine.features import open_network_settings
            open_network_settings()

        elif any(keyword in query for keyword in ["open personalization settings", "personalization settings"]) :
            from engine.features import open_personalization_settings
            open_personalization_settings()

        elif any(keyword in query for keyword in ["open time and language settings", "time and language settings"]) :
            from engine.features import open_time_and_language_settings
            open_time_and_language_settings()

        elif any(keyword in query for keyword in ["open privacy settings", "privacy settings"]) :
            from engine.features import open_privacy_settings
            open_privacy_settings()

        elif any(keyword in query for keyword in ["open update and security settings", "update and security settings"]) :
            from engine.features import open_update_and_security_settings
            open_update_and_security_settings()

        elif any(keyword in query for keyword in ["open ease of access settings", "ease of access settings"]) :
            from engine.features import open_ease_of_access_settings
            open_ease_of_access_settings()

        elif any(keyword in query for keyword in ["open devices settings", "devices settings"]) :
            from engine.features import open_devices_settings
            open_devices_settings()

        elif any(keyword in query for keyword in ["open phone settings", "phone settings"]) :
            from engine.features import open_phone_settings
            open_phone_settings()

        elif any(keyword in query for keyword in ["open apps settings", "apps settings"]) :
            from engine.features import open_apps_settings
            open_apps_settings()

        elif any(keyword in query for keyword in ["open account settings", "account settings"]) :
            from engine.features import open_account_settings
            open_account_settings()

        elif any(keyword in query for keyword in ["open command prompt", "command prompt"]) :
            from engine.features import open_command_prompt
            open_command_prompt()

        elif any(keyword in query for keyword in ["open powershell", "powershell"]) :
            from engine.features import open_powershell
            open_powershell()

        elif any(keyword in query for keyword in ["open calculator", "calculator"]) :
            from engine.features import open_calculator
            open_calculator()

        elif any(keyword in query for keyword in ["open notepad", "notepad"]) :
            from engine.features import open_notepad
            open_notepad()

        elif any(keyword in query for keyword in ["open paint", "paint"]) :
            from engine.features import open_paint
            open_paint()

        elif any(keyword in query for keyword in ["open wordpad", "wordpad"]) :
            from engine.features import open_wordpad
            open_wordpad()

        elif any(keyword in query for keyword in ["open system properties", "system properties"]) :
            from engine.features import open_system_properties
            open_system_properties()

        elif any(keyword in query for keyword in ["open user accounts", "user accounts"]) :
            from engine.features import open_user_accounts
            open_user_accounts()

        elif any(keyword in query for keyword in ["open network connections", "network connections"]) :
            from engine.features import open_network_connections
            open_network_connections()
        elif any(keyword in query for keyword in ["open system restore", "system restore"]) :
            from engine.features import open_system_restore
            open_system_restore()

        elif any(keyword in query for keyword in ["open computer management", "computer management"]) :
            from engine.features import open_computer_management
            open_computer_management()

        elif any(keyword in query for keyword in ["open network connections", "network connections"]) :
            from engine.features import open_network_connections
            open_network_connections()

        elif any(keyword in query for keyword in ["open system settings", "system settings"]) :
            from engine.features import open_system_settings
            open_system_settings()

        elif any(keyword in query for keyword in ["open default apps", "default apps"]) :
            from engine.features import open_default_apps
            open_default_apps()

        elif any(keyword in query for keyword in ["open firewall settings", "firewall settings"]) :
            from engine.features import open_firewall_settings
            open_firewall_settings()

        elif any(keyword in query for keyword in ["open disk cleanup", "disk cleanup"]) :
            from engine.features import open_disk_cleanup
            open_disk_cleanup()

        elif any(keyword in query for keyword in ["open remote desktop", "remote desktop"]) :
            from engine.features import open_remote_desktop
            open_remote_desktop()

        elif any(keyword in query for keyword in ["open system properties", "system properties"]) :
            from engine.features import open_system_properties
            open_system_properties()

        elif any(keyword in query for keyword in ["open device manager", "device manager"]) :
            from engine.features import open_device_manager
            open_device_manager()

        elif any(keyword in query for keyword in ["open performance monitor", "performance monitor"]) :
            from engine.features import open_performance_monitor
            open_performance_monitor()

        elif any(keyword in query for keyword in ["open power options", "power options"]) :
            from engine.features import open_power_options
            open_power_options()

        elif any(keyword in query for keyword in ["open system restore", "system restore"]) :
            from engine.features import open_system_restore
            open_system_restore()

        elif any(keyword in query for keyword in ["open system configuration", "system configuration"]) :
            from engine.features import open_system_configuration
            open_system_configuration()

        elif any(keyword in query for keyword in ["open registry editor", "registry editor"]) :
            from engine.features import open_registry_editor
            open_registry_editor()

        elif any(keyword in query for keyword in ["open resource monitor", "resource monitor"]) :
            from engine.features import open_resource_monitor
            open_resource_monitor()

        elif any(keyword in query for keyword in ["open command prompt as admin", "command prompt as admin"]) :
            from engine.features import open_command_prompt_as_admin
            open_command_prompt_as_admin()

        elif any(keyword in query for keyword in ["open powershell as admin", "powershell as admin"]) :
            from engine.features import open_powershell_as_admin
            open_powershell_as_admin()

        elif any(keyword in query for keyword in ["open taskbar settings", "taskbar settings"]) :
            from engine.features import open_taskbar_settings
            open_taskbar_settings()

        elif any(keyword in query for keyword in ["open display settings", "display settings"]) :
            from engine.features import open_display_settings
            open_display_settings()

        elif any(keyword in query for keyword in ["open sound settings", "sound settings"]) :
            from engine.features import open_sound_settings
            open_sound_settings()

        elif any(keyword in query for keyword in ["open date and time settings", "date and time settings"]) :
            from engine.features import open_date_and_time_settings
            open_date_and_time_settings()

        elif any(keyword in query for keyword in ["open disk management", "disk management"]) :
            from engine.features import open_disk_management
            open_disk_management()

        elif any(keyword in query for keyword in ["open event viewer", "event viewer"]) :
            from engine.features import open_event_viewer
            open_event_viewer()

        elif any(keyword in query for keyword in ["open services", "services"]) :
            from engine.features import open_services
            open_services()

        elif any(keyword in query for keyword in ["open task scheduler", "task scheduler"]) :
            from engine.features import open_task_scheduler
            open_task_scheduler()

        elif any(keyword in query for keyword in ["open firewall settings", "firewall settings"]) :
            from engine.features import open_firewall_settings
            open_firewall_settings()

        elif any(keyword in query for keyword in ["open device manager", "device manager"]) :
            from engine.features import open_device_manager
            open_device_manager()

        elif any(keyword in query for keyword in ["open system properties", "system properties"]) :
            from engine.features import open_system_properties
            open_system_properties()

        elif any(keyword in query for keyword in ["open performance monitor", "performance monitor"]) :
            from engine.features import open_performance_monitor
            open_performance_monitor()

        elif any(keyword in query for keyword in ["open power options", "power options"]) :
            from engine.features import open_power_options
            open_power_options()

        elif any(keyword in query for keyword in ["open system restore", "system restore"]) :
            from engine.features import open_system_restore
            open_system_restore()

        elif any(keyword in query for keyword in ["open system configuration", "system configuration"]) :
            from engine.features import open_system_configuration
            open_system_configuration()

        elif any(keyword in query for keyword in ["open registry editor", "registry editor"]) :
            from engine.features import open_registry_editor
            open_registry_editor()

        elif any(keyword in query for keyword in ["open resource monitor", "resource monitor"]) :
            from engine.features import open_resource_monitor
            open_resource_monitor()

        elif any(keyword in query for keyword in ["open command prompt as admin", "command prompt as admin"]) :
            from engine.features import open_command_prompt_as_admin
            open_command_prompt_as_admin()

        elif any(keyword in query for keyword in ["open powershell as admin", "powershell as admin"]) :
            from engine.features import open_powershell_as_admin
            open_powershell_as_admin()

        elif any(keyword in query for keyword in ["open taskbar settings", "taskbar settings"]) :
            from engine.features import open_taskbar_settings
            open_taskbar_settings()

        elif any(keyword in query for keyword in ["open display settings", "display settings"]) :
            from engine.features import open_display_settings
            open_display_settings()

        elif any(keyword in query for keyword in ["open sound settings", "sound settings"]) :
            from engine.features import open_sound_settings
            open_sound_settings()

        elif any(keyword in query for keyword in ["open date and time settings", "date and time settings"]) :
            from engine.features import open_date_and_time_settings
            open_date_and_time_settings()
        
        elif any(keyword in query for keyword in ["open network connections", "network connections"]) :
            from engine.features import open_network_connections
            open_network_connections()

        elif any(keyword in query for keyword in ["open system settings", "system settings"]) :
            from engine.features import open_system_settings
            open_system_settings()

        elif any(keyword in query for keyword in ["open default apps", "default apps"]) :
            from engine.features import open_default_apps
            open_default_apps()

        elif any(keyword in query for keyword in ["turn on wifi", "turnon wifi","turn on wi-fi","turnon wi-fi","wifi turnon","on wifi","on wi fi","on wi-fi","wifi on"]) :
            from engine.features import toggle_wifi
            toggle_wifi(True)

        elif any(keyword in query for keyword in ["turn off wifi", "turnoff wifi","turn off wi-fi","turnoff wi-fi","wifi turnoff","off wifi","off wi fi","off wi-fi","wifi off"]) :
            from engine.features import toggle_wifi
            toggle_wifi(False)

        elif any(keyword in query for keyword in ["turn on darkmode", "turnon darkmode","turn off lightmode","turnoff lightmode","on darkmode","off lightmode","on dark mode","off light mode"]) :
            from engine.features import set_dark_mode
            set_dark_mode(True)

        elif any(keyword in query for keyword in ["turn off darkmode", "turnoff darkmode","turn on lightmode","turnon lightmode","off darkmode","on lightmode","off dark mode","on light mode"]) :
            from engine.features import set_dark_mode
            set_dark_mode(False)

        elif any(keyword in query for keyword in ["brightness to", "set brightness","percentage","%","set brightness level"]) :
            from engine.features import set_display_brightness
            set_display_brightness(query)

        elif any(keyword in query for keyword in ["increase brightness","increase brightness level","increasebrightness","up brightness","brightness up"]) :
            from engine.features import increase_display_brightness
            increase_display_brightness()
            
        elif "open" in query:
            # from engine.features import openCommand2
            # openCommand2(query)
            from engine.features import openCommand3
            openCommand3(query)

        elif any(keyword in query for keyword in ["decrease brightness","decrease brightness level","decreasebrightness","down brightness","brightness down"]) :
            from engine.features import decrease_display_brightness
            decrease_display_brightness()
        else:
            from engine.features import chatBot
            chatBot(query)
    except:
        print("error")
    
    eel.ShowHood()