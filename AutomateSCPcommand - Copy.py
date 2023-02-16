import os
import subprocess
import pyautogui
import time

    
def change_dir():
    while True:
        try:
            path = input("Enter new path: ")
            os.chdir(path)
            show_files()
            return path
        except FileNotFoundError: print("That path doesn't exists")
    

def show_files():
    allfiles = os.listdir()
    for item in allfiles:
            print(item)
    pick_files(allfiles)
            
def pick_files(allfiles):
    program = True
    while program == True:
        file = input("\nWelke file wil je uploaden? ")
        found = False
        for filename in allfiles:
            if file == filename:
                found = True
                transfer(file)
                program = False
        if not found:
            print("Sorry, that file doesn't exists.")
            
def transfer(file):
    server_address = "<your_ip_here>"
    username = "<your_username_here>"
    password = "<your_password_here>"
    remote_path = "<your_remote_path_here>"
    scp_command = ["scp", file, f"{username}@{server_address}:{remote_path}"]
    #alternative:
    #os.system("start cmd /k")
    #time.sleep(1)
    #pyautogui.write(scp_command)
    #pyautogui.press("enter")
    #time.sleep(1)
    #pyautogui.write(password)
    #pyautogui.press("enter")
    # 
#universl_newlines specifies whether to use text mode or binary mode for input/output streams.
    process = subprocess.Popen(scp_command, universal_newlines=True)
    time.sleep(1)
    pyautogui.write(password)
    pyautogui.press("enter")
    transfer_again()

def transfer_again():
    choice = input("Do you want to transfer another file? Type Y/N ")
    if choice.upper() == "Y":
        main()
    else:
        print("Thank you and goodbye")
        exit()    

def main():
    current_path = os.getcwd()
    print(f"The current dir is: {current_path}")
    optie = input("\nAre you in the right dir? Type Y/N ")
    if optie.upper() == "Y":
        show_files()
    else: change_dir() 
          
main()


    






