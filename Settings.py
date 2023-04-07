
def open_settings():
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
    print(pitches)
    print(SoundLocation)
    def __is_digit(P):
        try:
            if int(P):
                return True
        except: 
            if P == "":
                return True
            return False
    
    
    def __validate_command(P):
        if len(P) in range(0,3) and __is_digit(P):   
            return True
        else: return False
    
    
    
        
    def __save_to_file(pitches:dict,sound_loc:dict):
        data = {
            "Pitches":pitches,
            "SoundLocations":sound_loc
        }
        from json import dump
        with open("settings.json","w") as f:
            dump(data,f)


    import tkinter as tk
    class __Label_Entry:
    
        def __init__(self,x,y,text) -> None:
            
            self.__x = x
            self.__y = y
            self.__text = text
            self.__PitchVar = pitches[text]
            self.__LocVar = SoundLocation[text]
            self.__entry_pitch = None
            self.__entry_loc = None
            self.__constructor()
        def __constructor(self):
            tk.Label(master = root,text=self.__text).place(x=self.__x,y=self.__y)
            
            self.__entry_pitch = tk.Entry(master = root,textvariable=self.__PitchVar,validate="key",validatecommand=vcmd)
            self.__entry_pitch.place(x=self.__x + 100,y=self.__y)
            self.__entry_pitch.insert(0,str(self.__PitchVar))
            self.__entry_loc = tk.Entry(master = root,textvariable=self.__LocVar,width=50)
            self.__entry_loc.place(x=self.__x + 300,y=self.__y)
            self.__entry_loc.insert(0,str(self.__LocVar))
        def get_pitch(self):
            if self.__entry_pitch.get() in [""," "]:
                return 0
            else:
                return int(self.__entry_pitch.get())
        def get_sound_location(self):
            if self.__entry_loc.get() in [""," "]:
                return "No_Location"
            else:
                return str(self.__entry_loc.get())

    def __save():
        pithces = {
    	"Crash": Crash.get_pitch(),
    	"HHc": HHc.get_pitch(),
    	"HHpedal": HHpedal.get_pitch(),
    	"Kick": Kick.get_pitch(),
    	"Ride": Ride.get_pitch(),
    	"Snare": Snare.get_pitch(),
    	"Tom1": Tom1.get_pitch(),
    	"Tom2": Tom2.get_pitch(),
    	"Tom3": Tom3.get_pitch()
        }
        sound_loc = {
            "Crash": Crash.get_sound_location(),
            "HHc": HHc.get_sound_location(),
            "HHpedal": HHpedal.get_sound_location(),
            "Kick": Kick.get_sound_location(),
            "Ride": Ride.get_sound_location(),
            "Snare": Snare.get_sound_location(),
            "Tom1": Tom1.get_sound_location(),
            "Tom2": Tom2.get_sound_location(),
            "Tom3": Tom3.get_sound_location()
        }
        tk.Label(master = root,text="Saved Data in settings.json").place(x=500,y=500)
        
        __save_to_file(pitches,sound_loc)
    root = tk.Tk()
    x = 10
    vcmd = (root.register(__validate_command),'%P')
    Crash = __Label_Entry(x,40,"Crash")
    HHc = __Label_Entry(x,80,"HHc")
    HHpedal = __Label_Entry(x,120,"HHpedal")
    Kick = __Label_Entry(x,160,"Kick")
    Ride = __Label_Entry(x,200,"Ride")
    Snare = __Label_Entry(x,240,"Snare")
    Tom1 = __Label_Entry(x,280,"Tom1")
    Tom2 = __Label_Entry(x,320,"Tom2")
    Tom3 = __Label_Entry(x,360,"Tom3")
    
    tk.Button(master = root,command=__save,text="save").place(x=400,y=550)
    
    root.title("Settings")
    root.geometry("800x600")
    root.resizable(width=False,height=False)
    tk.Button(master=root,command=lambda:root.destroy(),text="Quit").place(x=500,y=550)
    tk.mainloop()



if __name__ == "__main__":
    open_settings()