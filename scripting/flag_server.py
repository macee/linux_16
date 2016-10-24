#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-02-08 11:31:10
# @Last Modified by:   john
# @Last Modified time: 2016-02-14 16:46:46

import subprocess
from colorama import *
import os

from threading import Thread

from time import *

logging = True
init(autoreset = True)

flag_filename = "flag"
flag = ''

def return_flag( flag ):
	return Fore.GREEN + Style.BRIGHT + flag + Style.NORMAL + Fore.RESET

def log( string ):
	if logging: print string

def generate_flag(show=False):

	global flag

	bash_command = "head /dev/urandom|sha1sum|cut -d' ' -f1"
	flag =  subprocess.check_output( bash_command, shell=True ).strip()

	if (show): log ( Fore.YELLOW + "Generated new flag " + return_flag( flag ) )

	return flag

def save_flag( flag, folder_location = '.' ):
	
	global flag_filename
	
	flag_file_location = os.path.join(folder_location, flag_filename )
	handle = open( flag_file_location, 'w' )
	handle.write( flag )
	handle.close()

	log( Fore.YELLOW + "Saved flag " + return_flag( flag ) + \
	     Fore.YELLOW + " at " + Fore.CYAN + flag_file_location  )

def flag_timer( flag_reset_time = 60 ):
	
	while True:
		flag = generate_flag()
		save_flag( flag )

		sleep( flag_reset_time )

def main():
	
	flag_timer_thread = Thread( target = flag_timer )
	flag_timer_thread.start()
	
	while True:
		print "What is the flag?"
		raw_input(  )
		print "The flag is currently", flag

if ( __name__ == "__main__" ):
	main()