# ============================================
# Maxwell-Dice Roller (Persistent Counter)
# ============================================

import sys
import os

COUNTER_FILE = "maxwell_counter.txt"
M = 100

# Cumulative MB tables
P9 = [0.040, 0.183, 0.423, 0.663, 0.835,
      0.931, 0.975, 0.992, 1.000]

P12 = [0.020, 0.070, 0.160, 0.290, 0.450,
       0.620, 0.780, 0.890, 0.950,
       0.980, 0.995, 1.000]


def load_counter():
    """Load persistent counter from file."""
    if not os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "w") as f:
            f.write("1")
        return 1
    with open(COUNTER_FILE, "r") as f:
        return int(f.read().strip())


def save_counter(n):
    """Save persistent counter to file."""
    with open(COUNTER_FILE, "w") as f:
        f.write(str(n))


def maxwell_random_value():
    """Generate pseudo-random x using persistent counter."""
    n = load_counter()
    x = ((n % M) + 1) / M
    save_counter(n + 1)
    return x


def maxwell_roll(table):
    """General MB roll function."""
    x = maxwell_random_value()
    for i, threshold in enumerate(table, start=1):
        if x <= threshold:
            return i
    return len(table)


def maxwell_roll_d9():
    return maxwell_roll(P9)


def maxwell_roll_d12():
    return maxwell_roll(P12)


# ============================================
# Command-line interface
# ============================================

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: py maxwell.py rolld9 | rolld12")
        sys.exit(0)

    cmd = sys.argv[1].lower()

    if cmd == "rolld9":
        print(maxwell_roll_d9())
    elif cmd == "rolld12":
        print(maxwell_roll_d12())
    else:
        print("Unknown command. Use rolld9 or rolld12.")
