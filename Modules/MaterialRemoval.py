from pathlib import Path
import tkinter as tk
from tkinter import ttk

class MaterialRemovalRate():
    def __init__(self, master, font1, font2):
        self.master = master
        self.font1 = font1
        self.font2 = font2

        self.mrr = tk.StringVar()

        ttk.Style().configure('Dark.TSeparator', background='#000000')

        master_frame = tk.LabelFrame(self.master, bg='Grey', borderwidth=0)
        master_frame.pack()

        self.prewiev_body(master_frame, self.font1, self.font2)

    def prewiev_body(self, master, font1, font2):

        # Header image
        st_logo = Path('./Assets/mill.png')
        header = tk.PhotoImage(file=st_logo)

        main_header = tk.Label(master, bg='Grey', image=header)
        main_header.image = header
        main_header.grid(row=0, column=0, columnspan=2, sticky='S', pady=5)

        frame = Path('./Assets/Labelframe3.png')
        labelframe = tk.PhotoImage(file=frame)

        ap = tk.Label(master, bg='Grey', image=labelframe, text='Depth of Cut', compound='center', font=font1)
        ap.image = labelframe
        ap.grid(row=1, column=0, sticky='W', padx=5)
        self.ap_entry = tk.Entry(master, bg='#737373', font=font2, relief='flat', justify='center')
        self.ap_entry.grid(row=1, column=1, sticky='EW', padx=8)

        ae = tk.Label(master, bg='Grey', image=labelframe, text='Width of Cut', compound='center', font=font1)
        ae.image = labelframe
        ae.grid(row=2, column=0, sticky='W', padx=5)
        self.ae_entry = tk.Entry(master, bg='#737373', font=font2, relief='flat', justify='center')
        self.ae_entry.grid(row=2, column=1, sticky='EW', padx=8)

        feedrate = tk.Label(master, bg='Grey', image=labelframe, text='Feed Rate', compound='center', font=font1)
        feedrate.image = labelframe
        feedrate.grid(row=3, column=0, sticky='W', padx=5)
        self.feedrate_entry = tk.Entry(master, bg='#737373', font=font2, relief='flat', justify='center')
        self.feedrate_entry.grid(row=3, column=1, sticky='EW', padx=8)

        tk.Button(master, bg='Grey', font=font2, text='Calculate', bd=3).grid(row=4, column=0, columnspan=2, sticky='EW', padx=15, pady=45)

        # Results labels
        result_image1 = Path('./Assets/Resultframe2.png')
        result_frame1 = tk.PhotoImage(file=result_image1)

        result_image2 = Path('./Assets/Resultframe3.png')
        result_frame2 = tk.PhotoImage(file=result_image2)

        result_rpm = tk.Label(master, bg='Grey', image=result_frame1, text='Material Removal', compound='center', font=font1)
        result_rpm.image = result_frame1
        result_rpm.grid(row=5, column=0, sticky='W', padx=5)

        output_rpm = tk.Label(master, bg='Grey', image=result_frame2, textvariable=self.mrr, compound='center', font=font1)
        output_rpm.image = result_frame2
        output_rpm.grid(row=5, column=1, sticky='E', padx=5)
