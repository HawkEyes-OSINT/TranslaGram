import requests
import settings
import csv


class Translator:
    """
    Translate text from auto detect language to selected language
    """
    def __init__(self):
        self.url = "https://text-translator2.p.rapidapi.com/translate"
        self.payload = {
            "source_language": "auto",
            "target_language": self._getLang(),
            "text": ''
        }
        self.headers = {
            "content-type": "application/x-www-form-urlencoded",
            "X-RapidAPI-Key": self._getKey(),
            "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
        }


    def _getKey(self):
        """
        Get translating service API key from settings file
        """
        try:
            with open(settings.SETTINGS, 'r') as f:
                lines = list(csv.reader(f))
                KEY = lines[0][1]
            print('[+] Key found')
        except:
            print('[-] Key not found')
            settings.get_settings()
            KEY = self._getKey()
        return KEY
    
    def _getLang(self):
        """
        Get translating service language from settings file
        """
        try:
            with open(settings.SETTINGS, 'r') as f:
                lines = list(csv.reader(f))
                lang = lines[1][1]
                print(f'[+] Translating to: {lang}')
        except:
            print('[-] Language not found')
            settings.get_settings()
            lang = self._getLang()
        return lang

    def translate(self, input_text):
        """
        Translate text from auto detect language to selected language
        """
        if not input_text: # ignore empty string
            return ''
        try:
            self.payload['text'] = input_text
            response = requests.request("POST", self.url, data=self.payload, headers=self.headers)
            return response.json()['data']['translatedText']
        except:
            print('[-] Error occured')
            print(response.status_code, response.text)
            exit()
