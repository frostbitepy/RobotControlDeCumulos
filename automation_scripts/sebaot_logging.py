import pyautogui
import time
import subprocess
from automation_scripts.script_logger import logger


# Define the file path to the Sebaot application
ubicacionSebaot = "C:/SEBAOT/SebaotActu.exe"
imagen_sebaot = "resources/images/imagen_sebaot.png"
x_sebaot, y_sebaot = 649, 369
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
        logger.error("Error: %s", str(e))

    # Command 2: Wait for Sebaot to open
    time.sleep(25)

    try:
        if pyautogui.locateOnScreen(imagen_sebaot) is not None:
            pyautogui.click(x_sebaot, y_sebaot)
        else:
            print("No se encuentra la imagen")
            logger.error("No se encuentra la imagen de Sebaot")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        logger.error("An error occurred: No se pudo iniciar Sebaot - %s", str(e))

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

