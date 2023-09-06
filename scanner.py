#!/bin/python
import socket
import os
import sys
import itertools
import threading
import signal
import time
from datetime import datetime
from colorama import Fore, Back, Style


#=================================================================================================================================


def Printbanner():
    print('''
{bright}{green}██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗{reset}
{bright}{green}██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗{reset}
{bright}{green}██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝{reset}
{green}██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗{reset}
{green}██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║{reset}
{green}╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝{reset}
                                                                                                  
    {bright}Version {green}{ver}\t\t\t\t\t\tBy: {yellow}DarkOne{white}
    '''.format(ver=1.2, red=Fore.RED, yellow=Fore.YELLOW, green=Fore.GREEN,
    blue=Fore.BLUE, pink=Fore.MAGENTA, white=Fore.WHITE, reset=Style.RESET_ALL, bright=Style.BRIGHT))
    

#=================================================================================================================================


Printbanner()


#=================================================================================================================================


if len(sys.argv) < 2:
	print("Invalid amount of arguments!")
	print('''{white}syntax:{reset}'''.format(blue=Fore.BLUE, reset=Style.RESET_ALL, white=Fore.WHITE) + '''{blue} python3 scanner2.0.py <ip> <port_start> <port end>{reset}'''.format(blue=Fore.BLUE, reset=Style.RESET_ALL))
	print('''{yellow}Exiting program...{reset}'''.format(yellow = Fore.YELLOW, reset=Style.RESET_ALL))
	print("\nExiting program")
	sys.exit()
else:
	target = socket.gethostbyname(sys.argv[1])
	    
print("- " * 25)
print("\n")
print("scanning target {}".format(target))
print("time started " + str(datetime.now()))
print("\n")
print("- "* 25)
print("\n")
ctr = 0




#long process here
#time.sleep(10)
#done = True

try:
	for port in range (int(sys.argv[2]), int(sys.argv[3])):
		
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.1)
		result = s.connect_ex((target, port))
		
					
	done = False
	def animate():
		for loop in itertools.cycle(['|', '/', '-', '\\']):
			if done:
				break
			sys.stdout.write('   \rloading ' + loop)
			sys.stdout.flush()
			time.sleep(int(sys.argv[3] - int(sys.argv[2])))
		sys.stdout.write('\rDone!     ')

	t = threading.Thread(target=animate)
	t.start()
		
			#long process here
	time.sleep(10)
	done = True

		
	if result == 0:				

		print("Port {} is open".format(port))
		
	ctr += 1
	time.sleep(1)
	sys.exit()
			
except KeyboardInterrupt:
	print('''\n{yellow}Exiting program...{reset}'''.format(yellow = Fore.YELLOW, reset=Style.RESET_ALL))
	time.sleep(1)
	os.system('clear')
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	print('''{yellow}Exiting program...{reset}'''.format(yellow = Fore.YELLOW, reset=Style.RESET_ALL))
	sys.exit()

except socket.error:
	print("Could not connect to server.")
	print('''{yellow}Exiting program...{reset}'''.format(yellow = Fore.YELLOW, reset=Style.RESET_ALL))
	sys.exit()

if ctr == 0:
	print("\nNo Open Ports...")
	print('''{yellow}Exiting program...{reset}'''.format(yellow = Fore.YELLOW, reset=Style.RESET_ALL))
	time.sleep(1)
	sys.exit()
