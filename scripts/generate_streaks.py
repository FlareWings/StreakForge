# scripts/generate_streaks.py

import os
from datetime import datetime, timedelta

def get_log_dates(user_folder):
    dates = []
    for fname in os.listdir(user_folder):
        if not fname.endswith('.md'):
            continue
        try:
            dt = datetime.strptime(fname[:-3], "%Y-%m-%d").date()
            dates.append(dt)
        except ValueError:
            continue
    return sorted(dates)

def calculate_current_streak(dates):
    streak = 0
    today = datetime.today().date()
    for i, day in enumerate(reversed(dates)):
        if day == today - timedelta(days=i):
            streak += 1
        else:
            break
    return streak

def calculate_longest_streak(dates):
    if not dates:
        return 0
    longest = current = 1
    for prev, curr in zip(dates, dates[1:]):
        if curr == prev + timedelta(days=1):
            current += 1
        else:
            longest = max(longest, current)
            current = 1
    return max(longest, current)
