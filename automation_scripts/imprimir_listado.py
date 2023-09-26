import pyautogui
import time


output_file_name = "listado.xlsx"
imagen_asegurado = "resources/images/imagen_asegurado.png"
x_seguros_button, y_seguros_button = 886, 658
x_cedula_button, y_cedula_button = 346, 654


def generar_listado_sebaot(documento):
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'm')
    time.sleep(2)
    pyautogui.typewrite("asegurados vida")
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x_cedula_button, y_cedula_button)
    time.sleep(2)
    pyautogui.write(documento)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)

    # Identificar si el asegurado tiene operaciones vigentes para
    # proceder a imprimir el listado
    try:
        if pyautogui.locateOnScreen(imagen_asegurado) is not None:
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.click(x_seguros_button, y_seguros_button)
            time.sleep(2)
            pyautogui.press("right")
            pyautogui.press("right")
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('e')
            pyautogui.press('e')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.write(output_file_name)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('s')
        else:
            print("No se encuentra la imagen")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

