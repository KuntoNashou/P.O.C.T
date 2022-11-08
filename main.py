import os 
import time
import subprocess


os.system('cls')

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
print("""                    type the programm you want to use
        ---------------------------------------------------------------------------     
        1.precise phone tracker          2.ddos tool              3.wifi extractor
         4.ip tracker                     5.phone tracker(country & service) 
        --------------------------------------------------------------------------  
        https://github.com/KuntoNashou/P.O.C.T    |     Made By KuntoNashou""")

option = input('>')

if option == "1":
    exec(open('util/location.py').read())

elif option == '2':
    print("We are sorry but this tool is under construction")

elif option == '3':
    exec(open("util/wifi-extractor.py" ).read())
    
elif option == '4':
    exec(open("util/ip-tracker.py").read())

elif option == '5':
    exec(open("util/phone-tracker.py").read())
  
else:
    print("wrong command. retry")



                                                    