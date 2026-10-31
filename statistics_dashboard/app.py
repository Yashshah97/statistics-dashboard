"""
Main application entry point.

This module sets up the curses window and starts the main loop.
"""

import argparse
from statistics_dashboard import __version__
from statistics_dashboard.dashboard import Dashboard
from statistics_dashboard.panel import PanelManager

def main():
    """
    Parse command-line arguments and start the dashboard.
    """
    parser = argparse.ArgumentParser(description='Statistics TUI Dashboard')
    parser.add_argument('--version', action='version',
                        version=__version__)
    args = parser.parse_args()

    # Set up the curses window
    import curses
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    try:
        # Create and run the dashboard
        panel_manager = PanelManager(stdscr)
        dashboard = Dashboard(panel_manager)
        dashboard.run()
    finally:
        # Clean up the curses window on exit
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()

if __name__ == '__main__':
    main()
