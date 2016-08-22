#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-08-13 23:48:50
# @Last Modified by:   john
# @Last Modified time: 2016-08-19 14:23:26

import readline
import sys
import time
import socket
import os
import colorama
import subprocess
import textwrap
import threading

from colors import *

wrong_command_tally = 0
punction_stops = "\n.,!?-"

something_to_say_inbetween = ""
current_module = None

entered = ""

time_on = False

class Module(object):
	'''
	This should acts as like the "template" module for all the future lessons
	
	The function `go()` is the one that acts like the script for the whole
	module. It should be able to see and determine if things are going
	according to plan. 
	'''

	def __init__( self ):

		self.wrong = "That is not what you should be trying to do right now!"
		self.seen_entries = []
		self.understands = {}

	def learn_something( self, name, message, command_waiting, incorrect, on_correct = None ):

		global entered, something_to_say_inbetween

		if ( name not in self.understands ):
			self.understands[name] = False

		if ( not self.understands[name] ):
				say(C( textwrap.dedent(message) ))

				wanted_arguments = command_waiting.split()
				number_of_wanted_arguments = len(wanted_arguments)

				while (command_waiting not in self.seen_entries):
					prompt()

					arguments = entered.split(" ")
					number_of_arguments = len(arguments)

					if ( number_of_arguments != number_of_wanted_arguments ):
						if ( not self.understands[name] ):
							process()
							print( Y("\n" + textwrap.dedent(incorrect) + "\n") )
							continue


					if ( number_of_wanted_arguments > 1 ):
						
						if ( number_of_wanted_arguments == 2 ):
							
							if ( wanted_arguments[-1] == "???" ):
								
								if ( number_of_arguments == number_of_wanted_arguments ):
									# They got it!
									# print "Got it!"
									if ( on_correct ):
										on_correct()
									self.understands[name] = True
									self.seen_entries.append(command_waiting)

					else:
						
						if entered == command_waiting:
							
							# They got it!
							if ( on_correct ):
								on_correct()
							self.understands[name] = True


					process()

					if ( not self.understands[name] ):
						print( Y("\n" + textwrap.dedent(incorrect) + "\n") )

		something_to_say_inbetween = ""
		self.seen_entries = []


	def go( self ):

		# You will want to include these variables so you can control them
		# while you go through the "script"
		global entered, something_to_say_inbetween

		pass


class FirstTimeModule( Module ):

	def __init__( self ):

		super( FirstTimeModule, self ).__init__()

	def go( self ):

		global entered, something_to_say_inbetween

		self.learn_something( "The Name of the Shell", 

							message = ''' 

Hello!

Welcome to the Intro to Linux "Training Wheels" shell!

This tool is designed to help you learn about Linux and how to navigate a
command-line interface. That's what you are using right now... a command-line!

Often times it is called a "shell", or a "console", or a "terminal"... 
it has many names. But, the jist of it is, the way that you interact with it
is by you entering "commands" and having it do things.

Do you understand that?

		''',
							 command_waiting = "yes",
							 incorrect = "Should I explain it one more time?",
							 on_correct = self.after_yes_command )
		
		self.learn_something( "Standard Streams",

							message = ''' 

WOAH! 

That was crazy! 

Did you see what happened?

I'm letting you live entirely inside the shell, so all you can really enter
are commands, whether they work or not. Check it out:

You entered the `yes` command, and -- believe it or not -- that really is a 
command!

It repeatedly sends the letter 'y' to standard output.

Standard output is one of the three "streams" that are SUPER important when 
working with the Linux shell. 

(1) There is standard output... like everything you are seeing right now, the 
things that are printed out on the screen by certain programs or commands. 

(2) There is standard input, like how you just entered that command with the
keyboard, or how you use a mouse to interact with your computer.

(3) And there is standard error, which gets displayed like standard output, 
but is reserved for error messages or when things go wrong with a program.

Does that all make sense to you?

		''',
							 command_waiting = "yes",
							 incorrect = '''
If you need more clarification, ask around or Google it!
Does it make sense to you now?
''' )



		self.learn_something( "Standard Error", 

							message = ''' 

And it looks like you have figured out that Control + C will break out of a 
running program, or stop it from running inside your shell. Awesome!

So, funnily enough, there may be a `yes` command, but there actually is not a
`no` command. Try entering "no" and see what happens!

		''',
							 command_waiting = "no",
							 incorrect = '''
Try and enter \"no\" as a command, and see what happens.
''' )

		self.learn_something( "Echo Command", 

							message = ''' 

Check out how the shell told you that wasn't a real command. It printed out
the error message on the screen... but it was on the standard error stream!

Like I said before, standard error (or "stderr") is usually printed on standard
output (or "stdout"), but it itself is a separate stream.

So you are typing on the keyboard, putting data into the standard input (or 
"stdin") stream, and you can even control what goes to standard output.

The command `echo` will let you work with stdout. Try entering "echo"!

		''',
							 command_waiting = "echo",
							 incorrect = '''
Enter just the `echo` command.
''' )

		self.learn_something( "Command arguments", 

							message = ''' 

Hmm... nothing happened! 

The `echo` command didn't do anything!

Why not? Well, we didn't give it any arguments!

The very first thing you type into the shell is the "command". Anything that
follows is considered an "argument", or a "parameter", that you pass to the
command. 

Try entering something like "echo hello" or "echo USCGA".

		''',
							 command_waiting = "echo ???",
							 incorrect = '''
Try running the `echo` command with an argument!
''' )

		self.learn_something( "More arguments", 

							message = ''' 

Nice! See how it "echo-ed out" the argument you passed to it? It just sent it
to the standard output. That is really all the `echo` command does, it just
puts whatever you give it as arguments out onto stdout. 

The `yes` command that we saw earlier also takes an argument. Give it a try!

		''',
							 command_waiting = "yes ???",
							 incorrect = '''
Give the `yes` command an argument and see what happens.
''' )

		self.learn_something( "Intro to the man pages", 

							message = ''' 

Nice, see how the `yes` command printed out your argument over and over again,
rather than just the letter `y`? When you pass arguments to a program, you
change how the program behaves when it executes.

Keep in mind that arguments are separated by spaces. The very first thing you
type in into the shell is your command, and then everything following the 
first space is an argument.

Here's another funny named command: `man`. Try it! Don't give it any arguments
just yet.

		''',

							 command_waiting = "man",
							 incorrect = '''
Enter just the `man` command.
''' )


		self.learn_something( "What is a man page?", 

							message = ''' 
See how it asked you about a "manual page"? That is exactly what you think it
is. The `man` command will show you a manual regarding any certain command, so
you can learn more about what that command does, or how you can use it.

Try it with an argument. Let's check out the manual for that `yes` command.

		''',

							 command_waiting = "man yes",
							 incorrect = '''
What do you think you would enter to see the manual for the `yes` command?
''' )

		self.learn_something( "Man page for `yes`", 

							message = ''' 


		''',

							 command_waiting = "man man",
							 incorrect = '''
What do you think you would enter to see the manual for the `yes` command?
''' )
	
	
	def after_yes_command( self ):
		global something_to_say_inbetween

		something_to_say_inbetween = R(	"Oh no! You entered a special command!\n" + \
											"Press CONTROL and C at the same time to stop it!\n")


def load_module():

	# Here we should read from a save file of what things the person
	# has learned or still needs to work with. 
	# While testing, we'll just load the first module.

	global current_module

	current_module = FirstTimeModule()


def say(message):
	for character in message:
		sys.stdout.write(character)
		sys.stdout.flush()
		if time_on:
			if character in punction_stops:
				time.sleep(0.2)
			else:
				time.sleep(0.03)


def test_special_cases( ):

	global entered

	args = entered.split()
	
	if ( args[0] == "cd" and len(args) == 1 ):
		os.chdir( os.environ['HOME'] )

	if ( ( args[0] == "exit" or args[0] == "quit" ) and len(args) == 1 ):
		say_goodbye()

def get_size():

	global rows, columns

	rows, columns = [ int(a) for a in os.popen('stty size', 'r').read().split()] 
	return rows, columns

def error(e):
	print colorama.Back.BLACK + R("Oh no! I hit an error!")
	print r("\n" + str(e.__repr__())), colorama.Back.RESET
	print r("\n" + e.child_traceback), colorama.Back.RESET

def say_goodbye():

	global rows, columns

	get_size()

	print C("\n\nGoodbye!") 
	
	print B("_" * columns + "\n")
	exit()

def process():

	global entered

	if entered == "":
		return

	test_special_cases()

	try:

		p = subprocess.Popen( entered.split(), 	stdout = subprocess.PIPE, 
												stdin=subprocess.PIPE )

		while ( p ):
			try:
				sys.stdout.write( something_to_say_inbetween )
				sys.stdout.write( p.stdout.next() )
			except StopIteration:
				break

	except OSError as e:
		print entered + ": command not found"


def prompt():

	global entered

	ps1 = "".join([	colorama.Fore.GREEN, colorama.Style.BRIGHT, 
					os.environ['USER'], '@', socket.gethostname(), 
					colorama.Fore.BLUE, " ", os.getcwd(), " $ ", 
					colorama.Fore.RESET, colorama.Style.NORMAL
				  ]).replace( os.environ["HOME"], "~" )

	entered = raw_input(  ps1 )
	readline.add_history( entered )
	current_module.seen_entries.append(entered)

def run():


	global current_module

	if ( current_module == None ):
		print R("No module loaded... nothing to do!")

	while ( True ):

		try:
			current_module.go()
			# prompt()
			# process()

		except KeyboardInterrupt:
			
			sys.stdout.write("^C\n")
			continue

		except Exception as e:
			error(e)

def print_banner():
	global columns
	get_size()


	os.system("clear")
	print B("-" * columns )
	print c(\
" ... this tool was developed by John Hammond. If you're curious about it, ask!\n")


def main():

	global current_module

	print_banner()
	load_module()
	run()


if ( __name__ == "__main__" ):
	main()