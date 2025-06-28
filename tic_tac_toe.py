import os
from datetime import datetime, timedelta

# Base path = your repo folder
base_path = os.path.dirname(os.path.abspath(__file__))
commit_folder = os.path.join(base_path, "fake-code")
os.makedirs(commit_folder, exist_ok=True)

# 🗓️ Start from a recent Sunday to center the RB
start_date = datetime(2025, 6, 29)  # adjust as needed

# 🟩 RB pattern — 'X' will become green squares
pattern = [
    "XXX  XXX ",
    "X  X X  X",
    "XXX  XXX ",
    "X R  X  X",
    "X  X XXX "
]

commits_per_cell = 30  # darker green

# Loop through each cell
for row in range(len(pattern)):
    for col in range(len(pattern[row])):
        if pattern[row][col] == "X":
            day_offset = col + row * 7
            commit_date = start_date + timedelta(days=day_offset)

            for n in range(commits_per_cell):
                file_path = os.path.join(commit_folder, "rb.txt")
                with open(file_path, "a") as f:
                    f.write(f"Commit {n+1} at {commit_date}\n")

                os.chdir(base_path)
                os.system("git add .")
                os.system(f'git commit --date="{commit_date.isoformat()}" -m "RB pattern commit on {commit_date.date()}"')
