import pyautogui
import time
import subprocess

# Define the file path to the Sebaot application
ubicacionSebaot = "C:/SEBAOT/SebaotActu.exe"

# Define user and password (replace with actual credentials)
user = "ROBOT"
password = "Bot*2021"

def start_sebaot_application():
    time.sleep(3)
    # Command 1: Start the Sebaot application
    try:
        subprocess.Popen(ubicacionSebaot, shell=True)
    except Exception as e:
        print("Error:", str(e))

    # Command 2: Wait for Sebaot to open
    time.sleep(23)  # Adjust the delay as needed

    # Command 3: Enter the username
    pyautogui.typewrite(user)

    # Command 4: Press TAB to move to the password field
    pyautogui.press('tab')

    # Command 5: Enter the password
    pyautogui.typewrite(password)

    # Command 6: Press TAB to move to the "Login" button and press ENTER
    pyautogui.press('tab')
    pyautogui.press('enter')

    # Command 7: Wait for the Sebaot window to open (adjust the delay as needed)
    time.sleep(15)

    # Command 8: Set a window scope for Sebaot (you may need to modify this)
    # Replace the selector with the appropriate one for your application
    # For example, if the application's title is known, you can use:
    # pyautogui.click("Application Title")
    # to bring it to focus.

    # Further actions can be added based on your specific requirements.

def stop_sebaot_application():
    time.sleep(3)
    pyautogui.hotkey('alt', 'F4')
    pyautogui.press('s')

