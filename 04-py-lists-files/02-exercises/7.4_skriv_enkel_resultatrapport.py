from pathlib import  Path

scores_list = [100, 50, 90, 75, 68]

score_report_path = Path("..") / "data" / "score_report.txt"

with open(score_report_path, "w", encoding="utf-8") as file:
    file.write(f"Count: {len(scores_list)}\n")
    file.write(f"Total: {sum(scores_list)}\n")
    file.write(f"Average: {(sum(scores_list) / len(scores_list)):.2f}\n")
    file.write(f"Lowest: {min(scores_list)}\n")
    file.write(f"Highest: {max(scores_list)}\n")
