# scripts/calculate_totals.py

import os

def count_logs(user_folder):
    return len([f for f in os.listdir(user_folder) if f.endswith('.md')])

def main():
    base = 'logs'
    for user in os.listdir(base):
        user_path = os.path.join(base, user)
        if not os.path.isdir(user_path):
            continue
        total = count_logs(user_path)
        print(f"✅ {user}: {total} problems solved")

if __name__ == "__main__":
    main()
