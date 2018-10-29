import tkinter as tk
from tkinter import ttk

from Modules.Cuttingdata import Cuttingdata
from Modules.AdvancedInfo import AdvancedInfo
from Modules.MaterialRemoval import MaterialRemovalRate

class Main(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master = master
        self.font1 = ("Consolas", 23)
        self.font2 = ("San Francisco", 25)

        ttk.Style().configure('Dark.TNotebook', background='Grey')
        ttk.Style().configure('Dark.TFrame', background='Grey')

        self.tab_controll = ttk.Notebook(self.master, style='Dark.TNotebook')

        self.tab1 = ttk.Frame(self.tab_controll, style='Dark.TFrame')
        self.tab2 = ttk.Frame(self.tab_controll, style='Dark.TFrame')

        self.tab_controll.add(self.tab1, text='Cutting Speed')
        self.tab_controll.add(self.tab2, text='Material Removal')

        self.tab_controll.pack(expand=1, fill="both")

        basic_cuttingdata = Cuttingdata(self.tab1, self.font1, self.font2)
        #advanced_cuttingdata = AdvancedInfo(self.tab2)
        material_removal = MaterialRemovalRate(self.tab2, self.font1, self.font2)


if __name__ == '__main__':
    win = tk.Tk()
    win.geometry("900x700")
    #win.resizable(width=False, height=False)

    app = Main(master=win)

    app.mainloop()
