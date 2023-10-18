import os
import datetime
import sys
import re


def get_valid_name(file_name, folder_name):
    current_date = datetime.date.today().strftime("%d-%m-%Y")
    name, extension = os.path.splitext(file_name)

    date_pattern = r"\d{2}-\d{2}-\d{4}"
    match = re.match(date_pattern, file_name)

    if match:
        valid_name = file_name
    else:
        valid_name = f"{current_date}_{folder_name}_{name}{extension}"

    return valid_name


def rename_file(root, file_name, script_name):
    folder_name = os.path.basename(root)

    if file_name != script_name:
        valid_name = get_valid_name(file_name, folder_name)
        old_file = os.path.join(root, file_name)
        new_file = os.path.join(root, valid_name)

        os.rename(old_file, new_file)


def rename_files(directory, script_name):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            rename_file(root, file_name, script_name)


def main():
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    script_name = os.path.basename(sys.argv[0])
    DIRECTORY = script_dir
    # DIRECTORY = r"C:\Users\Lenovo\OneDrive\Рабочий стол\it\python\projects\files-renamer\test"
    rename_files(DIRECTORY, script_name)


if __name__ == "__main__":
    main()
