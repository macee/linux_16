October 18th, 2016
======================

> John Hammond | Intro to Linux 2016

--------------------------------------

Recap:
-----

Welcome back to __Intro to Linux!__

Last week, you learned in [Training Wheels] how to interact with the _root_ user and even create and manage user accounts on your own. 

If you don't remember, does the command `sudo` ring a bell? It is "Super User Do"! ... in that you can temporarily _borrow_ the _root_ users powers to do escalate your privileges and do things like install new software, add new users, or manage essential parts of the file system.

For Today's Class...
-------

Today, we'll be brushing the dust off of the `sudo` command and just briefly reviewing how to add a user. Then, we'll explore some simple networking things that [Linux] can do for us, an awesome thing called [`SSH`][SSH], and some file permissions. 

Let's dive right in!
-------

To get started, let's set the stage: today, you're going to be _remote controlling_ your friend's [Raspberry Pi]. That's right -- you're going to log into their computer... _from your computer!_

This works both ways, though -- just as you will be logging into their computer, _they_ will be logging into yours!

To set this up and to review some concepts from last week, we'll add a user to our machine.

Adding the User
----------------

You may not remember from last week, but last week we used a command called [`useradd`][useradd] to create a new user on your [Linux] computer. It wasn't very nice to us; we have to supply arguments for the user's home directory, their shell, we had to set the password separately, and other silly stuff.

I briefly mentioned at the end of the [Training Wheels] lesson that there is a better command to add a user, that simply has its words reordered: [`adduser`][adduser]. This will prompt you for the password and set everything up for you.

Let's create a user with an easy name like `linux` and a simple password like `is for penguins`. (I like to use spaces in my passwords [because it really amps up the entropy bits](http://lifehacker.com/5796816/why-multiword-phrases-make-more-secure-passwords-than-incomprehensible-gibberish) and the strength of the password) You don't have to use these exact credentials; but make it something simple and easy to remember, because you'll be telling them to your friend.

```
adduser linux
```


Oh! If you run this, you may get an error: `adduser: Only root may add a user or group to the system.`. Remember you need `sudo`!

```
sudo adduser linux
```

You should then be greeted with a lot of prompts, which you can fill out (or not fill out) however you would like, it really doesn't matter for the point of our exercise.

```
Adding user `linux' ...
Adding new group `linux' (1002) ...
Adding new user `linux' (1003) with group `linux' ...
Creating home directory `/home/linux' ...
Copying files from `/etc/skel' ...
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
Changing the user information for linux
Enter the new value, or press ENTER for the default
    Full Name []: Linux  
    Room Number []:  
    Work Phone []: 
    Home Phone []: 
    Other []: 
Is the information correct? [Y/n] y
```

Once you get your prompt back, you can do things to verify that the new user has been created. Try checking out the home directories with a command like `ls /home`, or even viewing the `/etc/passwd` file with `cat`. At this point, I trust you to be able to do things like that (if you feel unsure about them, let me know!)

Just for good measure, let's try and run a command as that new `linux` user with the `sudo` command. Remember how you can pass another username as an argument, and you can start

[Training Wheels]: https://github.com/macee/linux_16/tree/master/training_wheels
[MicroSD]: https://en.wikipedia.org/wiki/MicroSD
[Raspbian]: https://www.raspberrypi.org/downloads/raspbian/
[operating system]: https://en.wikipedia.org/wiki/Operating_system
[operating systems]: https://en.wikipedia.org/wiki/Operating_system
[github]: https://github.com/
[bash]: https://en.wikipedia.org/wiki/Bash_(Unix_shell)
[IMG]: https://en.wikipedia.org/wiki/IMG_(file_format)
[Linux]: https://en.wikipedia.org/wiki/Linux
[Microsoft Windows]: https://en.wikipedia.org/wiki/Microsoft_Windows
[command-line]: https://en.wikipedia.org/wiki/Command-line_interface
[command line]: https://en.wikipedia.org/wiki/Command-line_interface
[Raspberry Pi]: https://www.raspberrypi.org/
[open-source]: https://en.wikipedia.org/wiki/Open-source_software
[Python]: https://www.python.org/
[github]: https://github.com
[Flask]: http://flask.pocoo.org/
[JSON]: http://www.json.org/
[SSH]: https://en.wikipedia.org/wiki/Secure_Shell
[useradd]: https://linux.die.net/man/8/useradd
[adduser]: http://askubuntu.com/questions/345974/what-is-the-difference-between-adduser-and-useradd