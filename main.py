import tkinter as tk
from tkinter import ttk
from pathlib import Path

class Cuttingdata(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master = master
        self.font_size = ("Consolas", 23)
        self.font_size1 = ("San Francisco", 25)
        master_frame = tk.Frame(self.master, bg='Grey', width='800', height='600').grid(row=0, column=0, rowspan=10, columnspan=10)
        #master_frame.grid(row=0, column=0)

        #self.preview_body(master_frame)
        self.asset_preview_body(master_frame)

    def preview_body(self, master):

        #tk.Frame(master, bg='Black', width='750', height='100').grid(row=0, column=0, columnspan=2, sticky='N', pady=5)
        st_logo = Path('./Assets/ST.png')
        header = tk.PhotoImage(file=st_logo)

        label1 = tk.Label(master, bg='Grey', image=header)
        label1.image = header
        label1.grid(row=0, column=0, columnspan=2, sticky='N', pady=5)

        for i in range(1, 5):
            tk.Frame(master, bg='Black', width='390', height='50').grid(row=i, column=0, sticky='W', padx=5)
            tk.Frame(master, bg='Black', width='390', height='50').grid(row=i, column=1, sticky='E', padx=5)

        tk.Frame(master, bg='#333333', width='750', height='60').grid(row=5, column=0, columnspan=2, padx=5)

        for i in range(6, 8):
            tk.Frame(master, bg='Black', width='390', height='50').grid(row=i, column=0, sticky='W', padx=5)
            tk.Frame(master, bg='Black', width='390', height='50').grid(row=i, column=1, sticky='E', padx=5)

        asset1 = Path('./Assets/Labelframe2.png')
        photo = tk.PhotoImage(file=asset1)
        label2 = tk.Label(master, bg='Grey', image=photo, text='Cutting Speed', compound='center', font=self.font_size)
        label2.image = photo
        label2.grid(row=1, column=0, sticky='W', padx=5)

        tk.Entry(master, bg='Grey', font=self.font_size1, relief='flat', justify='center').grid(row=1, column=1, sticky='EWNS', padx=5)

    def asset_preview_body(self, master):

        st_logo = Path('./Assets/ST.png')
        header = tk.PhotoImage(file=st_logo)

        label1 = tk.Label(master, bg='Grey', image=header)
        label1.image = header
        label1.grid(row=0, column=0, columnspan=2, sticky='N', pady=5)

        frame = Path('./Assets/Labelframe3.png')
        labelframe = tk.PhotoImage(file=frame)

        labeltext = ['Cutting Speed', 'Diameter', 'Teeths', 'Feed']
        for row, text in zip(range(1, 5), labeltext):

            label2 = tk.Label(master, bg='Grey', image=labelframe, text=text, compound='center', font=self.font_size)
            label2.image = labelframe
            label2.grid(row=row, column=0, sticky='W')

            tk.Entry(master, bg='#737373', font=self.font_size1, relief='flat', justify='center').grid(row=row, column=1, sticky='EW', padx=5)



        


win = tk.Tk()
win.geometry("800x600")
#win.resizable(width=False, height=False)

app = Cuttingdata(master=win)

if __name__ == '__main__':
    app.mainloop()
