from colorama import*
import os
import datetime
import platform
def clear():
    import platform
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
    else:
        pass
clear()
print("welcome to shiter DNS-Shell")
init(autoreset=True)
def get_prompt( working_dir, shiter_path):
    cwd = working_dir.replace(shiter_path, "")
    
    segment_user = f"{Back.BLACK}{Fore.YELLOW}🗲  dns-shell@shiter"
    segment_cwd = f"{Back.BLUE}{Fore.BLACK}~{cwd} "
    
    arrow_fill_cwd = f"{Back.BLUE}{Fore.BLACK}{Back.RESET}"
    arrow_fill_branch = f"{Back.RESET}{Fore.BLUE}"

    prompt = (
        f"{segment_user}{arrow_fill_cwd}"
        f"{segment_cwd}"
        f"{arrow_fill_branch}"
        f"{Fore.RESET}"
    )
    return prompt

prompt = get_prompt("","")
while True:
    command = input(prompt)
    if command == 'exit':
        print()
        break
    if not command:
        continue
    else:
        shiter_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(shiter_path)
        os.system(f"python3 DNS-Shell.py {command}")