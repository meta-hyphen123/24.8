import time
from tqdm import tqdm

# Function to create a loading bar
def loading_bar(duration):
    # Define the number of iterations (you can adjust this to change the speed)
    iterations = 100

    # Create a tqdm progress bar
    with tqdm(total=iterations, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}", ncols=60) as pbar:
        for _ in range(iterations):
            time.sleep(duration / iterations)
            pbar.update(1)

# Call the loading_bar function with a duration of 5 seconds
loading_bar(5)
