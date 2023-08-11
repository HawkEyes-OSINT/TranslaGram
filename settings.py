import csv
import os

"""
This module contains the settings of the bot.
"""

SETTINGS = 'settings.csv'
TRANSLATE_SERVICE = 'X-RapidAPI-Key'
LANGUAGES = """
Language Name 	    Language Code

Afrikaans               af
Albanian                sq
Amharic                 am
Arabic                  ar
Armenian                hy
Azerbaijani             az
Basque                  eu
Belarusian              be
Bengali                 bn
Bosnian                 bs
Bulgarian               bg
Catalan                 ca
Cebuano                 ce
Chichewa                ny
Chinese (Simplified)    zh-CN
Chinese (Traditional)   zh-TW
Corsican                co
Croatian                hr
Czech                   cs
Danish                  da
Dutch                   nl
English                 en
Esperanto               eo
Estonian                et
Filipino                tl
Finnish                 fi
French                  fr
Frisian                 fy
Galician                gl
Georgian                ka
German                  de
Greek                   el
Gujarati                gu
Haitian Creole          ht
Hausa                   ha
Hawaiian                haw
Hebrew                  iw
Hindi                   hi
Hmong                   hmn
Hungarian               hu
Icelandic               is
Igbo                    ig
Indonesian              id
Irish                   ga
Italian                 it
Japanese                ja
Javanese                jw
Kannada                 kn
Kazakh                  kz
Khmer                   km
Korean                  ko
Kurdish (Kurmanji)      ku
Kyrgyz                  ky
Lao                     lo
Latin                   la
Latvian                 lv
Lithuanian              lt
Luxembourgish           lb
Macedonian              mk
Malagasy                mg
Malay                   ms
Malayalam               ml
Maltese                 mt
Maori                   mi
Marathi                 mr
Mongolian               mn
Myanmar (Burmese)       my
Nepali                  ne
Norwegian               no
Odia (Oriya)            or
Pashto                  ps
Persian                 fa
Polish                  pl
Portuguese              pt
Punjabi                 pa
Romanian                ro
Russian                 ru
Samoan                  sm
Scots Gaelic            gd
Serbian                 sr
Sesotho                 st
Shona                   sn
Sindhi                  sd
Sinhala                 si
Slovak                  sk
Slovenian               sl
Somali                  so
Spanish                 es
Sundanese               su
Swahili                 sw
Swedish                 sv
Tajik                   tg
Tamil                   ta
Telugu                  te
Thai                    th
Turkish                 tr
Turkmen                 tk
Ukrainian               uk
Urdu                    ur
Uyghur                  ug
Uzbek                   uz
Vietnamese              vi
Welsh                   cy
Xhosa                   xh
Yiddish                 yi
Yoruba                  yo
Zulu                    zu
Hebrew                  he
Chinese (Simplified)    zh
"""


def checksettings():
    """
    Check if the settings file exists.
    """
    set = True
    with open(SETTINGS, 'r') as f:
        lines = f.readlines()

        # check translater API key
        if not lines[0][0] == TRANSLATE_SERVICE or not lines[0][1]:
            set = False
            print('[-] Missing API key for translater service.')
        
        # check translater language
        if not lines[1][0] == 'language' or not lines[1][1]:
            set = False
            print('[-] Missing language for translater service.')

        # check telegram settings
        if not lines[2][0] == 'api_id' or not lines[2][1]:
            set = False
            print('[-] Missing api_id for telegram service.')
        if not lines[3][0] == 'api_hash' or not lines[3][1]:
            set = False
            print('[-] Missing api_hash for telegram service.')
        if not lines[4][0] == 'phone_number' or not lines[4][1]:
            set = False
            print('[-] Missing phone_number for telegram service.')

    return set

def get_settings():
    """
    Get the settings from the user for the settings file
    """
    with open(SETTINGS, 'w') as f:
        # translation details
        f_writer = csv.writer(f)
        f_writer.writerow([TRANSLATE_SERVICE, input('Enter X-RapidAPI-Key: ')])
        print(LANGUAGES)
        f_writer.writerow(['language', input('Enter language: ')])
        
        # telegram details
        f_writer.writerow(['api_id', input('Enter api_id: ')])
        f_writer.writerow(['api_hash', input('Enter api_hash: ')])
        f_writer.writerow(['phone_number', input('Enter phone_number: ')])

def change_api_key():
    # Read the original CSV file
    with open(SETTINGS, 'r') as original_csv:
        csv_reader = csv.reader(original_csv)
        rows = list(csv_reader)  # Convert CSV content to a list of rows

    # Replace the specified row with new_row_data
    rows[0][1] = input('Enter X-RapidAPI-Key: ')

    # Write the modified data to a new CSV file
    with open(SETTINGS, 'w', newline='') as new_csv:
        csv_writer = csv.writer(new_csv)
        csv_writer.writerows(rows)

def change_language():
    # Read the original CSV file
    with open(SETTINGS, 'r') as original_csv:
        csv_reader = csv.reader(original_csv)
        rows = list(csv_reader)  # Convert CSV content to a list of rows

    # Replace the specified row with new_row_data
    print(LANGUAGES)
    rows[1][1] = input('Enter language: ')

    # Write the modified data to a new CSV file
    with open(SETTINGS, 'w', newline='') as new_csv:
        csv_writer = csv.writer(new_csv)
        csv_writer.writerows(rows)
        
def change_telegram_settings():
    # Read the original CSV file
    with open(SETTINGS, 'r') as original_csv:
        csv_reader = csv.reader(original_csv)
        rows = list(csv_reader)  # Convert CSV content to a list of rows

    # Replace the specified row with new_row_data
    rows[2][1] = input('Enter api_id: ')
    rows[3][1] = input('Enter api_hash: ')
    rows[4][1] = input('Enter phone_number: ')

    # Write the modified data to a new CSV file
    with open(SETTINGS, 'w', newline='') as new_csv:
        csv_writer = csv.writer(new_csv)
        csv_writer.writerows(rows)
        