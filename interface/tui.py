
# import only system from os
import os
 
# define our clear function
def clear():
 
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


class TUI:
    # @param v value of the progress bar
    # @param v maximum value of the progress bar
    # @param progbar_size = 80 progress bar's size
    # @param start = "[" progress bar starting string
    # @param end = "]" progress bar ending string
    # @param fill = "#" progress bar's fill character
    # @param gap = "#" progress bar's space character
    # @return string of the progress bar
    @staticmethod
    def progressBarString(v,maxv,progbar_size = 80,start="[",end="]",fill="#",gap=" "):
        f = v/maxv
        f *= progbar_size
        f = round(f)
        return start+fill*f+gap*(progbar_size-f)+end
    
    @staticmethod
    def __init__():
        TUI.buffer = "\n" # type: ignore
        TUI.information = {} # type: ignore
        pass

    @staticmethod
    def addInfo(name,value,maxvalue=-1,hasProgressBar=False):
        TUI.information[name]={"value":value,"maxvalue":maxvalue,"hasProgressBar":hasProgressBar} # type: ignore
         
    @staticmethod
    def clearInfo():
        TUI.information = {} # type: ignore
    
    @staticmethod
    def print(*text,sep=" ",end="\n"):
        t = False #Why, @cj05. Why?
        for i in text:
            if t:
                TUI.buffer+=sep # type: ignore
            TUI.buffer+=i # type: ignore
            t=True
        TUI.buffer+=end # type: ignore
        
    @staticmethod
    def clearconsole():
        TUI.buffer="\n" # type: ignore
    
    @staticmethod
    def render(isclrscr=True):
        if(isclrscr):
            clear()
            
        print("Colony Data")
        
        for key in TUI.information: # type: ignore
            #print(i)
            i = TUI.information[key] # type: ignore
            value = i["value"].getValue()
            if i["maxvalue"] >= 0:
                print(key,value,"/",i["maxvalue"])
                if i["hasProgressBar"]:
                    print(TUI.progressBarString(value,i["maxvalue"]))
            else:
                print(key,value)

        
        print("Booting system...")
        print(TUI.buffer.replace("\n","\n# "),end="") # type: ignore