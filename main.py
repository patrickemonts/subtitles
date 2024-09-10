import tkinter as tk
import sys
import os

# We are using global variables here, not recommended, but we are not writing a library here
label = None
stringvec = None
root = None
i = 0
is_mode_auto = True
delay = None

def incr_text(event):
    """
    Increases the text displayed on a label widget by one position in the stringvec list.
    Parameters:
        - event: The event that triggers the function.
    Returns:
        None
    """
    global root, i, is_mode_auto
    # This is not a very nice function to call, but it works
    root.focus_force()

    if i < len(stringvec) - 1:
        i += 1
        text = stringvec[i]
        if stringvec[i] == "## START ##":
            is_mode_auto = True
            auto_update_label()
        else:
            if text == "## END ##":
                is_mode_auto = False
                text = ""
            elif text == "## START ##":
                text = ""
            label.config(text=text)
    # scale_font(event)


def decr_text(event):
    """
    Decreases the index `i` and updates the text displayed in the label widget.
    Parameters:
    - event: The event that triggered the function.
    Returns:
    None
    """

    global root, i, is_mode_auto
    # This is not a very nice function to call, but it works
    is_mode_auto = False
    root.focus_force()
    if i >= 1:
        i -= 1
        if stringvec[i] == "## START ##" or stringvec[i] == "## END ##":
            text = ""
        else:
            text=stringvec[i]
    else:
        i = 0
        text=""
    label.config(text=text)
    # scale_font(event)

def auto_update_label():
    global i, is_mode_auto, delay
    if i < len(stringvec):
        i += 1
        if stringvec[i] != "## END ##" and is_mode_auto:
            label.config(text=stringvec[i])
            root.after(delay*1000, auto_update_label)  # Schedule the next update in 5 seconds
        else:
            is_mode_auto = False
            label.config(text="")


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

def main(args):
    # Create the main window
    global root, label, stringvec, i, delay
    delay = args.delay
    fname = args.fname
    display_fraction = args.fraction
    if os.path.exists(fname):
        root = tk.Tk()

        # Make the window full screen
        # root.attributes('-fullscreen', True)

        # Make the window transparent
        # root.attributes('-alpha', 0.0)
        root.configure(bg="black")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        display_height = int(screen_height * display_fraction)
        display_width = screen_width
        offset_x = 0
        offset_y = int((1-display_fraction)*screen_height)

        root.geometry(f"{display_width}x{display_height}+{offset_x}+{offset_y}")
        root.focus_force()

        root.wm_attributes("-type", "dock")

        # List of strings to display
        with open(args.fname, "r") as f:
            stringvec = f.readlines()

        # stringvec = [x.strip() for x in stringvec if len(x.strip()) > 0]
        stringvec = [x.strip() for x in stringvec] 
        stringvec = [x.replace('\\n','\n') for x in stringvec]
        # We start on black
        stringvec.insert(0,"")

        # Create a label with the initial text "Foobar" in black
        label = tk.Label(root, text="", font=("Roboto", 40), fg="white", bg="black", anchor=tk.CENTER, width = display_width)
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
    else:
        print(f"File {args.fname} not found.",file=sys.stderr)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Display subtitles on the screen.")
    parser.add_argument(
        "fname", type=str, help="The name of the file containing the subtitles."
    )
    parser.add_argument(
        "--fraction", type=float, default=0.25, help="Fraction of the screen height to use."
    )
    parser.add_argument(
        "--delay", type=float, default=5, help="Delay in seconds for the automatic scrolling."
    )
    args = parser.parse_args()
    main(args)
