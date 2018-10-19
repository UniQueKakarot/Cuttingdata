import tkinter as tk
from tkinter import ttk
from pathlib import Path

from Modules.Cuttingdata import Cuttingdata

class Main(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master = master
        self.font_size = ("Consolas", 23)
        self.font_size1 = ("San Francisco", 25)

        ttk.Style().configure('Dark.TNotebook', background='Grey')
        ttk.Style().configure('Dark.TFrame', background='Grey')

        self.tab_controll = ttk.Notebook(self.master, style='Dark.TNotebook')

        self.tab1 = ttk.Frame(self.tab_controll, style='Dark.TFrame')

        self.tab_controll.add(self.tab1, text='Tab 1')
        self.tab_controll.pack(expand=1, fill="both")

        self.master_frame = tk.LabelFrame(self.tab1, bg='Grey', borderwidth=0)
        self.master_frame.pack()

        basic_cuttingdata = Cuttingdata(self.master_frame, self.font_size, self.font_size1)


if __name__ == '__main__':
    win = tk.Tk()
    win.geometry("900x700")
    #win.resizable(width=False, height=False)

    app = Main(master=win)

    app.mainloop()
