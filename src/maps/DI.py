from importlib.machinery import SourceFileLoader
import os

file_directory = os.path.realpath(__file__)
file_directory_splited = file_directory.split("/")
root_folder = "/".join(file_directory_splited[:-3])
print(file_directory)


ENV = SourceFileLoader("ENV", f"{root_folder}/settings_env.py").load_module()