# scripts/generate_badges.py

import os
from pathlib import Path
from generate_streaks import (
    get_log_dates,
    calculate_current_streak,
    calculate_longest_streak
)

def make_badge(label, value, color):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="170" height="20">
  <rect width="80" height="20" fill="#555"/>
  <rect x="80" width="90" height="20" fill="{color}"/>
  <text x="10" y="14" fill="#fff" font-family="Verdana" font-size="11">{label}</text>
  <text x="90" y="14" fill="#fff" font-family="Verdana" font-size="11">{value}</text>
</svg>'''

def main():
    badge_dir = Path("badges")
    badge_dir.mkdir(exist_ok=True)

    for user in os.listdir("logs"):
        folder = os.path.join("logs", user)
        if not os.path.isdir(folder):
            continue

        dates = get_log_dates(folder)
        current = calculate_current_streak(dates)
        longest = calculate_longest_streak(dates)
        total   = len(dates)

        # Write badges
        (badge_dir / f"{user}_streak.svg").write_text(
            make_badge("Streak", f"{current} 🔥", "#e07b00")
        )
        (badge_dir / f"{user}_solved.svg").write_text(
            make_badge("Solved", f"{total} ✅", "#4caf50")
        )
        (badge_dir / f"{user}_longest.svg").write_text(
            make_badge("Longest", f"{longest} 🏆", "#1e90ff")
        )

        print(f"Updated badges for {user}: streak={current}, total={total}, longest={longest}")

if __name__ == "__main__":
    main()
