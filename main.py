import os
import time
import getpass

print("ProgrammingTools")
print("Code By > https://github.com/adilaxmdv")
userchk = os.popen("id -u").read().strip("\n")
if int(userchk) != 0:
  print("Please run script as root, Aborting!")
  exit()
time.sleep(3)
os.system("clear")
print(">>>Main Page")

print("""
1)Update System
2)Install Editors
3)Install Programming Language
4)Exit
5)Upgrade System
""")
slct = int(input("Select One:"))
if slct == 1:
        os.system("apt update")
elif slct == 5:
        os.system("apt upgrade")
elif slct == 2:
        print("""
        1)Visual Studio Code
        2)Atom
        3)Pycharm 
        4)Vim
        5)Geany
        """)
        code= int(input("Select:"))
        if code == 1:
                os.system("apt install code")
        elif code == 2:
                os.system("""sudo add-apt-repository "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main""")
                os.system("sudo apt install atom")
        elif code == 3:
                os.system("sudo snap install pycharm-community --classic")
        elif code == 4:
                os.system("sudo apt install vim")
        elif code == 5:
                os.system("apt install geany -y")
        else:
                exit
elif slct == 3:
            print("""
    1)Python
    2)Php
    3)C
    4)Cpp
    5)Golang
    6)Ruby
    """)
lng = int(input("Select:"))
if lng == 1:
            os.system("apt install python3")
elif lng == 2:
            os.system("apt install php")
elif lng == 3:
            os.system("apt update")
elif lng == 4:
            os.system("sudo apt-get install g++")
elif lng == 5:
            os.system("apt install golang")
elif lng == 6:
            os.system("apt install ruby")
elif slct== 4:
            exit

 
