import tkinter as tk
from tkinter import ttk

def delay_btn():
    print("button hit!")
    return

root = tk.Tk()
root.title('Squat Alert!')

# set windowsize
window_width = 250
window_height = 50

# get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# place a label on the root window
message = tk.Label(root, text="Drop and give me 10 Squats!")
message.pack()

# set position
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# buttons
delay_btn = ttk.Button(
    root,
    text="Delay 30s",
    command=delay_btn
)

delay_btn.pack(
    ipadx=5,
    ipady=5,
    expand=True
    )

# keep the window displaying and put atop all other windows
root.attributes('-topmost', 1)
root.iconbitmap('./assets/dumbbell.ico')
root.mainloop()