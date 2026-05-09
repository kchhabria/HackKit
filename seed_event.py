#!/usr/bin/env python3
"""
Seed script: Pre-loads judges and categories for a new event.
Run this once before event day to set up the scoring app.

Usage:
    python seed_event.py

Edit the JUDGES and CATEGORIES lists below for your event.
"""

import db

# --- CUSTOMIZE THESE FOR YOUR EVENT ---

JUDGES = [
    "Judge 1",
    "Judge 2",
    "Judge 3",
    "Judge 4",
]

CATEGORIES = [
    ("Business Impact / Industry Alignment", 0.40),
    ("Technical Excellence", 0.40),
    ("Innovation", 0.20),
]

TEAMS = [
    # Add team names here on event day, or use the app UI
    # "Team Alpha",
    # "Team Beta",
]

# --- DO NOT EDIT BELOW THIS LINE ---

def main():
    print("Seeding HackKit database...")
    print()

    # Add judges
    existing_judges = [j["name"] for j in db.get_judges()]
    for name in JUDGES:
        if name not in existing_judges:
            db.add_judge(name)
            print(f"  Added judge: {name}")
        else:
            print(f"  Judge already exists: {name}")

    # Add categories
    existing_cats = [c["name"] for c in db.get_categories()]
    for name, weight in CATEGORIES:
        if name not in existing_cats:
            db.add_category(name, weight)
            print(f"  Added category: {name} ({int(weight*100)}%)")
        else:
            print(f"  Category already exists: {name}")

    # Add teams
    if TEAMS:
        existing_teams = [t["name"] for t in db.get_teams()]
        for name in TEAMS:
            if name not in existing_teams:
                db.add_team(name)
                print(f"  Added team: {name}")
            else:
                print(f"  Team already exists: {name}")

    print()
    print("Done! Run 'streamlit run app.py' to start the scoring app.")

if __name__ == "__main__":
    main()
