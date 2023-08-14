# TranslaGram
Get chats from a Telegram group in from any language to a CSV translated to any language

## About
TranslaGram connects to your Telegram user to create CSV files containg the chats in groups and channels your user is in.
After you install and set up the program, you will be able to choose the group or channel from which you would like to retreive the chats.
The program will then create a CSV file in the 'chat' folder located in the programs directory.
The CSV file will contain the 300 most recent messages in their original language, the sender and the message translated in to the chosen language.

This program uses a text translator API from RapidAPI, and you will need to obtain an API key.  You will find instructions on how to do this below.

## Installation
Open a command line in the directory you want to store the code files and run:

    git clone https://github.com/HawkEyes-OSINT/TranslaGram.git
    pip install -r requirements.txt
    mkdir chats

To run the program:

    python translagram.py

## Setup Preperatrion
### In order to use TranslaGram, you will need several API keys.

#### Text Translator
Subscribe to RapidAPI at https://rapidapi.com/auth/sign-up

Visit https://rapidapi.com/dickyagustin/api/text-translator2/pricing and choose a plan.
Click on the 'Subscribed' drop down on the right hand side and select 'View Analytics'
On the left hand side, click on the application drop down and click on 'Authorization'.
There you will find your API key, have this key on hand for the setup process.

#### Telegram API
Visit https://my.telegram.org/auth, enter the phone number associated with the Telegram account you want to use, and click 'Next'

You will receive a confirmation code on your Telegram app, enter this code and click 'Sign In'

Click on 'API Develpment Tools'.  You only need to fill out the Title and Short Title fields.

You will now be provided an 'App api_id' and an 'App api_hash'.  Have these items on hand for the setup process.




