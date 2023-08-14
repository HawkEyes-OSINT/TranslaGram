from telethon import TelegramClient
import translator
import settings
import csv

"""
Handle interactions with Telegram API
"""

LIMIT = 300


class Account:
    """
    telegram account api details
    """
    def __init__(self):
        self.API_ID, self.API_HASH, self.PHONE_NUMBER = self._getaccount()

    def _getaccount(self):
        try:
            # retreive account data from settings file
            with open(settings.SETTINGS, 'r') as f:
                reader = csv.reader(f)
                row = list(reader)
                api_id, api_hash, phone_number = row[2][1], row[3][1], row[4][1]
            print('[+] Account found')
            return api_id, api_hash, phone_number
        except:
            # account not found
            print('[-] Account not found')
            settings.get_settings()
            return self._getaccount()
        


async def choose_group(client):
    """
    Ask user to choose a group or channel from their dialogs
    """
    dialogs = await client.get_dialogs()

    # list groups and channels
    print("Your Groups and Channels:")
    for index, dialog in enumerate(dialogs, start=1):
        if dialog.is_group or dialog.is_channel:
            print(f"{index}. {dialog.title}")

    # choose group
    choice = int(input("Enter the number of the group to extract messages from: ")) - 1

    # check if choice is valid
    if 0 <= choice < len(dialogs) and (dialogs[choice].is_group or dialogs[choice].is_channel):
        return dialogs[choice].entity
    else:
        print("[-] Invalid choice")
        return choose_group(client)


async def get_messages(client, group_entity):
    """
    Get messages from a group or channel and translate them
    """
    t = translator.Translator()
    messages = []

    # get messages
    print('[!] Getting messages')
    async for message in client.iter_messages(group_entity):
        messages.append(message)
        if len(messages) >= LIMIT:
            break

    # save messages to csv
    with open(f'chats/{group_entity.title}_chat.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Sender', 'Message', 'Translation'])

        print('[!] Translating messages')
        for message in messages:
            if message.sender_id:
                sender = await client.get_entity(message.sender_id)
                if sender.username:
                    sender_name = sender.username
                elif sender.first_name:
                    sender_name = sender.first_name
            else:
                sender_name = 'System'

            csv_writer.writerow([sender_name, message.text, t.translate(message.text)])
