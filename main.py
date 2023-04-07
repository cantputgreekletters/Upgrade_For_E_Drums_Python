import tkinter as tk

def Settings_Command():
    from Settings import open_settings
    open_settings()
    
def CheckInput_Command():
    from CheckInput import check_input
    check_input()

def Drum_Command():
    from Drum import Drum
    Drum()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("800x600")
    root.resizable(width=False,height=False)
    tk.Button(command=Settings_Command,text="Open Settings").pack()
    tk.Button(command=CheckInput_Command,text="Check Input").pack()
    tk.Button(command=Drum_Command,text="Drum").pack()
    tk.Button(master=root,command=lambda:root.destroy(),text="Quit").pack()
    root.mainloop()
