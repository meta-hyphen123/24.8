from colorama import init, Fore, Back
import os
import datetime
import inspect

init(autoreset=True)

# 定义 basic_prompt 函数
basic_prompt_code = """
def basic_prompt(username, hostname, working_dir, shiter_path):
    cwd = working_dir.replace(shiter_path, "")
    return f"{Back.BLACK}{Fore.WHITE} {username}@{hostname} {Back.WHITE}{Fore.BLACK}~{cwd} {Back.RESET}{Fore.RESET}$ "
"""

# 定义 classical_prompt 函数
classical_prompt_code = """
def classical_prompt(username, hostname, working_dir, shiter_path):
    return f"{Fore.CYAN}{username}@{hostname} {Fore.MAGENTA}{working_dir} {Fore.YELLOW}→{Fore.RESET} {Fore.GREEN}$ {Fore.RESET}"
"""

# 定义 get_prompt 函数
get_prompt_code = """
def get_prompt(username, hostname, working_dir, shiter_path):
    cwd = working_dir.replace(shiter_path, "")
    
    segment_user = f"{Back.BLUE}{Fore.BLACK} {username}@{hostname} "
    segment_cwd = f"{Back.YELLOW}{Fore.BLACK}~{cwd}"
    
    arrow_fill_cwd = f"{Back.YELLOW}{Fore.BLUE}{Back.RESET}"
    arrow_fill_branch = f"{Back.RESET}{Fore.YELLOW}"

    prompt = (
        f"{segment_user}{arrow_fill_cwd}"
        f"{segment_cwd}"
        f"{arrow_fill_branch}"
        f"{Fore.RESET}"
    )
    return prompt
"""

# 定义 simple_prompt 函数
simple_prompt_code = """
def simple_prompt(username, hostname, working_dir, shiter_path):
    return f"{username}@{hostname}:{working_dir}$ "
"""

# 定义 similar_prompt 函数
similar_prompt_code = """
def similar_prompt(username, hostname, working_dir, shiter_path):
    cwd = working_dir.replace(shiter_path, "")
    return f"{Back.BLACK}{Fore.WHITE} {username}@{hostname} {Back.WHITE}{Fore.BLACK} ~{cwd} {Back.RESET}{Fore.RESET}$ "
"""

# 定义 multiline_prompt 函数
multiline_prompt_code = """
def multiline_prompt(username, hostname, working_dir, shiter_path):
    cwd = working_dir.replace(shiter_path, "")
    return f"{Fore.BLUE}{username}@{hostname}\n{Fore.GREEN}{cwd}$ {Fore.RESET}"
"""

# 定义 similar_multiline_prompt 函数
similar_multiline_prompt_code = """
def similar_multiline_prompt(username, hostname, working_dir, shiter_path):
    cwd = working_dir.replace(shiter_path, "")
    return f"{Fore.BLUE}{username}@{hostname}\n{Fore.GREEN}{cwd}$ {Fore.RESET}"
"""

# 定义 special_char_prompt 函数
special_char_prompt_code = """
def special_char_prompt(username, hostname, working_dir, shiter_path):
    cwd = working_dir.replace(shiter_path, "")
    return f"{Fore.CYAN}{username}@{hostname} ▪ {Fore.MAGENTA}{cwd}$ {Fore.RESET}"
"""

# 定义 minimal_prompt 函数
minimal_prompt_code = """
def minimal_prompt(username, hostname, working_dir, shiter_path):
    cwd = working_dir.replace(shiter_path, "")
    return f"{username}@{hostname}:{cwd}$ "
"""

# 定义 color_cycle_prompt 函数
color_cycle_prompt_code = """
def color_cycle_prompt(username, hostname, working_dir, shiter_path):
    cwd = working_dir.replace(shiter_path, "")
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    return f"{colors[0]}{username}@{hostname}{colors[1]}:{colors[2]}{cwd}{colors[3]}$ {Fore.RESET}"
"""

# 定义 time_prompt 函数
time_prompt_code = """
def time_prompt(username, hostname, working_dir, shiter_path):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"{Fore.YELLOW}{current_time} {Fore.BLUE}{username}@{hostname}:{Fore.GREEN}{working_dir}$ {Fore.RESET}"
"""

# 将所有 prompt 函数代码存储到一个字典中
prompt_codes = {
    'basic': basic_prompt_code,
    'classical': classical_prompt_code,
    'get': get_prompt_code,
    'simple': simple_prompt_code,
    'similar': similar_prompt_code,
    'multiline': multiline_prompt_code,
    'similar_multiline': similar_multiline_prompt_code,
    'special_char': special_char_prompt_code,
    'minimal': minimal_prompt_code,
    'color_cycle': color_cycle_prompt_code,
    'time': time_prompt_code,
    # 添加其他的 prompt 函数代码...
}

def write_to_text_file(file_path, text):
    try:
        with open(file_path, 'w') as file:
            file.write(text)
    except FileNotFoundError:
        print("File not found!")

# 用户输入要写入的函数名
user_input = input("请输入要写入的函数名：")

# 检查函数是否存在，并写入对应的代码到文件
current_file_path = os.path.dirname(os.path.abspath(__file__))
text_file_path = os.path.join(current_file_path, 'prompt.py')
if user_input in prompt_codes:
    write_to_text_file
