import tkinter as tk
import subprocess
import sys
import os

def start_info():
    """Opens info.py in a new process and closes the current window."""
    try:
        # Construct the full path to info.py, handling potential issues with relative paths.
        script_dir = os.path.dirname(os.path.abspath(__file__))
        info_path = os.path.join(script_dir, "info.py")  # Ensure info.py is in the same directory.

        if not os.path.exists(info_path):
            print(f"Error: info.py not found at {info_path}")
            return

        # Use subprocess.Popen to avoid blocking the main tkinter thread.
        subprocess.Popen([sys.executable, info_path]) # use the same python interpreter.

        root.destroy()  # Close the main window after launching info.py.

    except Exception as e:
        print(f"An error occurred: {e}")

root = tk.Tk()
root.title("Start Info")

start_button = tk.Button(root, text="Start", command=start_info)
start_button.pack(pady=20)

root.mainloop()