import os
from datetime import datetime, timedelta

# Path setup
base_path = os.path.dirname(os.path.abspath(__file__))
commit_folder = os.path.join(base_path, "fake-code")
os.makedirs(commit_folder, exist_ok=True)

# Start from a Sunday so GitHub grid lines up
start_date = datetime(2024, 1, 7)

# Tic Tac Toe pattern (3x3 grid)
pattern = [
    "XOX",  # row 0
    "OXO",  # row 1
    "XOX"   # row 2
]

commits_per_cell = 20

# Loop through the 3x3 grid
for row in range(len(pattern)):
    for col in range(len(pattern[row])):
        if pattern[row][col] == 'X':
            # Each grid cell is 1 day (col) + 7-day step (row)
            day_offset = col + (row * 7)
            commit_date = start_date + timedelta(days=day_offset)

            for n in range(commits_per_cell):
                file_path = os.path.join(commit_folder, "dummy.txt")
                with open(file_path, "a") as f:
                    f.write(f"Commit {n+1} at {commit_date}\n")

                os.chdir(base_path)
                os.system("git add .")
                os.system(f'git commit --date="{commit_date.isoformat()}" -m "Tic Tac Toe move on {commit_date.date()}"')
