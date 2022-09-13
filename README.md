# API_2_Bitly

The program takes a link and:
- If it's a regular link, then shortens it using the service [bitly.com](https://app.bitly.com/)
- If it's a bitlink, then return the number of clicks on it

How to install
------

Python3 should already be installed. Use pip (or pip3, if there is a conflict with Python2) to install dependencies:

    pip install -r requirements.txt
    
For using you also need your TOKEN from [bitly.com](https://app.bitly.com/)
You should use environment variables. Create file name **.env** and variable BITLY_TOKEN in the root directory.
In file **.env** only one line:

    BITLY_TOKEN='here is your own TOKEN'

Example for command line:

    $ python '\API_bitly\API_2_Bitly.py' https://dwmn.org
    Битлинк: https://bit.ly/3U0CDXa

Recomended to use [virtualenv/venv](https://docs.python.org/3/library/venv.html)

Project Goals
------
This code was written for educational purposes as part of an online course for web developers at dvmn.org.
