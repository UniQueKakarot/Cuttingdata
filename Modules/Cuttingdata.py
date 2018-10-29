from pathlib import Path
import tkinter as tk
from tkinter import ttk
from math import pi


class Cuttingdata():

    """ Cutting data calculator """

    def __init__(self, master, font1, font2):

        self.master = master
        self.font1 = font1
        self.font2 = font2

        self.rpm = tk.StringVar()
        self.feed = tk.StringVar()

        # Refrences to all entry widgets
        self.cutting_speed_entry = None
        self.diameter_entry = None
        self.teeths_entry = None
        self.feed_entry = None
        
        ttk.Style().configure('Dark.TEntry', background='#737373', font=("San Francisco", 25))

        master_frame = tk.LabelFrame(self.master, bg='Grey', borderwidth=0)
        master_frame.pack()

        self.body(master_frame, self.font1, self.font2)

    def body(self, master, font1, font2):

        """ Definition and creation of Cutting Speed gui """

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
        self.cutting_speed_entry = tk.Entry(master, bg='#737373', font=font2, relief='flat', justify='center')
        self.cutting_speed_entry.grid(row=1, column=1, sticky='EW', padx=8)

        diameter = tk.Label(master, bg='Grey', image=labelframe, text='Diameter', compound='center', font=font1)
        diameter.image = labelframe
        diameter.grid(row=2, column=0, sticky='W', padx=5)
        self.diameter_entry = tk.Entry(master, bg='#737373', font=font2, relief='flat', justify='center')
        self.diameter_entry.grid(row=2, column=1, sticky='EW', padx=8)

        teeths = tk.Label(master, bg='Grey', image=labelframe, text='Nr of teeths', compound='center', font=font1)
        teeths.image = labelframe
        teeths.grid(row=3, column=0, sticky='W', padx=5)
        self.teeths_entry = tk.Entry(master, bg='#737373', font=font2, relief='flat', justify='center')
        self.teeths_entry.grid(row=3, column=1, sticky='EW', padx=8)

        feed_text = tk.Label(master, bg='Grey', image=labelframe, text='Feed', compound='center', font=font1)
        feed_text.image = labelframe
        feed_text.grid(row=4, column=0, sticky='W', padx=5)
        self.feed_entry = tk.Entry(master, bg='#737373', font=font2, relief='flat', justify='center')
        self.feed_entry.grid(row=4, column=1, sticky='EW', padx=8)

        # Button
        tk.Button(master, bg='Grey', font=font2, text='Calculate', bd=3, command=self.calculations).grid(row=6, column=0, columnspan=2, sticky='EW', padx=15, pady=15)

        # Results labels
        result_image1 = Path('./Assets/Resultframe2.png')
        result_frame1 = tk.PhotoImage(file=result_image1)

        result_image2 = Path('./Assets/Resultframe3.png')
        result_frame2 = tk.PhotoImage(file=result_image2)

        result_rpm = tk.Label(master, bg='Grey', image=result_frame1, text='Spindel RPM', compound='center', font=font1)
        result_rpm.image = result_frame1
        result_rpm.grid(row=7, column=0, sticky='W', padx=5)

        output_rpm = tk.Label(master, bg='Grey', image=result_frame2, textvariable=self.rpm, compound='center', font=font1)
        output_rpm.image = result_frame2
        output_rpm.grid(row=7, column=1, sticky='E', padx=5)

        result_feed = tk.Label(master, bg='Grey', image=result_frame1, text='Feedrate', compound='center', font=font1)
        result_feed.image = result_frame1
        result_feed.grid(row=8, column=0, sticky='W', padx=5, pady=10)

        output_feed = tk.Label(master, bg='Grey', image=result_frame2, textvariable=self.feed, compound='center', font=font1)
        output_feed.image = result_frame2
        output_feed.grid(row=8, column=1, sticky='E', padx=5, pady=10)

    def calculations(self):

        """ Calculating Cutting Speed and Feedrate """

        cuttingspeed = self.cutting_speed_entry.get()
        cuttingspeed = cuttingspeed.replace(',', '.')
        try:
            cuttingspeed = float(cuttingspeed)
        except ValueError:
            cuttingspeed = 0

        diameter = self.diameter_entry.get()
        diameter = diameter.replace(',', '.')
        try:
            diameter = float(diameter)
        except ValueError:
            diameter = 0

        teehts = self.teeths_entry.get()
        teehts = teehts.replace(',', '.')
        try:
            teehts = float(teehts)
        except ValueError:
            teehts = 0

        feed = self.feed_entry.get()
        feed = feed.replace(',', '.')
        try:
            feed = float(feed)
        except ValueError:
            feed = 0

        try:
            rpm = (cuttingspeed * 1000.0) / (pi * diameter)
        except ZeroDivisionError:
            rpm = 0

        feedrate = feed * rpm * teehts

        self.rpm.set(int(round(rpm, 0)))
        self.feed.set(int(round(feedrate, 0)))
