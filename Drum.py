import pygame.midi as midi
import pygame.mixer as mixer
import tkinter as tk

global num
num = 80

class Pad:
    def __init__(self,name:str,sound_path:str,pitch:int,channel:int,sensitivity:int = 80) -> None:
        self.name = name
        self.__pitch = pitch
        self.__sensitivity = sensitivity
        self.__channel = channel
        print(name)
        self.__sound = mixer.Sound(sound_path)

    def Play_Sound(self,pitch:int,velocity:int):
        if pitch == self.__pitch and velocity > 100 - self.__sensitivity:
            #vol = velocity / self.__sensitivity
            #mixer.Channel(self.__channel).set_volume(vol)
            mixer.Channel(self.__channel).play(self.__sound)

def __get_data():
    import json
    with open("settings.json","r") as f:
        data = json.load(f)
    Dicts = (data["Pitches"],data["SoundLocations"],data["Sensitivities"])
    for i in Dicts:
        print(i)
        yield i
gd = __get_data()
pitches = gd.__next__()
SoundLocation = gd.__next__()
Sensitivity = gd.__next__()

del gd
mixer.init()


names = list(pitches.keys())
Sound_paths = list(SoundLocation.values())
pitches = list(pitches.values())
Sensitivities = list(Sensitivity.values())
pops = []
for Index in range(0,len(names)):
    if Sound_paths[Index] in ["No_Location",""," "]:
        pops.append(Index)
pops.sort(reverse= True)
for i in pops:
    names.pop(i)
    Sound_paths.pop(i)
    pitches.pop(i)
    Sensitivities.pop(i)

len_of_instruments = len(names)
mixer.set_num_channels(len_of_instruments - 1)
channels = [i for i in range(len_of_instruments)]
global objects

objects = [Pad(name,sound_path,pitch,channel,sensitivity) 
for name,sound_path,pitch,channel,sensitivity 
in zip(names,Sound_paths,pitches,channels,Sensitivities)]

del names,Sound_paths,pitches,channels,Sensitivities

#Test Midi output from pygame
def __Trigger_Sound(pitch,velocity):
    for i in objects:
        i.Play_Sound(pitch,velocity)
 
def __play():
    mixer.init()
    midi_input = midi.Input(device_id=default_id)
    print("press f to stop")
    from keyboard import is_pressed
    while True:
      results = midi_input.read(num_events=3)
      
      if len(results) > 0:
        if results[0][0][1] > 0:
            __Trigger_Sound(results[0][0][1],results[0][0][2]) 
      if is_pressed("f"):
        break
    root.destroy()

def drum():
    midi.init()
    global default_id
    default_id = midi.get_default_input_id()
    if default_id != -1:
        tk.Label(master=root,text="You are ready to drum\nPress f to stop").pack()
        tk.Button(master=root,text="Start",command=__play).pack()        
        
    else:
        tk.Label(master=root,text="No device found").pack()
        print("No device found")
    
    mixer.quit()

def Drum():
    global root
    root = tk.Tk()
    root.title("Drum")
    root.geometry("800x600")
    root.after(1,drum)
    root.mainloop()
if __name__=="__main__":
    Drum()

