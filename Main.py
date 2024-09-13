import os
import sys
import pathlib
import zipfile
def Main():
    gamefolder = input("Please Write FOLDER to Extract DXVK: ")
    if not pathlib.Path(os.getcwd() + "\\dxvkzipfiles"):
        print("Failed to Find DXVK Folder")
        os._exit(112)
    else:
        with zipfile.ZipFile(file="{}".format(os.getcwd() + "\\dxvkzipfiles\\dxvk_x64_dx11.zip")) as zipf_dx11:
            zipf_dx11.extractall(path=gamefolder)
            exit(3321)

if __name__ == "__main__":
    Main()