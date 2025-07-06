import os
from datetime import datetime, timedelta

# Get the base repo path (ROHANBAIJU)
base_path = os.path.dirname(os.path.abspath(__file__))

# Ensure 'fake-code' exists inside your repo
commit_folder = os.path.join(base_path, "fake-code")
os.makedirs(commit_folder, exist_ok=True)

# ✅ Set a recent Sunday (adjustable)
# Today is 2025-07-29, so let's start from 2025-06-29 (Sunday)
start_date = datetime(2025, 6, 29)

# Tic Tac Toe pattern with a gap around (5x5 grid)
pattern = [
    "     ",
    " XOX ",
    " OXO ",
    " XOX ",
    "     "
]

# Strong green = more commits
commits_per_cell = 40

for row in range(len(pattern)):
    for col in range(len(pattern[row])):
        if pattern[row][col] == 'X':
            # 1 week = 7 days row offset
            day_offset = row * 7 + col
            commit_date = start_date + timedelta(days=day_offset)

            for n in range(commits_per_cell):
                file_path = os.path.join(commit_folder, "dummy.txt")
                with open(file_path, "a") as f:
                    f.write(f"Commit {n+1} at {commit_date}\n")

                os.chdir(base_path)
                os.system("git add .")
                os.system(f'git commit --date="{commit_date.isoformat()}" -m "Enhanced Tic Tac Toe {commit_date.date()}"')
