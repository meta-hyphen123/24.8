import curses
import os
import sys

def main(stdscr, filename):
    curses.curs_set(1)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.clear()

    # Set up the window
    sh, sw = stdscr.getmaxyx()
    edit_win = curses.newwin(sh-3, sw, 1, 0)
    top_bar = curses.newwin(1, sw, 0, 0)
    bottom_bar = curses.newwin(2, sw, sh-2, 0)

    # Read file content if filename is provided
    if filename and os.path.isfile(filename):
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.read().splitlines()
    else:
        lines = ['']
    cursor_x = 0
    cursor_y = 0

    # Key mappings
    key_map = {
        27: 'ESC',  # Escape key
        10: 'ENTER',  # Enter key
        127: 'BACKSPACE',  # Backspace key on Linux
        curses.KEY_BACKSPACE: 'BACKSPACE',  # Backspace key on Windows
        8: 'BACKSPACE',  # Backspace key on some terminals
        330: 'DELETE',  # Delete key
        19: 'SAVE',  # Ctrl+S for save
        24: 'EXIT',  # Ctrl+X for exit
        curses.KEY_UP: 'UP',       # Arrow key up
        curses.KEY_DOWN: 'DOWN',   # Arrow key down
        curses.KEY_LEFT: 'LEFT',   # Arrow key left
        curses.KEY_RIGHT: 'RIGHT'  # Arrow key right
    }

    def draw_window():
        edit_win.clear()
        for i, line in enumerate(lines):
            try:
                edit_win.addstr(i, 0, line)
            except curses.error as e:
                # Print the problematic line
                print(f"Error adding line {i}: {e}")
        edit_win.move(cursor_y, cursor_x)
        edit_win.refresh()

    def draw_top_bar():
        top_bar.clear()
        top_bar.bkgd(' ', curses.color_pair(1))
        title = f"GNU nano 5.7    {filename if filename else 'New Buffer'}"
        top_bar.addstr(0, 0, title[:sw-1], curses.color_pair(1))
        top_bar.refresh()

    def draw_bottom_bar():
        bottom_bar.clear()
        bottom_bar.bkgd(' ', curses.color_pair(2))
        shortcuts = [
            "^G", "Help", "^O", "Write Out", "^W", "Where Is", "^K", "Cut", "^T", "Execute", "^C", "Location",
            "^X", "Exit", "^R", "Read File", "^\\", "Replace", "^U", "Paste", "^J", "Justify", "^W", "Write File"
        ]
        x_offset = 0
        for i, text in enumerate(shortcuts):
            if i % 2 == 0:
                if x_offset + len(text) < sw:
                    bottom_bar.addstr(i // 12, x_offset, text, curses.color_pair(1))
                x_offset += len(text) + 1
            else:
                if x_offset + len(text) < sw:
                    bottom_bar.addstr(i // 12, x_offset, text, curses.color_pair(2))
                x_offset += len(text) + 2
            if x_offset >= sw:
                x_offset = 0
        bottom_bar.refresh()

    def handle_key(key):
        nonlocal cursor_x, cursor_y, lines

        if key in key_map:
            if key_map[key] == 'ESC':
                return False
            elif key_map[key] == 'ENTER':
                lines.insert(cursor_y + 1, '')
                cursor_y += 1
                cursor_x = 0
            elif key_map[key] == 'BACKSPACE':
                if cursor_x > 0:
                    lines[cursor_y] = lines[cursor_y][:cursor_x-1] + lines[cursor_y][cursor_x:]
                    cursor_x -= 1
                elif cursor_y > 0:
                    cursor_x = len(lines[cursor_y - 1])
                    lines[cursor_y - 1] += lines.pop(cursor_y)
                    cursor_y -= 1
            elif key_map[key] == 'DELETE':
                if cursor_x < len(lines[cursor_y]):
                    lines[cursor_y] = lines[cursor_y][:cursor_x] + lines[cursor_y][cursor_x+1:]
            elif key_map[key] == 'SAVE':
                save_file()
            elif key_map[key] == 'EXIT':
                return False
            elif key_map[key] == 'UP':
                if cursor_y > 0:
                    cursor_y -= 1
            elif key_map[key] == 'DOWN':
                if cursor_y < len(lines) - 1:
                    cursor_y += 1
            elif key_map[key] == 'LEFT':
                if cursor_x > 0:
                    cursor_x -= 1
            elif key_map[key] == 'RIGHT':
                if cursor_x < len(lines[cursor_y]):
                    cursor_x += 1
        else:
            lines[cursor_y] = lines[cursor_y][:cursor_x] + chr(key) + lines[cursor_y][cursor_x:]
            cursor_x += 1

        if cursor_x > len(lines[cursor_y]):
            cursor_x = len(lines[cursor_y])

        if cursor_x < 0:
            cursor_x = 0

        if cursor_y >= len(lines):
            cursor_y = len(lines) - 1

        if cursor_y < 0:
            cursor_y = 0

        return True

    def save_file():
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))

    while True:
        draw_window()
        draw_top_bar()
        draw_bottom_bar()
        key = stdscr.getch()
        if not handle_key(key):
            break

if __name__ == "__main__":
    if len(sys.argv) < 2:
        filename = None
    else:
        filename = sys.argv[1]

    curses.wrapper(main, filename)
