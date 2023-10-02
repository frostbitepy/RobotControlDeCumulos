import pyautogui
import time
import pygetwindow as gw



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
    # pyautogui.click(x_cedula_button, y_cedula_button)
    pyautogui.press('3')
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
            time.sleep(2)
            pyautogui.write(output_file_name)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('s')
            time.sleep(7)
            fix_excel()
            # close_current_excel_window()
            time.sleep(3)
            pyautogui.press('c')
        else:
            print("No se encuentra la imagen")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def close_current_excel_window():
    # Find the Excel window by title or other criteria
    excel_window = gw.getWindowsWithTitle("listado - Excel")

    # If there are Excel windows open, close the first one
    if excel_window:
        excel_window[0].close()
    else:
        print("No Excel window found.")


# Función que soluciona el problema de no poder abrir luego el Excel generado por Sebaot
def fix_excel():
    try:
        # Find the Excel window by title or other criteria
        excel_window = gw.getWindowsWithTitle("listado - Excel")
        time.sleep(2)

        # Simula escribir en la primera celda (A1)
        pyautogui.click(x=100, y=100)  # Reemplaza con las coordenadas correctas
        time.sleep(2)
        pyautogui.write('Texto de prueba')

        # Simula deshacer (Ctrl+Z)
        pyautogui.hotkey('ctrl', 'z')
        
        # Espera un momento para que la ventana de guardado aparezca (ajusta según sea necesario).
        time.sleep(2)
        # If there are Excel windows open, close the first one
        if excel_window:
            excel_window[0].close()
            # Save file
            pyautogui.press('g')
        else:
            print("No Excel window found.")
        
        print("Acciones realizadas con éxito.")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")


if __name__ == "__main__":
    fix_excel()