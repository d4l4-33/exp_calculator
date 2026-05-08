import tkinter as tk
from tkinter import messagebox, PhotoImage
from constants import *
from calculate_exp_gui import *



class GUI:
    def __init__(self):
        #startup
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.geometry('600x600')
        self.root.title('Exp Calculator')
        self.root.iconphoto(True, PhotoImage(file='./src/GUI/exp_logo.png'))
        self.root.config(background=BGR_COLOR,)


        #Title Font
        self.label = tk.Label(text='Exp Calculator by d4l4-33', font=FONT_TITLE, background=BGR_COLOR, foreground=FRG_COLOR)
        self.label.pack(anchor='n', pady=10)


        self.start_label = tk.Label(self.root, text='Starting level & exp %', font=FONT_ENTRY, background=BGR_COLOR, foreground=FRG_COLOR)
        self.start_label.place(anchor='c', x=300, y=80)
        #Start Frame
        self.start_return = {}
        self.start_frame = tk.Frame(self.root, width=400, height=300, background=BUTTON_COLOR)
        #Level
        self.start_lvl = tk.Entry(self.start_frame, width=15, font=FONT_ENTRY, foreground=BUTTON_COLOR)
        self.start_lvl.insert(0, PLACEHOLDER_TEXT[0])
        self.start_lvl.bind('<FocusIn>', self.start_lvl_focus_in)
        self.start_lvl.bind('<FocusOut>', self.start_lvl_focus_out)
        self.start_lvl.bind('<Return>', self.submit_start)
        self.start_lvl.grid(row=0, column=0, padx=5)
        #EXP
        self.start_exp = tk.Entry(self.start_frame, width=15, font=FONT_ENTRY, foreground=BUTTON_COLOR)
        self.start_exp.insert(0, PLACEHOLDER_TEXT[1])
        self.start_exp.bind('<FocusIn>', self.start_exp_focus_in)
        self.start_exp.bind('<FocusOut>', self.start_exp_focus_out)
        self.start_exp.bind('<Return>', self.submit_start)
        self.start_exp.grid(row=0, column=1)
        #Button
        self.start_btn = tk.Button(self.start_frame, text='Start', font=FONT_BUTTON, width=5, command=self.click_start, background=BUTTON_COLOR, foreground=FRG_COLOR)
        self.start_btn.bind('<Return>', self.submit_start)
        self.start_btn.grid(row=0, column=2)
        self.start_frame.pack(pady=40)
        
        #Reply from start input
        self.start_text = tk.Label(self.root, text='Waiting for input...', font=FONT_TEXT, background=BGR_COLOR, foreground=FRG_COLOR)
        self.start_text.pack(anchor='s', pady=10)


        self.end_label = tk.Label(self.root, text='End level & exp %', font=FONT_ENTRY, background=BGR_COLOR, foreground=FRG_COLOR)
        self.end_label.place(anchor='c', x=300, y=230)
        #End Frame
        self.end_return = {}
        self.end_frame = tk.Frame(self.root, width=400, height=300, background=BUTTON_COLOR)
        #Level
        self.end_lvl = tk.Entry(self.end_frame, width=15, font=FONT_ENTRY, foreground=BUTTON_COLOR)
        self.end_lvl.insert(0, PLACEHOLDER_TEXT[0])
        self.end_lvl.bind('<FocusIn>', self.end_lvl_focus_in)
        self.end_lvl.bind('<FocusOut>', self.end_lvl_focus_out)
        self.end_lvl.bind('<Return>', self.submit_end)
        self.end_lvl.grid(row=0, column=0, padx=5)
        #EXP
        self.end_exp = tk.Entry(self.end_frame, width=15, font=FONT_ENTRY, foreground=BUTTON_COLOR)
        self.end_exp.insert(0, PLACEHOLDER_TEXT[1])
        self.end_exp.bind('<FocusIn>', self.end_exp_focus_in)
        self.end_exp.bind('<FocusOut>', self.end_exp_focus_out)
        self.end_exp.bind('<Return>', self.submit_end)
        self.end_exp.grid(row=0, column=1)
        #Button
        self.end_btn = tk.Button(self.end_frame, text='End', font=FONT_BUTTON, width=5, command=self.click_end, background=BUTTON_COLOR, foreground=FRG_COLOR)
        self.end_btn.bind('<Return>', self.submit_end)
        self.end_btn.grid(row=0, column=2)
        self.end_frame.pack(pady=40)
        #Reply from end input
        self.end_text = tk.Label(self.root, text='', font=FONT_TEXT, background=BGR_COLOR, foreground=FRG_COLOR)
        self.end_text.pack(anchor='c')

        #Calculations/Instructions
        self.instructions_text = ('Enter your starting level and exp %, then press start.\n'
        'When you are finished enter your final level and exp %.\n'
        '\nShortcuts:\n'
        'Escape: Close the calculator\n'
        'Return: Submit\n'
        'Ctrl + Return: Clear\n'
        'Tab: Jump between fields')
        self.calc_text = tk.Label(self.root, text=self.instructions_text, font=FONT_TEXT, background=BGR_COLOR, foreground=FRG_COLOR)
        self.calc_text.pack(anchor='c')

        #Clear Button
        self.clear_btn = tk.Button(self.root, text='Clear', font=FONT_BUTTON, width=5, height=3, command=self.clear, background=BUTTON_COLOR, foreground=FRG_COLOR)
        self.clear_btn.pack(anchor='s', pady=30)
        self.root.bind('<KeyPress>', self.clear_shorcut)

        self.root.protocol('WM_DELETE_WINDOW', self.exit)
        self.root.bind('<Escape>', self.exit_shortcut)
        
        self.root.mainloop()

    #Exit Functions
    def exit(self):
        if messagebox.askyesno(title='Quit?', message="Do you want to quit?"):
            self.root.destroy()

    def exit_shortcut(self, event):
        self.exit()

    #Submit Functions
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

    def submit_start(self, event):
        self.click_start()

    def submit_end(self, event): 
        self.click_end()

    #Clear Functions
    def clear(self):
        self.start_lvl.delete(0, tk.END)
        self.start_exp.delete(0, tk.END)
        self.start_exp.insert(0, PLACEHOLDER_TEXT[1])
        self.end_lvl.delete(0, tk.END)
        self.end_lvl.insert(0, PLACEHOLDER_TEXT[0])
        self.end_exp.delete(0, tk.END)
        self.end_exp.insert(0, PLACEHOLDER_TEXT[1])

        self.start_return = {}
        self.start_text.config(text="Waiting for input...")
        self.end_text.config(text='', background=BGR_COLOR)
        self.calc_text.config(text=self.instructions_text)
        self.start_lvl.focus_set()

    def clear_shorcut(self, event):
        if (event.state == 12 or event.state == 20) and event.keysym == 'Return':
            self.clear()

    #Focus In/out functions
    #Start
    def start_lvl_focus_in(self, event):
        if self.start_lvl.get() in PLACEHOLDER_TEXT:
            self.start_lvl.delete(0, tk.END)
            self.start_lvl.config(foreground=BGR_COLOR)
    def start_lvl_focus_out(self, event):
        if self.start_lvl.get() == '':
            self.start_lvl.insert(0, PLACEHOLDER_TEXT[0])
            self.start_lvl.config(foreground=BUTTON_COLOR)

    def start_exp_focus_in(self, event):
        if self.start_exp.get() in PLACEHOLDER_TEXT:
            self.start_exp.delete(0, tk.END)
            self.start_exp.config(foreground=BGR_COLOR)
    def start_exp_focus_out(self, event):
        if self.start_exp.get() == '':
            self.start_exp.insert(0, PLACEHOLDER_TEXT[1])
            self.start_exp.config(foreground=BUTTON_COLOR)
    #End
    def end_lvl_focus_in(self, event):
        if self.end_lvl.get() in PLACEHOLDER_TEXT:
            self.end_lvl.delete(0, tk.END)
            self.end_lvl.config(foreground=BGR_COLOR)
    def end_lvl_focus_out(self, event):
        if self.end_lvl.get() == '':
            self.end_lvl.insert(0, PLACEHOLDER_TEXT[0])
            self.end_lvl.config(foreground=BUTTON_COLOR)

    def end_exp_focus_in(self, event):
        if self.end_exp.get() in PLACEHOLDER_TEXT:
            self.end_exp.delete(0, tk.END)
            self.end_exp.config(foreground=BGR_COLOR)
    def end_exp_focus_out(self, event):
        if self.end_exp.get() == '':
            self.end_exp.insert(0, PLACEHOLDER_TEXT[1])
            self.end_exp.config(foreground=BUTTON_COLOR)



#for testing
GUI()


