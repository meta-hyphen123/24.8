from colorama import init, Fore, Back

import os
import datetime

init(autoreset=True)
def get_prompt(username, hostname, working_dir, shiter_path):
    cwd = working_dir.replace(shiter_path, "")
    
    segment_user = f"{Back.BLUE}{Fore.WHITE} {username}@{hostname} "
    segment_cwd = f"{Back.YELLOW}{Fore.BLACK}~{cwd} "
    
    arrow_fill_cwd = f"{Back.YELLOW}{Fore.BLUE}{Back.RESET}"
    arrow_fill_branch = f"{Back.RESET}{Fore.YELLOW}"

    prompt = (
        f"{segment_user}{arrow_fill_cwd}"
        f"{segment_cwd}"
        f"{arrow_fill_branch}"
        f"{Fore.RESET}"
    )
    return prompt