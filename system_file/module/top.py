import curses
import psutil
from curses import wrapper

class ProcessMonitor:
    def __init__(self, num_processes=10):
        self.num_processes = num_processes

    def init_colors(self, stdscr):
        # 初始化颜色对
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # 背景白色，前景黑色

    def get_process_info(self):
        processes = []
        for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                processes.append({
                    'PID': process.info['pid'],
                    'Name': process.info['name'],
                    'CPU %': process.info['cpu_percent'],
                    'Memory %': process.info['memory_percent']
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        return processes

    def display_processes(self, stdscr, processes):
        self.init_colors(stdscr)  # 初始化颜色
        curses.curs_set(0)  # 隐藏光标
        stdscr.nodelay(True)  # 非阻塞输入
        stdscr.clear()  # 清空屏幕

        # 打印表头
        header = "PID    Name                 CPU %   Memory %"
        stdscr.addstr(0, 0, header, curses.A_BOLD | curses.color_pair(1))

        # 打印进程信息
        sorted_processes = sorted(processes, key=lambda x: x['CPU %'], reverse=True)[:self.num_processes]
        for idx, process in enumerate(sorted_processes, start=2):
            line = "{:<6} {:<20} {:<7.2f} {:<10.2f}".format(
                process['PID'], process['Name'], process['CPU %'], process['Memory %'])
            stdscr.addstr(idx, 0, line)

        stdscr.refresh()  # 刷新屏幕显示更新

    def run(self, stdscr):
        while True:
            processes = self.get_process_info()
            self.display_processes(stdscr, processes)
            key = stdscr.getch()
            if key == ord('q'):
                break

def main(stdscr):
    monitor = ProcessMonitor()
    monitor.run(stdscr)

if __name__ == "__main__":
    wrapper(main)