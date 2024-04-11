import tkinter

from Recover import *
from customtkinter import *

class App(CTk):

    # Credits to HyperNylium (https://github.com/TomSchimansky/CustomTkinter/discussions/1820)
    def CenterWindowToDisplay(Screen: CTk, width: int, height: int, scale_factor: float = 1.0):

        screen_width = Screen.winfo_screenwidth()
        screen_height = Screen.winfo_screenheight()

        x = int(((screen_width/2) - (width/2)) * scale_factor)
        y = int(((screen_height/2) - (height/2)) * scale_factor)

        return f"{width}x{height}+{x}+{y}"
    
    app = CTk()

    app.geometry(CenterWindowToDisplay(app, 900, 600, app._get_window_scaling()))
    app.title("GDAR")

    app.mainloop()

if __name__ == "__main__":
    App()