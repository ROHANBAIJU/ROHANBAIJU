import os
from datetime import datetime, timedelta

# ✅ Get the path of the current script (which is inside ROHANBAIJU/)
base_path = os.path.dirname(os.path.abspath(__file__))

# ✅ Make sure fake-code folder is created INSIDE ROHANBAIJU/
commit_folder = os.path.join(base_path, "fake-code")
os.makedirs(commit_folder, exist_ok=True)

# ✅ Use start date that begins on a Sunday
start_date = datetime(2024, 1, 7)

# Tic Tac Toe pattern (3x3)
pattern = [
    "XOX",
    "OXO",
    "XOX"
]

commits_per_cell = 20

# Loop through each cell
for row in range(len(pattern)):
    for col in range(len(pattern[row])):
        if pattern[row][col] == 'X':
            offset = row * 7 + col
            commit_date = start_date + timedelta(days=offset)

            for commit_number in range(commits_per_cell):
                file_path = os.path.join(commit_folder, "dummy.txt")
                with open(file_path, "a") as f:
                    f.write(f"Commit {commit_number + 1} at {commit_date}\n")

                # ✅ Run git commands inside the ROHANBAIJU Git repo
                os.chdir(base_path)
                os.system("git add .")
                os.system(f'git commit --date="{commit_date.isoformat()}" -m "Tic Tac Toe move on {commit_date.date()}"')
