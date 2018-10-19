from pathlib import Path
import tkinter as tk
from tkinter import ttk


class Cuttingdata():
    def __init__(self, master, font1, font2): #, tab_master):

        self.master = master
        #self.tab_master = tab_master
        self.font1 = font1
        self.font2 = font2

        ttk.Style().configure('Dark.TButton', background='#737373', font=("San Francisco", 25))

        self.body(self.master, self.font1, self.font2)

    def body(self, master, font1, font2):

        # Header image
        st_logo = Path('./Assets/ST.png')
        header = tk.PhotoImage(file=st_logo)

        main_header = tk.Label(master, bg='Grey', image=header)
        main_header.image = header
        main_header.grid(row=0, column=0, columnspan=2, sticky='S', pady=5)

        # Text label image and main labels
        frame = Path('./Assets/Labelframe3.png')
        labelframe = tk.PhotoImage(file=frame)

        cutting_speed = tk.Label(master, bg='Grey', image=labelframe, text='Cutting Speed', compound='center', font=font1)
        cutting_speed.image = labelframe
        cutting_speed.grid(row=1, column=0, sticky='W', padx=5)
        cutting_speed_entry = tk.Entry(master, bg='#737373', font=font2, relief='flat', justify='center').grid(row=1, column=1, sticky='EW', padx=8)

        diameter = tk.Label(master, bg='Grey', image=labelframe, text='Diameter', compound='center', font=font1)
        diameter.image = labelframe
        diameter.grid(row=2, column=0, sticky='W', padx=5)
        diameter_entry = tk.Entry(master, bg='#737373', font=font2, relief='flat', justify='center').grid(row=2, column=1, sticky='EW', padx=8)

        teeths = tk.Label(master, bg='Grey', image=labelframe, text='Nr of teeths', compound='center', font=font1)
        teeths.image = labelframe
        teeths.grid(row=3, column=0, sticky='W', padx=5)
        teeths_entry = tk.Entry(master, bg='#737373', font=font2, relief='flat', justify='center').grid(row=3, column=1, sticky='EW', padx=8)

        feed = tk.Label(master, bg='Grey', image=labelframe, text='Feed', compound='center', font=font1)
        feed.image = labelframe
        feed.grid(row=4, column=0, sticky='W', padx=5)
        feed_entry = tk.Entry(master, bg='#737373', font=font2, relief='flat', justify='center').grid(row=4, column=1, sticky='EW', padx=8)

        # Button
        tk.Button(master, bg='Grey', font=font2, text='Calculate').grid(row=6, column=0, columnspan=2, sticky='EW', padx=15, pady=10)

        # Results labels
        result_image1 = Path('./Assets/Resultframe2.png')
        result_frame1 = tk.PhotoImage(file=result_image1)

        result_image2 = Path('./Assets/Resultframe3.png')
        result_frame2 = tk.PhotoImage(file=result_image2)

        label3 = tk.Label(master, bg='Grey', image=result_frame1, text='Spindel RPM', compound='center', font=font1)
        label3.image = result_frame1
        label3.grid(row=7, column=0, sticky='W', padx=5)

        label4 = tk.Label(master, bg='Grey', image=result_frame2, text='Test2', compound='center', font=font1)
        label4.image = result_frame2
        label4.grid(row=7, column=1, sticky='E', padx=5)

        label5 = tk.Label(master, bg='Grey', image=result_frame1, text='Feedrate', compound='center', font=font1)
        label5.image = result_frame1
        label5.grid(row=8, column=0, sticky='W', padx=5, pady=10)

        label6 = tk.Label(master, bg='Grey', image=result_frame2, text='Test4', compound='center', font=font1)
        label6.image = result_frame2
        label6.grid(row=8, column=1, sticky='E', padx=5, pady=10)