import tkinter as tk
from tkinter import ttk

class Cuttingdata(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master = master
        master_frame = tk.Frame(self.master, bg='Grey', width='800', height='600')
        master_frame.grid(row=0, column=0, rowspan=10, columnspan=10)

        self.preview_body(master_frame)

        """
        header = tk.Frame(self.master_frame, bg='Black', width='750', height='60').grid(row=0, column=0, columnspan=2, sticky='N', pady=5)

        tk.Frame(self.master_frame, bg='Black', width='390', height='40').grid(row=1, column=0, sticky='W', padx=5)
        tk.Frame(self.master_frame, bg='Black', width='390', height='40').grid(row=1, column=1, sticky='E', padx=5)

        #ttk.Style().configure('TButton', background='grey')
        #ttk.Button(self.master_frame, text="Hello World!", style='TButton').grid(row=0, column=0)
        """

    def preview_body(self, master):

        tk.Frame(master, bg='Black', width='750', height='100').grid(row=0, column=0, columnspan=2, sticky='N', pady=5)

        for i in range(1, 5):
            tk.Frame(master, bg='Black', width='390', height='60').grid(row=i, column=0, sticky='W', padx=5, pady=5)
            tk.Frame(master, bg='Black', width='390', height='60').grid(row=i, column=1, sticky='E', padx=5, pady=5)

        


win = tk.Tk()
win.geometry("800x600")
win.resizable(width=False, height=False)

app = Cuttingdata(master=win)

if __name__ == '__main__':
    app.mainloop()
