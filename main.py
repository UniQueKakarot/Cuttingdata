import tkinter as tk
from tkinter import ttk

class Cuttingdata(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master = master
        self.font_size = ("San Francisco", 25)
        self.font_size1 = ("San Francisco", 30)
        master_frame = tk.Frame(self.master, bg='Grey', width='800', height='600').grid(row=0, column=0, rowspan=10, columnspan=10)
        #master_frame.grid(row=0, column=0)

        self.preview_body(master_frame)

    def preview_body(self, master):

        tk.Frame(master, bg='Black', width='750', height='100').grid(row=0, column=0, columnspan=2, sticky='N', pady=5)

        for i in range(1, 5):
            tk.Frame(master, bg='Black', width='390', height='50').grid(row=i, column=0, sticky='W', padx=5)
            tk.Frame(master, bg='Black', width='390', height='50').grid(row=i, column=1, sticky='E', padx=5)

        tk.Frame(master, bg='#333333', width='750', height='60').grid(row=5, column=0, columnspan=2, padx=5)

        for i in range(6, 8):
            tk.Frame(master, bg='Black', width='390', height='50').grid(row=i, column=0, sticky='W', padx=5)
            tk.Frame(master, bg='Black', width='390', height='50').grid(row=i, column=1, sticky='E', padx=5)

        #photo = tk.PhotoImage(file='C:\\Users\\Iver\\Pictures\\Cuttingdata\\Labelframe2.png')
        photo = tk.PhotoImage(file='./Assets/Labelframe2.png')
        label = tk.Label(master, bg='Grey', image=photo, text='Cutting Meter', compound='center', font=self.font_size)
        label.image = photo
        label.grid(row=1, column=0, sticky='W', padx=5)

        tk.Entry(master, bg='Grey', font=self.font_size1, relief='flat').grid(row=1, column=1, sticky='EWNS', padx=5)

        


win = tk.Tk()
win.geometry("800x600")
#win.resizable(width=False, height=False)

app = Cuttingdata(master=win)

if __name__ == '__main__':
    app.mainloop()
