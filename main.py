import tkinter as tk
import sys

def incr_text(event):
    """
    Increases the text displayed on a label widget by one position in the stringvec list.
    Parameters:
        - event: The event that triggers the function.
    Returns:
        None
    """
    global root, i
    # This is not a very nice function to call, but it works
    root.focus_force()

    if i < len(stringvec) - 1:
        i += 1
    label.config(text=stringvec[i])
    # scale_font(event)


def decr_text(event):
    """
    Decreases the index `i` and updates the text displayed in the label widget.
    Parameters:
    - event: The event that triggered the function.
    Returns:
    None
    """

    global root, i
    # This is not a very nice function to call, but it works
    root.focus_force()
    if i < len(stringvec) - 1:
        i -= 1
    label.config(text=stringvec[i])
    # scale_font(event)


def quit(event):
    """Exit the program.

    Args:
        event: The event that triggered the function.
    """
    sys.exit(0)


# Function to scale the font size based on window size
def scale_font(event):
    """Scale the font size based on the window size.

    Args:
        event: The event that triggreed the function.
    """
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    font_size = min(window_width // 20, window_height // 10)
    label.config(font=("Helvetica", font_size))

# Create the main window
root = tk.Tk()

# Make the window full screen
# root.attributes('-fullscreen', True)

# Make the window transparent
# root.attributes('-alpha', 0.0)
root.configure(bg="black")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{int(screen_height/4)}+0+{3*screen_height//4}")
root.focus_force()

root.wm_attributes("-type", "dock")

# List of strings to display
with open("subtitles.txt", "r") as f:
    stringvec = f.readlines()

stringvec = [x.strip() for x in stringvec if len(x.strip()) > 0]
# print(stringvec)

# Create a label with the initial text "Foobar" in black
label = tk.Label(root, text="", font=("Helvetica", 30), fg="white", bg="black")
i = 0


# Bind the different events to the functions
label.bind("<Button-1>", incr_text)
root.bind("<Button-1>", incr_text)
root.bind("<Right>", incr_text)
label.bind("<Right>", incr_text)
root.bind("<Left>", decr_text)
label.bind("<Left>", decr_text)
root.bind("q", quit)
label.bind("q", quit)


# Bind the scaling function to the window resize event
# root.bind("<Configure>", scale_font)

# Center the label in the window
label.pack(expand=True)

# Run the main loop
root.mainloop()