import os
import datetime
import sys

# DIRECTORY = r"C:\Users\Lenovo\OneDrive\Рабочий стол\it\python\projects\files-renamer\test"


def get_valid_name(file_name, folder_name):
    current_date = datetime.date.today().strftime("%d-%m-%Y")
    name, extension = os.path.splitext(file_name)

    valid_name = f"{folder_name}_{name}_{current_date}{extension}"
    return valid_name


def rename_file(root, file_name):
    folder_name = os.path.basename(root)
    valid_name = get_valid_name(file_name, folder_name)
    old_file = os.path.join(root, file_name)
    new_file = os.path.join(root, valid_name)

    os.rename(old_file, new_file)


def rename_files(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            rename_file(root, file_name)


def main():
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    DIRECTORY = script_dir
    rename_files(DIRECTORY)


if __name__ == "__main__":
    main()
