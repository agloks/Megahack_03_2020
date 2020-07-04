from importlib.machinery import SourceFileLoader
import os

file_directory = os.path.realpath(__file__)
file_directory_splited = file_directory.split("/")
root_folder = "/".join(file_directory_splited[:-3])
# print(file_directory)

ENV = SourceFileLoader("ENV", f"{root_folder}/settings_env.py").load_module()
handlerJson = SourceFileLoader("handlerJson", f"{root_folder}/src/utility/handlerJson.py").load_module()
geocoding = SourceFileLoader("handlerJson", f"{root_folder}/src/maps/geocoding.py").load_module()