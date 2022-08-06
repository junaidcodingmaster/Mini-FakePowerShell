import os
import shutil

source = os.getcwd()
destination = "c:\FakePowerShell"

print("\nInstalling required modules ...\n")

os.system("pip install -r requirements.txt")

print("\nFake-PowerShell moving to FakePowerShell\nLocation ->", destination, "\n")

if os.path.isdir(destination) == True:
    pass
elif os.path.isdir(destination) == False:
    print("Creating Folder ->", destination, "\n")
    os.mkdir(destination)
else:
    pass

print("Removing Trash from project ...\n")

ls = os.listdir(source)
removeUnwanted = ["requirements.txt", "README.md", "install.py", "img"]

for i in range(0, 4):
    print("Removing unwanted files ->", removeUnwanted[i])
    ls.remove(removeUnwanted[i])

if os.path.isdir("__pycache__") == True:
    ls.remove("__pycache__")
else:
    pass

print("\nMoving files ...\n")

for i in range(0, len(ls)):
    print("Moving ->", shutil.copy(ls[i], destination))
