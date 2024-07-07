
def open_settings():
    def __get_data():
        import json
        with open("settings.json","r") as f:
            data = json.load(f)
        Dicts = (data["Pitches"],data["SoundLocations"],data["Sensitivities"])
        for i in Dicts:
            yield i
    gd = __get_data()
    pitches = gd.__next__()
    SoundLocation = gd.__next__()
    Sensitivities = gd.__next__()
    del gd
    
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
    
    
        
    def __save_to_file(pitches:dict,sound_loc:dict,sensitivities:dict):
        data = {
            "Pitches":pitches,
            "SoundLocations":sound_loc,
            "Sensitivities":sensitivities
        }
        from json import dump
        with open("settings.json","w") as f:
            dump(data,f)


    import tkinter as tk
    
    class _Parent_Label_Entry:
    
        def __init__(self,x,y,text) -> None:
            
            self.__x = x
            self.__y = y
            self._text = text
            self._PitchVar = ""
            self._LocVar = ""
            self._sensVar = ""
            self.__entry_name = None
            self.__entry_pitch = None
            self.__entry_loc = None
            self.__entry_sens = None
            
        def constructor(self):
            self.__entry_name = tk.Entry(master = root)
            self.__entry_name.place(x=self.__x,y=self.__y)
            self.__entry_name.insert(0,str(self._text))
            
            self.__entry_pitch = tk.Entry(master = root,validate="key",validatecommand=vcmd)
            self.__entry_pitch.place(x=self.__x + 100,y=self.__y)
            self.__entry_pitch.insert(0,str(self._PitchVar))

            self.__entry_loc = tk.Entry(master = root,width=50)
            self.__entry_loc.place(x=self.__x + 300,y=self.__y)
            self.__entry_loc.insert(0,str(self._LocVar))

            #Displays same number in every object's entry
            self.__entry_sens = tk.Entry(master = root,width=5,validate="key",validatecommand=vcmd)
            self.__entry_sens.place(x=self.__x + 600,y=self.__y)
            self.__entry_sens.insert(0,str(self._sensVar))

        def get_pitch(self):
            if self.__entry_pitch.get() in [""," "]:
                return 0
            else:
                return int(self.__entry_pitch.get())
        def get_sound_location(self):
            if self.__entry_loc.get() in [""," "]:
                return ""
            else:
                return str(self.__entry_loc.get())
        
        def get_sensitivity(self):
            if self.__entry_sens.get() in [""," "]:
                return 0
            else:
                return int(self.__entry_sens.get())
        def get_name(self):
            return self.__entry_name.get()

        def Destroy(self):
            self.__entry_name.destroy()
            self.__entry_pitch.destroy()
            self.__entry_loc.destroy()
            self.__entry_sens.destroy()
    
    class _Label_Entry(_Parent_Label_Entry):
        def __init__(self, x, y, text) -> None:
            super().__init__(x, y, text)
            self._PitchVar = pitches[self._text]
            self._LocVar = SoundLocation[self._text]
            self._sensVar = Sensitivities[self._text]

    class __New__Label_Entry(_Parent_Label_Entry):
        def __init__(self, x, y, text) -> None:
            super().__init__(x,y,text)
            
            


    def __save():
        pitches = {}
        sound_loc = {}
        sensitvities = {}
        for i in objects:
            name = i.get_name()
            pitches.update({name:i.get_pitch()})
            sound_loc.update({name:i.get_sound_location()})
            sensitvities.update({name:i.get_sensitivity()})
        tk.Label(master = root,text="Saved Data in settings.json").place(x=500,y=500)
        
        __save_to_file(pitches,sound_loc,sensitvities)

    def __create_field():
        global y
        y += 40
        objects.append(__New__Label_Entry(x,y,""))
        objects[-1].constructor()
        pass

    def __delete():
        global y
        y -= 40
        
        objects[-1].Destroy()
        
        objects.pop(-1)
        
    root = tk.Tk()
    global x 
    x = 10
    vcmd = (root.register(__validate_command),'%P')
    global y
    y = 0
    objects = []
    for i in list(SoundLocation.keys()):
        y += 40
        objects.append(_Label_Entry(x,y,i))
        
    for i in objects:
        i.constructor()
        tk.Button(master= root,command=__delete,text="Delete Last").place(x=200,y=550)
    tk.Button(master= root,command=__create_field,text="Create").place(x=300,y=550)
    tk.Button(master = root,command=__save,text="save").place(x=400,y=550)
    
    root.title("Settings")
    root.geometry("800x600")
    root.resizable(width=False,height=False)
    tk.Button(master=root,command=lambda:root.destroy(),text="Quit").place(x=500,y=550)
    tk.mainloop()



if __name__ == "__main__":
    open_settings()