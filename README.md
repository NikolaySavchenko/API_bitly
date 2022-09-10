# API_2_Bitly

The program takes a link and:
- If it's a regular link, then shortens it using the service [bitly.com](https://app.bitly.com/)
- If it's a bitlink, then return the number of clicks on it

How to install
------

Python3 should already be installed. Use pip (or pip3, if there is a conflict with Python2) to install dependencies:

    pip install -r requirements.txt
    
For using you also need your TOKEN from [bitly.com](https://app.bitly.com/)
You should use environment variables. Create file **.env** and variable BITLY_TOKEN with your token.
This token we use in API_2_Bitly.py in **main** function:

    token = os.getenv('BITLY_TOKEN')



Recomended to use [virtualenv/venv](https://docs.python.org/3/library/venv.html)

Project Goals
------
This code was written for educational purposes as part of an online course for web developers at dvmn.org.