import os
import random
import shutil
from time import sleep

import pandas as pd
from simple_chalk import chalk
from tqdm import tqdm


class Commands:
    devMode = dict()
    hackerMode = False

    def transCommand(run=bool, path=str):

        devMode = dict()
        o = True
        while run == True:
            try:
                com = input(path)
                o = True
            except KeyboardInterrupt:
                os.system("clear")
                Commands.transCommand(run=True, path=path)
                break
            else:
                pass

            if com == "ps maker":
                print(
                    "\nFakePowerShell , version - 2\nNew Addons -\nNode_modules remover - ps rm nm , __pycache__ remover - ps rm pyca\nThis PowerShell clone is Made By Junaid .\nThis is the clone of Windows Power Shell with fake hacking tools.\nFor more info. type 'ps info'\n"
                )
                o = False

            if com == "ps info":
                print(
                    "\nFakePowerShell , version - 2\nThis is the clone of Windows Power Shell with fake hacking tools.\nWhich is made by Junaid.\n"
                )
                print(
                    "\nNew Addons -\n1.Node_modules remover - 'ps rm nm' and\n2. __pycache__ remover - 'ps rm pyca' ."
                )
                print(
                    "\nFake Tools -> \n1.To see who is the user of the computer -> 'powerShell --user --name'\n2.'powerShell install coda' Fake malware installer",
                    "\n... \nFor more go to ",
                )
                o = False

            # developer Mode
            if com == "ps --dev":
                print("Create A developer account.")
                print("---" * 10)
                nam = input("Enter Your username -> ")
                ema = input("Enter Your e-mail -> ")
                devMode.update(devMode=True, devName=nam, devEmail=ema)
                for i in tqdm(
                    range(100), desc="Saving contacts...", ascii=False, ncols=75
                ):
                    pass

                print("\nYou have new terminal\n")
                print("For using dev commands , you want to use 'psdev' to run.")
                df = pd.DataFrame.from_dict(devMode, orient="index")
                df.to_csv("devMode.csv")
                o = False

            if com == "psdev userinfo":
                df = pd.read_csv("devMode.csv", index_col=0)
                devMode = df.to_dict("split")
                devMode = dict(zip(devMode["index"], devMode["data"]))
                print(devMode)
                o = False

            if com == "psdev update":
                os.system("C:/FakePowerShell/fakepowershell.bat")
                o = False

            if com == "ps hackermode":
                print("\nDo you want to on hacker Mode.\n")
                loo = input("(y or n) -> ")
                if loo == "y":
                    Commands.hackerCommand(path)
                    o = False
                else:
                    print("Ok! Bye!")
                    break

            if com == "psdev":
                if devMode.get("devMode") == True:
                    print("\npsdev : any properties not found.\n")
                elif devMode.get("devMode") == False:
                    print(
                        "\nYour are not in developer Mode.\nTo on it type -> 'ps --dev'\n"
                    )
                o = False

            if com == "ls":
                p = os.getcwd()
                print("\nFolder path ->", p)
                for x in os.listdir("."):
                    print("\n", "--->", x)
                print("\n")
                o = False

            if com == "ps rm nm":
                print("\nEnter Path below to delete 'Node_modules' folder .")
                print(
                    "\n",
                    chalk.yellow("NOTE : \n you want to give parent directory."),
                    "example -> /abc/ -> /Node_modules/ , /img/ , /e.c.t/ , app.js | [parent directory] is /abc/\n",
                )

                try:
                    oyo = input("Path -> ")
                except KeyboardInterrupt:
                    print(chalk.yellow("User Exited !"))
                    Commands.transCommand(run=True, path=path)
                except ValueError:
                    print(chalk.red("Invalid Value !"))
                    Commands.transCommand(run=True, path=path)
                else:
                    pass

                if os.path.isdir(oyo) == True:
                    pass
                else:
                    print(chalk.red("\nFolderNotFound: Given path was not exist.\n"))
                    os._exit(1)

                if os.path.isdir(oyo) == True:
                    pass
                else:
                    print(chalk.red("\nFolderNotFound: Given path was not exist.\n"))
                    os._exit(1)

                nm = oyo + "/node_modules"

                if os.path.isdir(nm) == True:
                    pass
                else:
                    print(
                        chalk.red(
                            "\nNodeModulesFolderNotFound: Given path was not have 'node_modules' folder .\n"
                        )
                    )
                    os._exit(1)

                shutil.rmtree(nm)
                print("\n", nm, "is deleted !\n")

                o = False

            if com == "ps rm pyca":
                print("\nEnter Path below to delete '__pycache__' folder .")
                print(
                    "\n",
                    chalk.yellow("NOTE : \n you want to give parent directory."),
                    "example -> /abc/ -> /__pycache__/ , /img/ , /e.c.t/ , app.py then [parent directory] is /abc/\n",
                )

                try:
                    oyo = input("Path -> ")
                except KeyboardInterrupt:
                    print(chalk.yellow("User Exited !"))
                    Commands.transCommand(run=True, path=path)
                except ValueError:
                    print(chalk.red("Invalid Value !"))
                    Commands.transCommand(run=True, path=path)
                else:
                    pass

                if os.path.isdir(oyo) == True:
                    pass
                else:
                    print(chalk.red("\nFolderNotFound: Given path was not exist.\n"))
                    os._exit(1)

                nm = oyo + "/__pycache__"

                if os.path.isdir(nm) == True:
                    pass
                else:
                    print(
                        chalk.red(
                            "\nPyCacheFolderNotFound: Given path was not have '__pycache__' folder .\n"
                        )
                    )
                    os._exit(1)

                shutil.rmtree(nm)
                print("\n", nm, "is deleted !\n")

                o = False

            if com == "exit":
                exit()
                break
            elif com == "exit()":
                exit()
                break
            else:
                pass

            if o == True:
                o = True
                os.system(com)

    def hackerCommand(path=str):
        hackerMode = True
        o = False
        npath = chalk.green("(Hacker) ") + path

        print("\nHacker Mode is ON !\n")

        while hackerMode == True:
            try:
                com = input(npath)
                o = True
            except KeyboardInterrupt:
                os.system("clear")
                exit(0)
            else:
                pass

            if com == "ls":
                p = os.getcwd()
                print("\nFolder path ->", p)
                for x in os.listdir("."):
                    print("\n", "--->", x)
                print("\n")
                o = False

            if com == "powershell --user --name":
                print("\nYour logged as guest.\n")
                o = False

            if com == "powershell install coda":
                print("\nInstall Coda ...")
                print("\nInstalling codaInstaller , codaSetup , coda.exe packages")
                for i in tqdm(range(100), desc="Installing codaInstaller..."):
                    sleep(0.1)
                    pass
                print("\nDone !")
                print("\nRemaining codaSetup , coda.exe packages")
                for i in tqdm(range(100), desc="Installing codaSetup..."):
                    sleep(0.1)
                    pass
                for i in tqdm(range(100), desc="Installing coda.exe..."):
                    sleep(0.1)
                    pass
                print("Loading setup.exe ...")
                for i in tqdm(range(100), desc="Loading setup.exe..."):
                    sleep(0.1)
                    pass
                print("\nSetup and install is successfully done !")
                o = False

            if com == "terminalHacker --all":
                print("\nUser ->", os.getlogin())
                print("Current User active -> Guest")
                o = False

            if com == "terminalHacker --getUser_access":
                print("\ncomputer -> access Denied !")
                print(
                    "terminalHacker -> We recommend you to use\n'terminalHacker --bute_force --getUser_access' to get access."
                )
                o = False

            if com == "terminalHacker --bute_force --getUser_access":
                print("\nBute Forcing User...")
                for i in tqdm(range(100), desc="Bute Forcing..."):
                    sleep(0.5)
                    pass
                print("computer -> access Denied !\n" * 5)
                for i in tqdm(range(100), desc="Bute Forcing..."):
                    sleep(1)
                    pass
                print("\ncomputer -> access confirmed\n")
                print(
                    "\nYour are user now ->\nyou can hack his bank account -> 'terminalHacker --bank'\nyou can hack his one or may bank accounts -> 'terminalHacker --bank --access(1)'\n...\nfor more go to help.md"
                )
                o = False

            if com == "terminalHacker --bank":
                print("\nSearching browsing history to find out his bank website ...")
                for i in tqdm(range(100), desc="Searching... "):
                    sleep(0.1)
                print("\nBank account found !")
                o = False

            if com == "terminalHacker --bank --access(1)":
                print("\nTyping Bank account Number")
                for i in tqdm(range(100), desc="Typing... ", ascii=False, ncols=75):
                    sleep(0.1)
                print("\nAccessing passwords of the bank accounts ...")
                for i in tqdm(range(100), desc="Accessing..."):
                    sleep(0.3)
                print("\nComputer -> Access confirmed")
                print(
                    "\nterminalHacker -> Accessing passwords of the bank accounts in chrome://passwords and in passwords.google.com"
                )
                for i in tqdm(range(100), desc="Accessing... ", ascii=False, ncols=75):
                    sleep(0.3)
                print("\nMatching passwords with bank account number...")
                for i in tqdm(range(100), desc="Typing... ", ascii=False, ncols=75):
                    sleep(0.1)
                print("\nTyping found Bank password ...")
                for i in tqdm(range(100), desc="Typing... ", ascii=False, ncols=75):
                    sleep(0.1)
                print("\nchrome -> (Norway Bank) -> Bank Access Granted\n")

                print(
                    "\nCreating Terminal Hacker Fake bank account to transfer money in manyVpn servers."
                )
                for i in tqdm(range(100), desc="Creating... ", ascii=False, ncols=75):
                    sleep(0.3)

                print("\nBank Account Created!\n")

                print("\nTransferring Funds to Fake bank account...")
                for i in tqdm(
                    range(100), desc="Transferring Funds... ", ascii=False, ncols=75
                ):
                    sleep(0.1)

                print("\nChrome -> (Norway Bank) -> Funds Transfer.\n")

                acNo = random.randrange(10000, 50000)
                accountNo = acNo * 5000 * 1000

                pw = random.randrange(1000, 5000)
                password = pw * 254

                cvv = random.randrange(100, 500)

                print("---" * 10)
                print("\nAccount Number ->", accountNo)
                print("Account Password ->", password)
                print("CVV Number ->", cvv, "\n")
                print("---" * 10)
                print(
                    "\nThis is fake bank account for temporary , this account will available for 24 hours , then this account will deleted."
                )
                o = False

            if com == "coda install terminalHacker":
                print("Do you want to install terminalHacker.")
                norpo = input("(y or n) -> ")
                if norpo == "y":
                    pass
                else:
                    print("Exiting hacker mode...")
                    Commands.transCommand(True, path)
                    os.exit(0)

                print("\nInstall Terminal Hacker ...")
                print(
                    "\nInstalling terminalHacker , terminalHackerGetAllAccess , os , terminalHacker.exe , terminalHackerMain packages"
                )
                for i in tqdm(range(100), desc="Installing terminalHacker..."):
                    sleep(0.1)
                    pass
                print("\nDone !")
                print(
                    "\nRemaining terminalHackerGetAllAccess , os , terminalHacker.exe , terminalHackerMain packages"
                )
                for i in tqdm(
                    range(100), desc="Installing terminalHackerGetAllAccess..."
                ):
                    sleep(0.1)
                    pass
                for i in tqdm(range(100), desc="Installing os..."):
                    sleep(0.1)
                    pass
                for i in tqdm(range(100), desc="Installing terminalHackerMain..."):
                    sleep(0.1)
                    pass
                for i in tqdm(range(100), desc="Getting Permissions..."):
                    sleep(0.1)
                    pass

                print("\nterminalHacker will access all user permissions.")
                ono = input("(y / k = yes to all / n / nk = no to all / c = cancel) ->")
                if ono == "y":
                    print("Your not User.")
                    print("Exiting hacker mode...")
                    Commands.transCommand(True, path)
                    os.exit(0)
                elif ono == "k":
                    print("your are not User.")
                    print("Exiting hacker mode...")
                    Commands.transCommand(True, path)
                    os.exit(0)
                elif ono == "WindowsPassword=184567_AccessGrant=True":
                    pass
                else:
                    print("Exiting hacker mode...")
                    Commands.transCommand(True, path)
                    os.exit(0)

                print("Loading setup.exe ...")
                for i in tqdm(range(100), desc="Loading setup.exe..."):
                    sleep(0.1)
                    pass
                print("\nSetup and install is successfully done !")
                o = False

            if com == "ps hackermode --exit":
                print("\nExiting Hacker Mode...")

                sleep(0.5)
                print("\nHacker Mode Exited !\n")
                print("\nRecoving powershell...")
                sleep(0.5)
                print("powershell recovered.")
                sleep(0.2)
                os.system("powershell")
                Commands.transCommand(run=True, path=path)
                o = False

            if com == "exit":
                exit()
                break
            elif com == "exit()":
                exit()
                break
            else:
                pass

            if o == True:
                o = True
                os.system(com)
