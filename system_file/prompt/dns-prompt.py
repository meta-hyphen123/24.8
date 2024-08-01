from colorama import*
import os
import datetime

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
