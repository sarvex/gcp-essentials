"""make a file that iterates """


import os

with open("output.txt", "w") as text_file:
    path = f"{os.getcwd()}/data"

    list_of_files = list(os.listdir(path))

    for file_in_dir in list_of_files:
        text_file.write(f"{path}{file_in_dir} 5:10\n")