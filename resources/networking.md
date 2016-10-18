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

Just for good measure, let's try and run a command as that new `linux` user with the `sudo` command. Remember how you can pass another username as an argument, and you can run commands as that user?

```
sudo linux whoami
```

You should see `linux` as your output. Hurray!

Next: Finding your Address
-----------

Now that you have the user set up for your friend to log in as, you will need to determine _your own [IP address]_ so they know where to try to and connect to.

You can find your [IP address] on [Linux] with the command: 

```
ifconfig
```

This shows you the _configuration_ for each _interface_ currently active on your [Linux] box. Typically, the wired connection is represent by `eth0`, denoting that it is with an _eth_ernet cable (and the computer is zero-based).

You should find your [IP address] similar to the form of `10.6.1.20` or something of the like. Again, this is information you want to keep track of so you can tell your friends. This is the address they will use to connect to your computer!

Starting to SSH!
--------

__Enter [`SSH`][SSH], the [Secure Shell][SSH]!__

[`SSH`][SSH] is a very commonly used utility in the world of [Linux]. You can think of it as a remote control connection from one computer to another; you can log in and interact with the box through the [command-line], the same way you do on your own machine. All the communication and networking over the [`SSH`][SSH] protocol is encrypted (hence the name "secure").

If you are curious, take a look at the description in the `man` page of the [`ssh`][ssh] command.

```
man ssh
```


When you and your friend are ready, exchange [IP addresses][IP address] and credentials. 

You will supply the "hostname" (in this case the [IP address]) that you want to connect to as an argument to [`ssh`][ssh].

```
ssh YOUR.FRIENDS.IP.ADDRESS
```

If you are asked about some `ECDSA` key, you can hit `yes`:

```
The authenticity of host '10.6.1.9 (10.6.1.9)' can't be established.
ECDSA key fingerprint is SHA256:3LyX9qgjdyrmUY39m8iiO6fsXhwakoNqAEVqFiQP71g.
Are you sure you want to continue connecting (yes/no)? yes
```


It should then prompt you for a password (I'm using `10.6.1.9` as an example):

```
pi@10.6.1.9's password:
```

Oh! ___Be careful!___

See how it is asking us for the `pi` user's password? That's not what we want... _we want to use the `linux` user!_ (Or whatever username your friend set up for you).

By default, [`ssh`][ssh] will use thee username of YOUR user, the currently logged in user when connecting to another host. To get around this, we can specify the username we want to connect with just like an e-mail address. Break out of the current prompt with `Control+C` and change your command to supply a username, like this:

```
ssh linux@YOUR.FRIENDS.IP.ADDRESS
```


Now you should be prompted for the correct password, which you can enter -- and you should be able to log in!

Explore!
--------------

You're in a whole new computer now. Explore! See if you can find your friends personal repository or their journal reflections. 

To drive a point home, try using the `ifconfig` to see your [IP address]. You should see your friend's [IP address], since that is the box you are currently on!




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
[IP Address]: https://en.wikipedia.org/wiki/IP_address