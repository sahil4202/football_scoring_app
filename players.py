# players.py
import tkinter as tk
import subprocess
import sys
import os

def save_players_and_start():
    """Saves player data and starts setup.py."""
    home_players = []
    away_players = []
    home_subs = []
    away_subs = []

    for i in range(11):
        home_name = home_name_entries[i].get()
        home_number = home_number_entries[i].get()
        away_name = away_name_entries[i].get()
        away_number = away_number_entries[i].get()

        home_players.append({"name": home_name, "number": home_number})
        away_players.append({"name": away_name, "number": away_number})

    for i in range(7):
        home_sub_name = home_sub_name_entries[i].get()
        home_sub_number = home_sub_number_entries[i].get()
        away_sub_name = away_sub_name_entries[i].get()
        away_sub_number = away_sub_number_entries[i].get()

        home_subs.append({"name": home_sub_name, "number": home_sub_number})
        away_subs.append({"name": away_sub_name, "number": away_sub_number})

    # Save player data (example: to a file)
    with open("player_data.txt", "w") as f:
        f.write("Home Team Players:\n")
        for player in home_players:
            f.write(f"{player['name']},{player['number']}\n")
        f.write("\nAway Team Players:\n")
        for player in away_players:
            f.write(f"{player['name']},{player['number']}\n")
        f.write("\nHome Team Substitutes:\n")
        for sub in home_subs:
            f.write(f"{sub['name']},{sub['number']}\n")
        f.write("\nAway Team Substitutes:\n")
        for sub in away_subs:
            f.write(f"{sub['name']},{sub['number']}\n")

    # Start setup.py
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        setup_path = os.path.join(script_dir, "setup.py")

        if not os.path.exists(setup_path):
            print(f"Error: setup.py not found at {setup_path}")
            return

        subprocess.Popen([sys.executable, setup_path])
        players_root.destroy()

    except Exception as e:
        print(f"An error occurred: {e}")

players_root = tk.Tk()
players_root.title("Enter Player Information")

# Home Team Labels and Entry Widgets
tk.Label(players_root, text="Home Team Players").grid(row=0, column=0, columnspan=2)
home_name_entries = []
home_number_entries = []

for i in range(11):
    tk.Label(players_root, text=f"Player {i+1} Name:").grid(row=i + 1, column=0, sticky="w")
    name_entry = tk.Entry(players_root)
    name_entry.grid(row=i + 1, column=1)
    home_name_entries.append(name_entry)

    tk.Label(players_root, text="Shirt Number:").grid(row=i + 1, column=2, sticky="w")
    number_entry = tk.Entry(players_root)
    number_entry.grid(row=i + 1, column=3)
    home_number_entries.append(number_entry)

# Away Team Labels and Entry Widgets
tk.Label(players_root, text="Away Team Players").grid(row=0, column=4, columnspan=2)
away_name_entries = []
away_number_entries = []

for i in range(11):
    tk.Label(players_root, text=f"Player {i+1} Name:").grid(row=i + 1, column=4, sticky="w")
    name_entry = tk.Entry(players_root)
    name_entry.grid(row=i + 1, column=5)
    away_name_entries.append(name_entry)

    tk.Label(players_root, text="Shirt Number:").grid(row=i + 1, column=6, sticky="w")
    number_entry = tk.Entry(players_root)
    number_entry.grid(row=i + 1, column=7)
    away_number_entries.append(number_entry)

# Home Team Substitutes
tk.Label(players_root, text="Home Team Substitutes").grid(row=12, column=0, columnspan=2)
home_sub_name_entries = []
home_sub_number_entries = []

for i in range(7):
    tk.Label(players_root, text=f"Sub {i+1} Name:").grid(row=13 + i, column=0, sticky="w")
    name_entry = tk.Entry(players_root)
    name_entry.grid(row=13 + i, column=1)
    home_sub_name_entries.append(name_entry)

    tk.Label(players_root, text="Shirt Number:").grid(row=13 + i, column=2, sticky="w")
    number_entry = tk.Entry(players_root)
    number_entry.grid(row=13 + i, column=3)
    home_sub_number_entries.append(number_entry)

# Away Team Substitutes
tk.Label(players_root, text="Away Team Substitutes").grid(row=12, column=4, columnspan=2)
away_sub_name_entries = []
away_sub_number_entries = []

for i in range(7):
    tk.Label(players_root, text=f"Sub {i+1} Name:").grid(row=13 + i, column=4, sticky="w")
    name_entry = tk.Entry(players_root)
    name_entry.grid(row=13 + i, column=5)
    away_sub_name_entries.append(name_entry)

    tk.Label(players_root, text="Shirt Number:").grid(row=13 + i, column=6, sticky="w")
    number_entry = tk.Entry(players_root)
    number_entry.grid(row=13 + i, column=7)
    away_sub_number_entries.append(number_entry)

start_game_button = tk.Button(players_root, text="Start Game", command=save_players_and_start)
start_game_button.grid(row=20, column=3, pady=20)

players_root.mainloop()