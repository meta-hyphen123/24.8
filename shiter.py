import os
import time
import subprocess
import sys
import platform
import threading
import requests
import glob
import colorama
from colorama import Fore, Back
from system_file.prompt.prompt import *
import os

# 假设 tools.py 模块定义了所有的工具及其相关命令
import system_file.etc.hack.tools




prompt_functions = {}
def write_to_text_file(file_path, text):
    try:
        with open(file_path, 'w') as file:
            file.write(text)
    except FileNotFoundError:
        print("File not found!")

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print("File not found!")
        return None
colorama.init(autoreset=True)

# Define colors
red = '\033[91m'
yellow = '\033[93m'
blue = '\033[94m'
green = '\033[92m'  
orange = '\033[33m'
purple = '\033[95m'
pink = '\033[95m'
white = '\033[37m'

# Determine script path
shiter_path = os.path.dirname(os.path.abspath(__file__))
system_file = os.path.join(shiter_path, 'system_file')
etc = os.path.join(system_file, 'etc')
module = os.path.join(system_file, 'module')
hack = os.path.join(etc, 'hack')
pip = os.path.join(etc, 'pip')
wget = os.path.join(etc, 'wget')
nano = os.path.join(etc, 'nano')
user = os.path.join(shiter_path, 'user')
exploits = os.path.join(module,"exploits")
scanqli = os.path.join(module,"ScanQLi")
shitertool = os.path.join(module,"shitertool")
INSTALLTOOL = os.path.join(hack,"installed_tools.txt")
# Set working directory
working_dir = os.getcwd()

def execute_run_command(tool_name):
    tool_classes = {getattr(cls, 'TITLE', '').lower(): cls for cls in tools.__dict__.values() if isinstance(cls, type)}
    tool_class = tool_classes.get(tool_name.lower())

    if tool_class and is_tool_installed(tool_name):
        commands = tool_class.RUN_COMMANDS
        for command in commands:
            print(f"Executing run command: {command}")
            os.system(command)
    else:
        print(f"The tool '{tool_name}' is not installed or not found. Please install it first.")

def is_tool_installed(tool_name):
    # 读取已安装工具的列表
    if os.path.exists(INSTALLTOOL):
        with open(INSTALLTOOL, 'r') as f:
            installed_tools = f.read().splitlines()
        return tool_name.lower() in (tool.lower() for tool in installed_tools)
    return False

def detect_suspicious_activity():
    while True:
        time.sleep(5)

def disconnect_network():
    try:
        subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "admin=disabled"], check=True)
        print("")
    except subprocess.CalledProcessError as e:
        print(f"Error disconnecting network: {e}")

# Start a background thread to detect suspicious activity
detect_thread = threading.Thread(target=detect_suspicious_activity)
detect_thread.daemon = True  
detect_thread.start()

def print_working_directory():
    try:
        return os.getcwd()
    except Exception as e:
        return str(e)

def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f}{unit}"
        size /= 1024

def get_last_write_time(path):
    # Get the last write time of a file/folder
    time_obj = time.gmtime(os.path.getmtime(path))
    return time.strftime('%m/%d/%Y %I:%M %p', time_obj)

def list_directory(path="."):
    # Get the directory contents
    pathB = path.replace(shiter_path, "")
    try:
        entries = os.listdir(path)
    except PermissionError:
        print(f"{red}Error: You do not have the necessary permissions to access '{path}'.{white}")
        return

    # Print the header
    print(f"Directory: {pathB}")
    print(f"""{yellow}
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----{white}""")
    # Iterate over the directory contents
    for entry in entries:
        full_path = os.path.join(path, entry)
        mode = ""
        if os.path.isdir(full_path):
            mode = "d----"
            color = yellow
        elif os.path.isfile(full_path):
            mode = "-a---"
            color = white
        if os.access(full_path, os.R_OK):
            mode = mode[:1] + "r" + mode[2:]
        if os.access(full_path, os.W_OK):
            mode = mode[:2] + "w" + mode[3:]
        if os.access(full_path, os.X_OK):
            mode = mode[:3] + "x" + mode[4:]

        last_write_time = get_last_write_time(full_path)
        size = format_size(os.path.getsize(full_path)) if os.path.isfile(full_path) else ""
        print(f"{color}{mode}  {last_write_time}  {size:>10}  {entry}{white}")

def etb(A):
    B = os.path.join(etc, A)
    os.chdir(B)

def run(command):
    os.system(command)

def clear():
    import platform
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
    else:
        pass

def typewriter(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def replace_wormgpt(answer):
    if "WORMGPT" in answer:
        answer = answer.replace("WORMGPT", "ShiterGPT")
    return answer

def display_response(answer):
    if answer is not None:
        typewriter(answer, 0.001)
    else:
        print("No answer available.")

api_url = "https://worker-quiet-haze-bf7d.apinepdev.workers.dev/"

def ask_question(question):
    response = requests.get(f"{api_url}?question={question}&state=omega")

    if response.status_code == 200:
        json_response = response.json()
        answer = json_response.get("answer")
        if answer:
            updated_answer = replace_wormgpt(answer)
            display_response(updated_answer)
        else:
            print("No answer available in the response.")
    else:
        print("Failed to get a response. Status code:", response.status_code)

def change_directory(target_name):
    global working_dir
    pattern = os.path.join(working_dir, target_name + '*')

    matches = glob.glob(pattern)
    if matches:
        new_dir = matches[0]
        if os.path.isdir(new_dir):
            os.chdir(new_dir)
            working_dir = os.getcwd()
        else:
            print(f"Error: {new_dir} is not a directory")
    else:
        print(f"No matching directory for: {target_name}")

def cd(folder):
    os.chdir(folder)
def sure():
    should_pip = "yes"
    should_run = "yse"
def main():
    should_pip = "no"
    should_run = "no"
    global working_dir
    global shiter_path

    # Initial directory setup
    os.chdir(user)
    working_dir = os.getcwd()
    os.chdir(system_file)
    
    username = "shiter"
    hostname = "shiter"
    prompt = get_prompt(username, hostname, working_dir, shiter_path)
    
    try:
        while True:

            user_input=input(prompt).strip()
            if not user_input:
                continue


            elif user_input.startswith('shit '):
                sure()
                cd(hack)
                hack_command = user_input[5:]
                run(f"python hack.dll {hack_command}")


            elif user_input.startswith('sqlmap'):
                cd(module)
                should_run = 'yes'
                cd("sqlmap")
                if user_input == 'sqlmap':
                    run("python3 sqlmap.py --wizard")
                else:
                    sqlmap_command = user_input[7:]
                    run(f'python3 sqlmap.py {sqlmap_command}')

            elif user_input.startswith('MHDDoS'):
                cd(module)
                cd("MHDDoS")
                should_run = 'yes'
                if user_input == 'MHDDoS':
                    run("python3 start.py -h")
                else:
                    mhddos_command = user_input[7:]
                    run(f'python3 start.py {mhddos_command}')

            elif user_input == 'top':
                cd(module)
                run("python3 top.py")

            elif user_input.startswith("pip"):
                sure()
                should_pip = 'yes'
                cd(pip)
                pip_command = user_input[4:]
                run(f"python pip_config.txt {pip_command}")
            elif user_input.startswith("wget"):
                sure()
                cd(wget)
                wget_command = user_input[5:]
                run(f"python wgat.dll {wget_command}")
            elif user_input == 'neofetch':
                cd(etc)
                run("python3 neofetch.py")
                should_run = 'yes'
                should_pip = 'yes'
            elif user_input.lower() == 'dns-shell':
                cd(module)
                run("python3 dnshell.py")
            elif user_input.startswith('dns-shell '):
                dnsshellcommand = user_input[8:]
                cd(module)
                run(f'python3 DNS-Shell.py {dnsshellcommand}')
            elif user_input == 'shiter tool':
                cd(shitertool)
                run("python3 shitertool.dll")
            elif user_input.startswith("scanqli"):
                cd(scanqli)
                run("python3 scanqli.py")
            elif user_input.startswith("nano"):
                should_run = 'yes'
                should_pip = 'yes'
                cd(nano)
                path = user_input[5:].strip()
                if path.startswith("/"):
                    full_path = os.path.join(shiter_path, path[1:])
                    full_path = os.path.normpath(full_path)
                elif path[1:3] == ':\\':
                    full_path = os.path.normpath(path)
                else:
                    full_path = os.path.join(working_dir, path)
                    full_path = os.path.normpath(full_path)
                
                # Add quotes
                full_path_with_quotes = f'"{full_path}"'
                
                run(f"python3 nano.py {full_path_with_quotes}")
                clear()        
            elif user_input == 'exploits':
                cd(etc)
                cd(exploits)
                run("python3 shiter-exploit.py")
            elif '@shitergpt' in user_input.lower():
                sure()
                q = user_input[11:]
                ask_question(q)
            elif user_input.lower() == 'dir':
                sure()
                
                list_directory(working_dir)
            elif 'rm' in user_input.lower():
                sure()
                cd(etc)
                B = user_input[3:]
                if shiter_path in user_input:
                    run(f'python3 rm.dll {B}')
                elif cwd in user_input:
                    rm_command = os.path.join(shiter_path, B)          
                    run(f'python3 rm.dll {rm_command}')
                else:
                    C = os.path.join(shiter_path, cwd, B)
                    run(f'python3 rm.dll {C}')
            elif user_input == 'telnet':
                cd(module)
                run("python3 apt.py")
            elif user_input.lower() == 'cd':
                os.chdir(shiter_path)
                os.chdir("user")
                working_dir = os.getcwd()
                cwd = working_dir.replace(shiter_path, "")
                prompt = get_prompt(username, hostname, working_dir, shiter_path)
            elif user_input.startswith("cd "):
                target_dir = user_input[3:].strip()
                change_directory(target_dir)
                current_dir = os.path.basename(working_dir)
                prompt = get_prompt(username, hostname, current_dir, shiter_path)
            elif user_input.lower() == "exit":
                exit()
            elif user_input.lower() == 'cl':
                sure()
                clear()           
            elif user_input.startswith('python'):
                sure()
                os.chdir(working_dir)
                run(user_input)
            elif './' in user_input.lower():
                sure()
                run(user_input)
            elif 'git clone' in user_input.lower():
                sure()
                run(user_input)
            else:
                if should_run == 'yes':
                    pass
                elif should_pip == 'yes':
                    pass
                else:

                    cd(hack)
                    os.system(f"python3 hack.dll run {user_input}")
                
    except KeyboardInterrupt:
        print(f"{Fore.RED}^C")
        main()

if __name__ == "__main__":
    commands = []
    os.chdir(shiter_path)
    if os.path.exists("system_file"):
        main()
    else:
        exit()
