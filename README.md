#Introduction
test_uer_story1.py:- This script will check KiwiSaver Retirement Calculator all fields in the calculator have got the information icon present.
.
test_uer_story2.py:- This script will check KiwiSaver Retirement Calculator users are able to calculate what their KiwiSaver projected balance would be at retirement.


#Installation
yum install -y python3
pip3 install virtualenv
. venv/bin/activate

pip3 install -r requirements.txt

#MAC OS
#please download latest firefox and geckodriver for this test and add your geckodriver executable path to config.ini file

#WINDOWS OS
#please download latest firefox and geckodriver for this test and add your geckodriver executable and firefox path to system path

#ToRun
python3 ~/git/Westpac_Test/test_uer_story1.py
python3 ~/git/Westpac_Test/test_uer_story2.py

