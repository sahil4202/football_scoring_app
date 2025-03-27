# info.py
import tkinter as tk
from tkinter import ttk
import subprocess
import sys
import os
from datetime import datetime

def validate_date(date_str):
    """Validates the date format (dd-mm-yyyy)."""
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def validate_time(time_str):
    """Validates the time format (hh:mm AM/PM)."""
    try:
        datetime.strptime(time_str, "%I:%M %p")
        return True
    except ValueError:
        return False

def next_to_players():
    """Validates inputs and navigates to players.py."""
    home_team = home_team_entry.get()
    away_team = away_team_entry.get()
    home_color = home_color_entry.get()
    away_color = away_color_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    stadium = stadium_entry.get()

    if not validate_date(date):
        error_label.config(text="Invalid date format (dd-mm-yyyy)")
        return
    if not validate_time(time):
        error_label.config(text="Invalid time format (hh:mm AM/PM)")
        return

    # Store data in a dictionary or file (for setup.py to access)
    match_info = {
        "home_team": home_team,
        "away_team": away_team,
        "home_color": home_color,
        "away_color": away_color,
        "date": date,
        "time": time,
        "stadium": stadium,
    }

    # Example: Save to a file (you can modify this part)
    with open("match_info.txt", "w") as f:
        for key, value in match_info.items():
            f.write(f"{key}: {value}\n")

    # Navigate to players.py
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        players_path = os.path.join(script_dir, "players.py")

        if not os.path.exists(players_path):
            print(f"Error: players.py not found at {players_path}")
            return

        subprocess.Popen([sys.executable, players_path])
        info_root.destroy()

    except Exception as e:
        print(f"An error occurred: {e}")

info_root = tk.Tk()
info_root.title("Match Information")

# Labels and Entry Widgets
tk.Label(info_root, text="Home Team:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
home_team_entry = tk.Entry(info_root)
home_team_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(info_root, text="Away Team:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
away_team_entry = tk.Entry(info_root)
away_team_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(info_root, text="Home Color:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
home_color_entry = tk.Entry(info_root)
home_color_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(info_root, text="Away Color:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
away_color_entry = tk.Entry(info_root)
away_color_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(info_root, text="Date (dd-mm-yyyy):").grid(row=4, column=0, sticky="w", padx=5, pady=5)
date_entry = tk.Entry(info_root)
date_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(info_root, text="Time (hh:mm AM/PM):").grid(row=5, column=0, sticky="w", padx=5, pady=5)
time_entry = tk.Entry(info_root)
time_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(info_root, text="Stadium:").grid(row=6, column=0, sticky="w", padx=5, pady=5)
stadium_entry = tk.Entry(info_root)
stadium_entry.grid(row=6, column=1, padx=5, pady=5)

next_button = tk.Button(info_root, text="Next", command=next_to_players)
next_button.grid(row=7, column=1, pady=10)

error_label = tk.Label(info_root, text="", fg="red")
error_label.grid(row=8, column=0, columnspan=2)

info_root.mainloop()