file_path = "C:/users.txt"


def remove_duplicates(file_name):
    unique_lines = set()

    with open(file_name, 'r') as file:
        for line in file:
            unique_lines.add(line)

    with open(file_name, 'w') as file:
        file.writelines(unique_lines)

    print("Duplicate lines successfully removed.")


remove_duplicates(file_path)