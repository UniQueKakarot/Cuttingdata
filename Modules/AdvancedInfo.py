from pathlib import Path
import tkinter as tk
from tkinter import ttk

class AdvancedInfo():
    def __init__(self, master):
        self.master = master
        self.font1 = ("Consolas", 20)
        self.font2 = ("San Francisco", 22)
        
        master_frame = tk.LabelFrame(self.master, bg='Grey', borderwidth=0)
        master_frame.pack()

        self.body_test(master_frame, self.font1, self.font2)

    def body_test(self, master, font1, font2):

        for i in range(1, 5):
            tk.Label(master, bg='Grey', text='Hello', font=font1).grid(row=i, column=0, sticky='W', pady=2, padx=2)
            tk.Entry(master, font=font2).grid(row=i, column=1, sticky='WE')

    def body(self, master):
        pass