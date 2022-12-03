#Introduction
login.py:- This script will validate user login to Gmail
.
send_email.py:- This script will check scenario of sending an email.


#Installation
For Windows/Mac:- #please install python3 and add python3 path to system path
For Linux:- Install Python3- sudo apt install python3, 
   Now type python, if you getting python-not found.
   Type- sudo apt-get install python-is-python3
pip3 install virtualenv
. venv/bin/activate

pip3 install -r requirements.txt

Note: Currently this test cases using firefox,chrome for testing. We are passing broswer dynimacally from command line. We can add new browser anytime.
python3 ~/git/automation_test/test/login.py browser_name
For Example:-
To run:-
cd automation_test
python3  test/login.py chrome
python3 test/login.py firefox
python3 test/send_email.py chrome
python3 test/send_email.py firefox

#Using .env file for password.


