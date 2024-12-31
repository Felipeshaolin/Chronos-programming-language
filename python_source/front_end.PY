
import tkinter as tk
from tkinter import filedialog

def start():
    """just a basic message to start the program"""


    #an iconic little bird :) Rest in peace chronos i will forever miss you
    print("      " + "\x1b[5;30;43m" + "\\\\" + "\x1b[0m" + "\n      " + "\x1b[5;30;43m"+ "(o" + "\x1b[0m" + "\x1b[5;30;43m" + ">" + "\x1b[0m"+ "\n   " + "\x1b[1;30;47m" + "\\\\" + "\x1b[0m" + "\x1b[1;30;47m" + "_" + "//)" + "\x1b[0m" + "\n    "+ "\x1b[1;30;47m" + "\\_/_)" + "\x1b[0m" + "\n     " + "\x1b[1;30;47m" + "_|_)" + "\x1b[0m")
    print("  ___| |__  _ __ ___  _ __   ___  ___")
    print(" / __| '_ \\| '__/ _ \\| '_ \\ / _ \\/ __|")
    print("| (__| | | | | | (_) | | | | (_) \\__ \\")
    print(" \\___|_| |_|_|  \\___/|_| |_|\\___/|___/")

    print("welcome to the chronos interpreter")
    print("select a file")


def file_prompt():

    """a funtion tht opens the file explorer to find the file you want it returns h ( the size in bytes of the memory) and file_path (the file path of the file chosen)"""

    # Create a root Tkinter window (it won't be shown)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open file dialog to choose a file
    file_path = filedialog.askopenfilename(title="Select a file")

    # Check if the user selected a file
    if file_path:
        print(f"Selected file: {file_path}")
        h = int(input("enter the size of memory in bytes:\n"))
        return file_path,h

    else:
        print("No file selected.")
