# 📖 Table of Contents
* [Online Python Interpreters](#online-python-interpreters)
* [Python 3 local Installation](#python-3-local-installation)
   * [How to install python on Linux](#how-to-install-python-on-linux)
   * [How to install python on macOS](#how-to-install-python-on-macos)
     * [Install from the Official Installer](#install-from-the-official-installer)
     * [Install From Homebrew](#install-from-homebrew)
* [Install Python on IOS](#install-python-on-ios)
* [Install Python on Android](#install-python-on-android)

## Online Python Interpreters

The purpose of installing python is to use python. Online python interpreters are a good way to start learning python `syntax` or `code style`. If you want to try out the examples in this tutorial without setting up Python on your local machine, then **there are several websites that offer an online Python interpreter**:

- [Python.org Online Console](https://www.python.org/shell)
- [Repl.it](https://repl.it/)
- [Python Fiddle](http://pythonfiddle.com/)
- [Trinket](https://trinket.io/)
- [Python Anywhere](https://www.pythonanywhere.com/)

These cloud-based Python interpreters may not be able to execute some of the more complex examples in this tutorial, but they’re adequate for running most of the code and may be a nice way to get started.

## [Python 3 local Installation](https://realpython.com/installing-python/)

### [How to install python on Linux](https://realpython.com/installing-python/#how-to-install-python-on-linux)

There are two ways to install the official Python distribution on Linux:

1. **Install from a package manager:** This is the most common installation method on most Linux distributions. It involves running a command from the command line.
2. **Build from source code:** This method is more difficult than using a package manager. It involves running a series of commands from the command line as well as making sure you have the correct dependencies installed to compile the Python source code.

***Not every Linux distribution has a package manager, and not every package manager has Python in its package repository. Depending on your operating system, building Python from source code might be your only option***.

You can also complete the installation on Linux using alternative distributions, such as Anaconda. Anaconda is a popular platform for doing scientific computing and data science with Python. To learn how to install Anaconda on Linux, check out the [Linux installation guide](https://docs.anaconda.com/anaconda/install/linux/) in the official Anaconda documentation.

### How to install python on macOS

Python 2 comes preinstalled on older versions of macOS. This is no longer the case for current versions of macOS, starting with macOS Catalina.

There are two installation methods on macOS:

- The official installer
- The Homebrew package manager
    
    The Homebrew package manager is a popular method for installing Python on macOS because it’s easy to manage from the command line and offers commands to upgrade Python without having to go to a website. Because Homebrew is a command-line utility, it can be automated with bash scripts.
    
- The Anaconda installer [how to install Anaconda on macOS](https://docs.anaconda.com/anaconda/install/mac-os/)

MacOS Installer Recommendation

However, the Python distribution offered by Homebrew isn’t controlled by the Python Software Foundation and could change at any time. **The most reliable method on macOS is to use the official installer**, especially if you plan on doing [Python GUI programming with Tkinter](https://realpython.com/python-gui-tkinter/).

```
Note: You can also complete the installation on macOS using alternative distributions, such as Anaconda, but this tutorial 
covers only official distributions.
Anaconda is a popular platform for doing scientific computing and data science with Python. To learn how to install 
Anaconda on macOS, check out the macOS installation guide from the official Anaconda documentation.
```



#### Install from the Official Installer
 
Step 1: Download the Official Installer

1. Open a browser window and navigate to the Python.org [Downloads page for macOS](https://www.python.org/downloads/mac-osx/).
2. Under the “Python Releases for Mac OS X” heading, click the link for the *Latest Python 3 Release - Python 3.x.x*.
3. Scroll to the bottom and click *macOS 64-bit installer* to start the download.

Step 2: Run the Installer

Run the installer by double-clicking the downloaded file. You should see the following window:

![https://files.realpython.com/media/Screen_Shot_2020-07-15_at_8.31.24_AM.2e5b82dbc195.png](https://files.realpython.com/media/Screen_Shot_2020-07-15_at_8.31.24_AM.2e5b82dbc195.png)

1. Press *Continue* a few times until you’re asked to agree to the software license agreement. Then click *`Agree`*.
2. You’ll be shown a window that tells you the install destination and how much space it will take. You most likely don’t want to change the default location, so go ahead and click *`Install`* to start the installation.
3. When the installer is finished copying files, click *`Close`* to close the installer window.

Congratulations—you now have the latest version of Python 3 on your macOS computer !
    



#### Install From Homebrew
    
For users who need to install from the command line, **especially those who won’t be using Python to develop graphical user interfaces with the Tkinter module(Homebrew doesn’t provide Tkinter module)**, the Homebrew package manager is a good option. You can install from the Homebrew package manager in two steps.

Step 1: Install Homebrew

1. Open a browser and navigate to http://brew.sh/.
2. You should see a command for installing Homebrew near the top of the page under the tile “Install Homebrew.” This command will be something like the following:

```
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Highlight the command with your cursor and press Cmd+C to copy it to your clipboard.

1. Open a terminal window and paste the command, then press Enter. This will begin the Homebrew installation.
2. Enter your macOS user password when prompted.

Once the installation is complete, you’ll end up back at the shell prompt in your terminal window.

> Note: If you’re doing this on a fresh install of macOS, you may get a pop-up alert asking you to install Apple’s command line developer tools. These tools are necessary for installation, so you can confirm the dialog box by clicking Install.
> 

After the developer tools are installed, you’ll need to press Enter to continue installation of Homebrew. Now that Homebrew is installed, you’re ready to install Python.

Step 2: Install Python

1. Open a terminal application.
2. Type in the following command to upgrade Homebrew:
3. `$ brew update && brew upgrade`

Installing with Homebrew is now as straightforward as running the command **`brew install python3`**.
This will download and set up the latest version of Python on your machine.

**Congratulations—you now have Python on your macOS system !**


## Install Python on IOS

The [Pythonista app](http://omz-software.com/pythonista/) for iOS is a full-fledged Python development environment that you can run on your iPhone or iPad. It features a Python editor, technical documentation, and an interpreter all rolled into a single app.

Pythonista is surprisingly fun to use. It’s a great little tool when you’re stuck without a laptop and want to work on your Python skills on the go. It comes with the complete Python 3 standard library and even includes full documentation that you can browse offline.

To set up Pythonista, you need to [download it from the iOS app store](https://geo.itunes.apple.com/us/app/pythonista-3/id1085978097?ls=1&mt=8&at=1000lqsw).

## Install Python on Android

If you have an Android tablet or phone and want to practice Python on the go, there are several options available. The one that we found most reliably supports Python 3.8 is [Pydroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3).

Pydroid 3 features an interpreter that you can use for REPL sessions, and it also allows you to edit, save, and execute Python code.

You can [download and install Pydroid 3 from the Google Play store](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3). There is a free version and also a paid Premium version that supports code prediction and code analysis.
