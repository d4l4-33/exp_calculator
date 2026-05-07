import tkinter as tk
from constants import *
from calculate_exp_gui import *



class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x600')
        self.root.title('Exp Calculator')
        self.root.config(background=BGR_COLOR)

        self.label = tk.Label(text='Exp Calculator by d4l4-33', font=FONT_TITLE, background=(BGR_COLOR), foreground=FRG_COLOR)
        self.label.pack(anchor='n', pady=10)

        self.start_dir = {'time': 0,
                        'level': 0,
                        'exp': 0,
                        'msg': ''
                        }
        self.start_frame = tk.Frame(self.root, width=300)
        self.start_lvl = tk.Entry(self.start_frame, width=15)
        self.start_lvl.grid(row=0, column=0, padx=5)
        self.start_exp = tk.Entry(self.start_frame, width=15)
        self.start_exp.grid(row=0, column=1)
        self.start_btn = tk.Button(self.start_frame, text='Start', font=FONT_BUTTON, width=5, command=self.click_start)
        self.start_btn.grid(row=0, column=2)
        self.start_frame.pack(pady=40)

        self.start_text = tk.Label(self.root, text="Waiting for input...", font=FONT_TEXT)
        self.start_text.pack(anchor='c')

        self.end_dir = {}
        self.end_frame = tk.Frame(self.root, width=300)
        self.end_lvl = tk.Entry(self.end_frame, width=15)
        self.end_lvl.grid(row=0, column=0, padx=5)
        self.end_exp = tk.Entry(self.end_frame, width=15)
        self.end_exp.grid(row=0, column=1)
        self.end_btn = tk.Button(self.end_frame, text="End", font=FONT_BUTTON, width=5, command=self.click_end)
        self.end_btn.grid(row=0, column=2)
        self.end_frame.pack(pady=50)

        self.clear_btn = tk.Button(self.root, text='clear', font=FONT_BUTTON, width=10, height=5, command=self.clear)
        self.clear_btn.pack(anchor='s', pady=20)

        self.root.mainloop()

    def click_start(self):
        self.start_return = start_exp(self.start_lvl.get(), self.start_exp.get())
        if type(self.start_return) == str:
            self.start_text.config(text=self.start_return)
            return
        self.start_text.config(text=f"Start: {time.strftime('%H:%M', self.start_return['time'])} | Level: {self.start_return['level']} | Experience %: {self.start_return['exp']} | Running...")
        
        
    
    def click_end(self):
        self.end_dir = end_exp(self.start_return, self.end_lvl, self.end_exp)

    def clear(self):
        self.start_lvl.delete(0, tk.END)
        self.start_exp.delete(0, tk.END)
        self.end_lvl.delete(0, tk.END)
        self.end_exp.delete(0, tk.END)
        self.start_text.config(text="Waiting for input...")

#for testing
GUI()


