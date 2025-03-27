# setup.py
import tkinter as tk
from tkinter import ttk
import os
from datetime import datetime

def load_match_info():
    """Loads match information from match_info.txt."""
    try:
        with open("match_info.txt", "r") as f:
            lines = f.readlines()
            match_info = {}
            for line in lines:
                key, value = line.strip().split(": ", 1)
                match_info[key] = value
            return match_info
    except FileNotFoundError:
        return None

def load_player_data():
    """Loads player data from player_data.txt."""
    try:
        with open("player_data.txt", "r") as f:
            lines = f.readlines()
            player_data = {"home_players": [], "away_players": [], "home_subs": [], "away_subs": []}
            current_section = None
            for line in lines:
                line = line.strip()
                if line == "Home Team Players:":
                    current_section = "home_players"
                elif line == "Away Team Players:":
                    current_section = "away_players"
                elif line == "Home Team Substitutes:":
                    current_section = "home_subs"
                elif line == "Away Team Substitutes:":
                    current_section = "away_subs"
                elif line:
                    name, number = line.split(",")
                    player_data[current_section].append({"name": name, "number": number})
            return player_data
    except FileNotFoundError:
        return None

def goal_scored(team_name, team_color):
    """Handles goal scoring."""
    goal_time = goal_time_entry.get()
    scorer_name = scorer_dropdown.get()

    try:
        datetime.strptime(goal_time, "%M:%S") #validate goal time.
    except ValueError:
        error_label.config(text = "Invalid Time format (MM:SS)")
        return

    result_text.insert(tk.END, f"{goal_time} - Goal for {team_name} by {scorer_name}\n")
    save_result(f"{goal_time} - Goal for {team_name} by {scorer_name}\n")

def cancel_goal():
    """Cancels the last goal."""
    lines = result_text.get(1.0, tk.END).splitlines()
    if lines:
        last_goal = lines[-1] + "\n"
        result_text.delete(f"end - {len(last_goal)}c", tk.END)
        remove_last_goal_from_file()

def save_result(goal_text):
    """Saves the result to a file."""
    try:
        with open(f"{match_info['home_team']}_vs_{match_info['away_team']}.txt", "a") as f:
            f.write(goal_text)
    except Exception as e:
        print(f"Error saving result: {e}")

def remove_last_goal_from_file():
    """Removes the last goal from the result file."""
    try:
        filename = f"{match_info['home_team']}_vs_{match_info['away_team']}.txt"
        with open(filename, "r") as f:
            lines = f.readlines()
        if lines:
            with open(filename, "w") as f:
                f.writelines(lines[:-1])
    except Exception as e:
        print(f"Error removing last goal: {e}")

def end_game():
    """Ends the game and displays the winner."""
    lines = result_text.get(1.0, tk.END).splitlines()
    home_goals = 0
    away_goals = 0
    for line in lines:
        if "Goal for " + match_info['home_team'] in line:
            home_goals += 1
        elif "Goal for " + match_info['away_team'] in line:
            away_goals += 1

    winner = ""
    if home_goals > away_goals:
        winner = match_info['home_team']
    elif away_goals > home_goals:
        winner = match_info['away_team']
    else:
        winner = "Draw"

    result_text.insert(tk.END, f"\nGame Ended. Winner: {winner}\n")
    save_result(f"\nGame Ended. Winner: {winner}\n")
    setup_root.title(f"{match_info['home_team']}_vs_{match_info['away_team']} - Winner: {winner}")

# Load match and player data
match_info = load_match_info()
player_data = load_player_data()

if not match_info or not player_data:
    print("Error: Could not load match or player data.")
    exit()

setup_root = tk.Tk()
setup_root.title("Match Setup")

# Team Names
team_names_label = tk.Label(setup_root, text=f"{match_info['home_team']} vs {match_info['away_team']}")
team_names_label.pack(pady=10)

# Goal Buttons
home_goal_button = tk.Button(setup_root, text=f"Goal for {match_info['home_team']}", command=lambda: goal_scored(match_info['home_team'], match_info['home_color']), bg=match_info['home_color'])
home_goal_button.pack(pady=5)

away_goal_button = tk.Button(setup_root, text=f"Goal for {match_info['away_team']}", command=lambda: goal_scored(match_info['away_team'], match_info['away_color']), bg=match_info['away_color'])
away_goal_button.pack(pady=5)

# Goal Time and Scorer
goal_time_label = tk.Label(setup_root, text="Goal Time (MM:SS):")
goal_time_label.pack()
goal_time_entry = tk.Entry(setup_root)
goal_time_entry.pack()

scorer_label = tk.Label(setup_root, text="Goal Scorer:")
scorer_label.pack()

all_players = player_data["home_players"] + player_data["away_players"] + player_data["home_subs"] + player_data["away_subs"]
scorer_names = [player["name"] for player in all_players]

scorer_dropdown = ttk.Combobox(setup_root, values=scorer_names)
scorer_dropdown.pack()

# Cancel Goal Button
cancel_goal_button = tk.Button(setup_root, text="Cancel Last Goal", command=cancel_goal)
cancel_goal_button.pack(pady=5)

# Result Text Area
result_label = tk.Label(setup_root, text="Match Results:")
result_label.pack()
result_text = tk.Text(setup_root, height=10, width=50)
result_text.pack()

error_label = tk.Label(setup_root, text="", fg="red")
error_label.pack()

# End Game Button
end_game_button = tk.Button(setup_root, text="End Game", command=end_game)
end_game_button.pack(pady=10)

# Initial file creation
try:
    with open(f"{match_info['home_team']}_vs_{match_info['away_team']}.txt", "w") as f:
        f.write(f"Home Team: {match_info['home_team']}\n")
        f.write(f"Away Team: {match_info['away_team']}\n")
        f.write(f"Date: {match_info['date']}\n")
        f.write(f"Time: {match_info['time']}\n")
        f.write(f"Home Color: {match_info['home_color']}\n")
        f.write(f"Away Color: {match_info['away_color']}\n")
        f.write(f"\nHome Team Players:\n")
        for player in player_data["home_players"]:
            f.write(f"{player['name']},{player['number']}\n")
        f.write(f"\nAway Team Players:\n")
        for player in player_data["away_players"]:
            f.write(f"{player['name']},{player['number']}\n")
        f.write(f"\nHome Team Substitutes:\n")
        for player in player_data["home_subs"]:
            f.write(f"{player['name']},{player['number']}\n")
        f.write(f"\nAway Team Substitutes:\n")
        for player in player_data["away_subs"]:
            f.write(f"{player['name']},{player['number']}\n")
        f.write("\nMatch Events:\n")
except Exception as e:
    print(f"Error creating initial result file: {e}") #error message

setup_root.mainloop()

