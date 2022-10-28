import os 
import time

print(" ███████████     ███████      █████████  ███████████  ") 
print("░░███░░░░░███  ███░░░░░███   ███░░░░░███░█░░░███░░░█   ") 
print(" ░███    ░███ ███     ░░███ ███     ░░░ ░   ░███  ░    ") 
print(" ░██████████ ░███      ░███░███             ░███       ") 
print(" ░███░░░░░░  ░███      ░███░███             ░███       ") 
print(" ░███        ░░███     ███ ░░███     ███    ░███       ") 
print(" █████        ░░░███████░   ░░█████████     █████      ") 
print("░░░░░           ░░░░░░░      ░░░░░░░░░     ░░░░░       ") 

print("                                                                        ")
time.sleep(2)          
print("                    type the programm you want to use")
print("---------------------------------------------------------------------------")      
print("1.phone tracker          2.ddos tool              3.wifi extractor")
print("4.ip tracker") 
print("---------------------------------------------------------------------------")  
option = input()

if option == 1:
    os.system("python location.py")

elif option == 2:
    os.system("python ddos.py")
elif option == 3:
    os.system("python wifi-extractor.py")
elif option == 4:
    os.system("python ip-tracker.py")


                                                    