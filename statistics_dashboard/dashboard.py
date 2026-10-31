import curses
from typing import Dict, List

class Dashboard:
    def __init__(self):
        self.panels = {}

    def add_panel(self, name: str) -> None:
        """Add a new panel to the dashboard."""
        self.panels[name] = {'y': 0, 'x': 0}

    def update_panel(self, name: str, height: int = 1, width: int = 20) -> None:
        """Update the size of an existing panel."""
        if name in self.panels:
            self.panels[name]['height'] = height
            self.panels[name]['width'] = width

    def render(self, stdscr: curses.window) -> None:
        """Render the dashboard to a curses window."""
        for i, (name, panel) in enumerate(self.panels.items()):
            y, x = panel['y'], panel['x']
            height, width = panel.get('height', 1), panel.get('width', 20)
            stdscr.addstr(y, x, f"Panel {name} ({i+1})")
            for j in range(height):
                stdscr.addstr(y + j, x, '-' * width)

def main(stdscr: curses.window) -> None:
    """Main function to run the dashboard."""
    dash = Dashboard()
    dash.add_panel('panel1')
    dash.update_panel('panel2', height=5)
    dash.render(stdscr)
    stdscr.refresh()

if __name__ == '__main__':
    curses.wrapper(main)
