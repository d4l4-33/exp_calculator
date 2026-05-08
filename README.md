# EXP Calculator by d4l4-33

This is my first boot.dev personal project. My idea going into this was to make a generic exp/h application for grinding RPG-games that needed to be fed a starting percentage exp and by reading the system's clock it could estimate exp per hour when another percentage was put in. This could then be further developed to calculate gold/mesos/groschen/denari per hour by also recieving that information and finally if allowed get all that information automatically.

I started with making a TUI-based calculator and wanted to try my hand at a GUI so I started looking into GUI. Because of that this project has two diffrent modes with the same math. 
- *See Logbook.md for... well, I'll give you three guesses.*


### To copy the repository:

```
git clone https://github.com/d4l4-33/exp_calculator
cd exp_calculator
```

### For the TUI version:
```
./main_tui.sh
``` 

### For the GUI version:

```
./main_gui.sh
```

#### Shortcuts in the GUI:
- Escape: Close the calculator
- Return: Submit
- Ctrl + Return: Clear
- Tab: Jump between fields