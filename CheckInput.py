import pygame.midi as midi
#import tkinter as tk


def __check(default_id):
    midi_input = midi.Input(device_id=default_id)
    print("press f to stop")
    from keyboard import is_pressed
    while True:
        results = midi_input.read(num_events=3)
        if len(results) > 0:
            if results[0][0][0] != 248:
                print(f"pitch = {results[0][0][1]}") 
                print(f"velocity = {results[0][0][2]}")
            if is_pressed("f"):
                break

def check_input():
    """
    TextVar = ""
    TextVar2 = ""
    root = tk.Tk()
    root.geometry("800x600")
    root.resizable(width=False,height=False)
    tk.Label(master=root,text="Press f to stop!").pack
    global Pitch,Velocity
    Pitch = tk.Label(master=root,textvariable=TextVar).pack()
    Velocity = tk.Label(master=root,textvariable=TextVar2).pack()
    tk.Button(master=root,text="Quit",command=lambda:root.destroy()).pack()
    """
    midi.init()
    default_id = midi.get_default_input_id()
    if default_id != -1:
        __check(default_id)
        #root.destroy()
    else:
        print("NO DEVICE")
        #tk.Label(master=root,text="No Midi input device found!").pack()
        
    #tk.mainloop()
#results[0][0] [channel,pitch,velocity,?]











if __name__=="__main__":
    check_input()