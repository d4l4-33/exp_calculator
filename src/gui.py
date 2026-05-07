import tkinter as tk
from tkinter import messagebox
from constants import *
from calculate_exp_gui import *



class GUI:
    def __init__(self):
        #startup
        self.root = tk.Tk()
        self.root.geometry('400x600')
        self.root.resizable(False, False)
        self.root.title('Exp Calculator')
        self.root.config(background=BGR_COLOR)


        #Title Font
        self.label = tk.Label(text='Exp Calculator by d4l4-33', font=FONT_TITLE, background=BGR_COLOR, foreground=FRG_COLOR)
        self.label.pack(anchor='n', pady=10)


        #Start Frame
        self.start_return = {}
        self.start_frame = tk.Frame(self.root, width=300, background=BUTTON_COLOR)
        self.start_label = tk.Label(self.start_frame, text='Starting level & exp %', font=FONT_TEXT, background=BUTTON_COLOR, foreground=FRG_COLOR)
        self.start_label.grid(row=0, column=1)
        #Level
        self.start_lvl = tk.Entry(self.start_frame, width=15)
        self.start_lvl.insert(0, PLACEHOLDER_TEXT[0])
        self.start_lvl.bind('<FocusIn>', self.on_entry_focus_in)
        self.start_lvl.bind('<FocusOut>', self.on_entry_focus_out)
        self.start_lvl.bind('<Return>', self.submit_start)
        self.start_lvl.grid(row=1, column=0, padx=5)
        #EXP
        self.start_exp = tk.Entry(self.start_frame, width=15)
        #Bind focusin
        self.start_exp.bind('<Return>', self.submit_start)
        self.start_exp.grid(row=1, column=1)
        #Button
        self.start_btn = tk.Button(self.start_frame, text='Start', font=FONT_BUTTON, width=5, command=self.click_start, background=BUTTON_COLOR, foreground=FRG_COLOR)
        self.start_btn.bind('<Return>', self.submit_start)
        self.start_btn.grid(row=1, column=2)
        self.start_frame.pack(pady=40)
        #Reply from start input
        self.start_text = tk.Label(self.root, text='Waiting for input...', font=FONT_TEXT, background=BGR_COLOR, foreground=FRG_COLOR)
        self.start_text.pack(anchor='c')


        #End Frame
        self.end_dir = {}
        self.end_frame = tk.Frame(self.root, width=300, background=BUTTON_COLOR)
        self.end_label = tk.Label(self.end_frame, text='End level & exp %', font=FONT_TEXT, background=BUTTON_COLOR, foreground=FRG_COLOR)
        self.end_label.grid(row=0, column=1)
        #Level
        self.end_lvl = tk.Entry(self.end_frame, width=15)
        self.end_lvl.bind('<Return>', self.submit_end)
        self.end_lvl.grid(row=1, column=0, padx=5)
        #EXP
        self.end_exp = tk.Entry(self.end_frame, width=15)
        self.end_exp.bind('<Return>', self.submit_end)
        self.end_exp.grid(row=1, column=1)
        #Button
        self.end_btn = tk.Button(self.end_frame, text='End', font=FONT_BUTTON, width=5, command=self.click_end, background=BUTTON_COLOR, foreground=FRG_COLOR)
        self.end_btn.bind('<Return>', self.submit_end)
        self.end_btn.grid(row=1, column=2)
        self.end_frame.pack(pady=50)
        #Reply from end input
        self.end_text = tk.Label(self.root, text='', font=FONT_TEXT, background=BGR_COLOR, foreground=FRG_COLOR)
        self.end_text.pack(anchor='c')

        #Class_Bind
        #self.start_lvl.bind_class('Entry', '<FocusIn>', self.on_entry_focus_in)
        #self.start_lvl.bind_class('Entry', '<FocusOut>', self.on_entry_focus_out)
        
        #Calculations/Instructions
        self.instructions_text = ('Enter your starting level and exp %, then press sumbit.\n'
        'When you are finished enter your final level and exp %.\n'
        '\nShortcuts:\n'
        'Escape: Close the calculator\n'
        'Return: Submit\n'
        'Ctrl + Return: Clear\n'
        'Tab: Jump between fields.')
        self.calc_text = tk.Label(self.root, text=self.instructions_text, font=FONT_TEXT, background=BGR_COLOR, foreground=FRG_COLOR)
        self.calc_text.pack(anchor='c', pady=10)

        #Clear Button
        self.clear_btn = tk.Button(self.root, text='clear', font=FONT_BUTTON, width=4, height=2, command=self.clear, background=BUTTON_COLOR, foreground=FRG_COLOR)
        self.clear_btn.pack(anchor='s', pady=50)
        self.root.bind('<KeyPress>', self.clear_shorcut)

        self.root.protocol('WM_DELETE_WINDOW', self.exit)
        self.root.bind('<Escape>', self.exit_shortcut)
        
        self.root.mainloop()

    def exit(self):
        if messagebox.askyesno(title='Quit?', message="Do you want to quit?"):
            self.root.destroy()

    def exit_shortcut(self, event):
        self.exit()

    def click_start(self):
        self.start_return = start_exp(self.start_lvl.get(), self.start_exp.get())
        if type(self.start_return) == str:
            self.start_text.config(text=self.start_return)
            return
        self.start_text.config(text=f"Start: {time.strftime('%H:%M', self.start_return['time'])} | Level: {self.start_return['level']} | Experience %: {self.start_return['exp']} | Running...")
            
    def click_end(self):
        self.end_return = end_exp(self.start_return, self.end_lvl.get(), self.end_exp.get())
        if type(self.end_return) == str:
            self.end_text.config(text=self.end_return)
            return
        self.start_text.config(text=f"Start: {time.strftime('%H:%M', self.start_return['time'])} | Level: {self.start_return['level']} | Experience %: {self.start_return['exp']}")
        self.end_text.config(text=f"End: {time.strftime('%H:%M', self.end_return['time'])} | Level: {self.end_return['level']} | Experience %: {self.end_return['exp']}")
        self.calc_text.config(text=calculate_exp(self.start_return, self.end_return))

    def clear(self):
        self.start_lvl.delete(0, tk.END)
        self.start_exp.delete(0, tk.END)
        self.end_lvl.delete(0, tk.END)
        self.end_exp.delete(0, tk.END)
        self.start_text.config(text="Waiting for input...")
        self.end_text.config(text='', background=BGR_COLOR)
        self.calc_text.config(text=self.instructions_text)
        self.start_lvl.focus_set()


    def on_entry_focus_in(self, event):
        if self.start_lvl.get() in PLACEHOLDER_TEXT:
            self.start_lvl.delete(0, tk.END)

    def on_entry_focus_out(self, event):
        if self.start_lvl.get() == '':
            self.start_lvl.insert(0, PLACEHOLDER_TEXT[0])

    def on_entry_test(self, event):
        print(event)


    def submit_start(self, event): 
        self.click_start()

    def submit_end(self, event): 
        self.click_end()

    def clear_shorcut(self, event):
        if event.state == 20 and event.keysym == 'Return':
            self.clear()

#for testing
GUI()


