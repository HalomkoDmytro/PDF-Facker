import os
import subprocess, sys

def remove_before_last_slash(path):
    last_slash_index = path.rfind('/')
    if last_slash_index != -1:
        return path[last_slash_index + 1:]
    return path


def remove_dimension(name):
    last_slash_index = name.rfind('.')
    if last_slash_index != -1:
        return name[:last_slash_index]
    return name


def get_file_paths_with_extension(folder_path, extension):
    file_paths = []
    for file in os.listdir(folder_path):
        if file.endswith(extension):
            full_path = os.path.join(folder_path, file)
            file_paths.append(full_path)
    return file_paths


def delete_all_files_in_folder(folder_path):
    print(f"Delete all files in {folder_path}")
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)


def delete_all_files_in_folder_with_extension(folder_path, extension):
    print(f"Delete all files in {folder_path} with extension {extension}")
    for file_name in os.listdir(folder_path):
        if file_name.endswith(extension):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)


def open_folder(folder_path="destination"):
    if folder_path:
        if sys.platform.startswith('win'):
            os.startfile(folder_path)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, folder_path])
