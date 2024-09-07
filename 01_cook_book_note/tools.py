import os


def get_file_path_for_dataset(filename: str):
    return os.path.join(os.path.dirname(__file__), "data_set", filename)


file_path = get_file_path_for_dataset("somefile.txt")
print(os.path.exists(file_path))
