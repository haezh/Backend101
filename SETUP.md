# Instructions To Get Your Dev Environment Ready

## Install Python

1. Go to https://www.python.org/downloads/ and install python 3
2. Verify your python install by using  `python --version` or `python3 --version` from your shell.

## Install databases
Usually you will need to set up databases to develop your backend projects. Python comes with a lightweight database called SQLite which is good enough for our 101 demo, so you won’t need to set up a database for now.


## Install Django (Refer  [here](https://docs.djangoproject.com/en/3.1/topics/install/#installing-official-release) for more details)
 1. Install Pip by using a standalone installer.  
	 - Download get-pip.py from [here](https://bootstrap.pypa.io/get-pip.py) or use curl:
 `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
	 - Then run the following command in the folder where you have downloaded get-pip.py:
Unix/macOS:  `python get-pip.py` or `python3 get-pip.py`
Windows: `py get-pip.py`
2. Run `python -m pip install Django` to install Django
3. Verify your django install by using `python -m django --version` or `python3 -m django --version` from your shell.



## Ta-da! Now you are done with your set up! We are all good to go!


## References 
- https://docs.djangoproject.com/en/3.1/intro/install/
- https://www.djangoproject.com/start/
- https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py
