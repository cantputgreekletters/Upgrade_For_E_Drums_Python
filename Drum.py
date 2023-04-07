import pygame.midi as midi
import pygame.mixer as mixer
import tkinter as tk

def __get_data():
    import json
    with open("settings.json","r") as f:
        data = json.load(f)
    Dicts = (data["Pitches"],data["SoundLocations"])
    for i in Dicts:
        print(i)
        yield i
gd = __get_data()
pitches = gd.__next__()
SoundLocation = gd.__next__()
del gd
mixer.init()
mixer.set_num_channels(8)
Snare = mixer.Sound(SoundLocation["Snare"])
Crash = mixer.Sound(SoundLocation["Crash"])
HHc = mixer.Sound(SoundLocation["OpenHH"])
#HHpedal = mixer.Sound(SoundLocation["HHpedal"])
Kick = mixer.Sound(SoundLocation["Kick"])
Ride = mixer.Sound(SoundLocation["Ride"])
Tom1 = mixer.Sound(SoundLocation["Tom1"])
Tom2 = mixer.Sound(SoundLocation["Tom2"])
Tom3 = mixer.Sound(SoundLocation["Tom3"])

#Test Midi output from pygame
def __Trigger_Sound(pitch):
    if pitch == pitches["Crash"]:
        mixer.Channel(0).play(Crash)
    if pitch == pitches["Kick"]:
        mixer.Channel(1).play(Kick)
    if pitch == pitches["HHc"]:
        mixer.Channel(2).play(HHc)
    if pitch == pitches["Ride"]:
        mixer.Channel(3).play(Ride)
    if pitch == pitches["Snare"]:
        mixer.Channel(4).play(Snare)   
    if pitch == pitches["Tom1"]:
        mixer.Channel(5).play(Tom1)
    if pitch == pitches["Tom2"]:
        mixer.Channel(6).play(Tom2)
    if pitch == pitches["Tom3"]:
        mixer.Channel(7).play(Tom3)
 
def __play(default_id):
    midi_input = midi.Input(device_id=default_id)
    print("press f to stop")
    from keyboard import is_pressed
    while True:
      results = midi_input.read(num_events=3)
      
      if len(results) > 0:
        __Trigger_Sound(results[0][0][1]) 
      if is_pressed("f"):
        break

def Drum():
    root = tk.Tk()
    root.geometry("800x600")
    root.resizable(width=False,height=False)
    tk.Button(master=root,command=lambda:root.destroy(),text="Quit").pack()
    midi.init()
    default_id = midi.get_default_input_id()
    if default_id != -1:
        __play(default_id)
        
        root.destroy()
    else:
        tk.Label(master=root,text="No midi input device found!").pack()
    root.mainloop()
    mixer.quit()

if __name__=="__main__":
    Drum()

