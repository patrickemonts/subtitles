import tkinter as tk
import sys

# Create the main window
root = tk.Tk()

# Make the window full screen
# root.attributes('-fullscreen', True)

# Make the window transparent
# root.attributes('-alpha', 0.0)
root.configure(bg='black')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{int(screen_height/4)}+0+{3*screen_height//4}")
root.focus_force()

root.wm_attributes('-type','dock')

# List of strings to display
with open('subtitles.txt', 'r') as f:
    stringvec = f.readlines()

stringvec = [x.strip() for x in stringvec if len(x.strip()) > 0]
#print(stringvec)

# Create a label with the initial text "Foobar" in black
label = tk.Label(root, text="", font=("Helvetica", 30), fg="white", bg="black")
i = 0

# Function to change the text of the label
# def force_focus(event):
#     global root
#     root.focus_force()

def incr_text(event):
    global root
    root.focus_force()

    global i
    if i < len(stringvec) - 1:
        i += 1
    label.config(text=stringvec[i])
    # scale_font(event)

def decr_text(event):
    global i
    if i < len(stringvec) - 1:
        i -= 1
    label.config(text=stringvec[i])
    # scale_font(event)

def quit(event):
    sys.exit(0)


# Function to scale the font size based on window size
def scale_font(event):
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    font_size = min(window_width // 20, window_height // 10)
    label.config(font=("Helvetica", font_size))

# Bind the function to the label's click event
label.bind("<Button-1>", incr_text)
root.bind("<Button-1>", incr_text)
root.bind("<Right>", incr_text)
label.bind("<Right>", incr_text)
root.bind("<Left>",decr_text)
label.bind("<Left>",decr_text)
root.bind("q",quit)
label.bind("q",quit)



# Bind the scaling function to the window resize event
# root.bind("<Configure>", scale_font)

# Center the label in the window
label.pack(expand=True)

# Run the main loop
root.mainloop()