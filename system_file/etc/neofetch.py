import platform
import os
import subprocess
import psutil
from datetime import timedelta
from rich.console import Console
from rich.color import Color
from rich.style import Style
from rich.text import Text

console = Console()

def get_uptime():
    boot_time = psutil.boot_time()
    now = psutil.time.time()
    uptime_seconds = now - boot_time
    uptime_string = str(timedelta(seconds=int(uptime_seconds)))
    return uptime_string

def get_packages():
    try:
        pass
    except:
        return "N/A"

def get_shell():
    return os.environ.get('COMSPEC', 'N/A')

def get_resolution():
    try:
        import ctypes
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        return f"{screensize[0]}x{screensize[1]}"
    except:
        return "N/A"

def get_cpu_info():
    try:
        return platform.processor()
    except:
        return "N/A"

def get_memory_info():
    memory = psutil.virtual_memory()
    return f"{memory.used // (1024 ** 2)}MB/{memory.total // (1024 ** 2)}MB"

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return f"{disk.percent}%"

def get_system_info():
    os_info = f"{platform.system()} {platform.release()}"
    kernel_info = platform.version()
    uptime_info = get_uptime()
    packages_info = get_packages()
    shell_info = get_shell()
    resolution_info = get_resolution()
    cpu_info = get_cpu_info()
    memory_info = get_memory_info()
    disk_info = get_disk_usage()

    info = [
    ]
    return "\n".join(info)

def generate_gradient_colors(colors, steps_per_segment):
    gradient = []
    for i in range(len(colors) - 1):
        start_color = Color.parse(colors[i]).get_truecolor()
        end_color = Color.parse(colors[i + 1]).get_truecolor()
        for j in range(steps_per_segment):
            red = int(start_color[0] + (end_color[0] - start_color[0]) * j / (steps_per_segment - 1))
            green = int(start_color[1] + (end_color[1] - start_color[1]) * j / (steps_per_segment - 1))
            blue = int(start_color[2] + (end_color[2] - start_color[2]) * j / (steps_per_segment - 1))
            gradient.append(Style(color=Color.from_rgb(red, green, blue)))
    return gradient

def display_info():
    # Get system information
    os_info = f"{platform.system()} {platform.release()}"
    kernel_info = platform.version()
    uptime_info = get_uptime()
    packages_info = get_packages()
    shell_info = get_shell()
    resolution_info = get_resolution()
    cpu_info = get_cpu_info()
    memory_info = get_memory_info()
    disk_info = get_disk_usage()

    # Gradient colors and steps
    colors = ["#FF0000", "#FFA500", "#FFFF00", "#008000", "#00FFFF", "#0000FF", "#800080"]
    steps_per_segment = 10
    gradient_height = 5

    # Generate gradient colors
    gradient_colors = generate_gradient_colors(colors, steps_per_segment)

    # Display ASCII art logo with gradient colors
    logo = f"""
                 FFFFFFFFFFFFFFFFFFFFFFF                   OS: {os_info}
             ZWWFCFCFCFCFCFCFCFCFCFCFCF                    Kernel: {kernel_info}
             ICCFCFFFFFFFFFFFFFFCFCFCFC                    Uptime: {uptime_info}
          TCFCFCFCI            FCFCFCFC                    Packages: {packages_info}
          TCFCFCFCI            FCFCFCFC                    Shell: {shell_info}
          TCFCFCFFI            FCFCFW                      Resolution: {resolution_info}
          TFCFCFCCI            FCFII                       CPU: {cpu_info}
          TCFCFCFCI            FF                          Memory: {memory_info}
          TFCFCFCFI                                        Disk Usage: {disk_info}
          TCFCFCFCI
          TCFCFCFCI
    TCCFCCFCFCFCFCFCCFCCFCCFCCFCCFCCFCC
       TFCFCFCFCFCFCFCFCFCFCFCFCFCFCFCF
                               FCFCFCFC
                               FCFCFCFF                 ████████████████████████████████████████████████████████████
                               FCFCFCFC                 ████████████████████████████████████████████████████████████
                FCI            FCFCFCFC                 ████████████████████████████████████████████████████████████
             TNNFFI            FCFCFCFC
             NFCCFI            FCFCFILL
          TCFCFCFCCCCFCCFCCFCCFCFCFFC
       TCCFCFCFCFFFFCFCFCFCCFCFCFCF
"""

    logo_lines = logo.splitlines()
    gradient_logo_lines = []
    for i, line in enumerate(logo_lines):
        gradient_line = Text()
        for j, char in enumerate(line):
            color_index = (i + j) % len(gradient_colors)
            gradient_line.append(char, style=gradient_colors[color_index])
        gradient_logo_lines.append(gradient_line)

    for line in gradient_logo_lines:
        console.print(line)

    # Display system info
    system_info = get_system_info()
    system_info_lines = system_info.splitlines()
    for line in system_info_lines:
        print(line)



if __name__ == "__main__":
    display_info()
