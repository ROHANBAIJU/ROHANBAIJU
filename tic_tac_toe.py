import os
from datetime import datetime, timedelta

# Start date must be a Sunday
start_date = datetime(2024, 1, 7)

# Tic Tac Toe pattern
pattern = [
    "XOX",
    "OXO",
    "XOX"
]

# Number of commits per cell
commits_per_cell = 20

os.makedirs("fake-code", exist_ok=True)
os.chdir("fake-code")
os.system("git init")

with open("game.txt", "a") as f:
    for row in range(len(pattern)):
        for col in range(len(pattern[row])):
            if pattern[row][col] == 'X':
                offset = row * 7 + col
                commit_date = start_date + timedelta(days=offset)
                for _ in range(commits_per_cell):
                    f.write(f"Commit at {commit_date}\n")
                    os.system("git add .")
                    os.system(f'git commit --date="{commit_date.isoformat()}" -m "Tic Tac Toe move"')
