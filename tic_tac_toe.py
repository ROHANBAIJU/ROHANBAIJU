import os
from datetime import datetime, timedelta

# ✅ This is the folder where dummy commits will happen (visible in GitHub Desktop)
commit_folder = "fake-code"
os.makedirs(commit_folder, exist_ok=True)

# ✅ Make sure we stay in the correct working directory
start_path = os.getcwd()

# Start date on a Sunday (aligns with GitHub graph)
start_date = datetime(2024, 1, 7)

# Tic Tac Toe pattern: X marks the cell where commits should happen
pattern = [
    "XOX",
    "OXO",
    "XOX"
]

commits_per_cell = 20  # more = darker green on GitHub graph

# Loop through each cell
for row in range(len(pattern)):
    for col in range(len(pattern[row])):
        if pattern[row][col] == 'X':
            day_offset = row * 7 + col
            commit_date = start_date + timedelta(days=day_offset)
            for n in range(commits_per_cell):
                file_path = os.path.join(commit_folder, "dummy.txt")
                with open(file_path, "a") as f:
                    f.write(f"Commit {n+1} at {commit_date}\n")
                os.system("git add .")
                os.system(f'git commit --date="{commit_date.isoformat()}" -m "Tic Tac Toe move on {commit_date.date()}"')
