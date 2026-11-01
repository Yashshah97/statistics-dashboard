"""Demo for Statistics Tui Dashboard."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import statistics_dashboard

print("Statistics Tui Dashboard", "v" + statistics_dashboard.__version__)
print("modules:", [m for m in dir(statistics_dashboard) if not m.startswith('_')])
