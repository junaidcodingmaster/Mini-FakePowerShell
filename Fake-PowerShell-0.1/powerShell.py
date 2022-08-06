from commands import Commands, os

os.system("cls")

print(
    "Windows PowerShell\nCopyright (C) Microsoft Corporation. All rights reserved.\n\nTry the new cross-platform PowerShell https://aka.ms/pscore6\n"
)

cwd = os.getcwd()
path = "PS " + cwd + "> "


Commands.transCommand(path=path, run=True)
