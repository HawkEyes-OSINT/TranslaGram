from telethon.sync import TelegramClient
import telegram
import settings
from colorama import Fore
import asyncio
import pyfiglet

"""
Main execution file
"""



def ui():
    """
    User Interface
    """
    # display welcome message
    ascii_title = pyfiglet.figlet_format('TranslaGram')
    print(Fore.GREEN + ascii_title)

    # introduction
    print(Fore.YELLOW + "This is a simple telegram bot that translates messages from one language to another.")
    print(Fore.YELLOW + "It uses the X-RapidAPI-Key from the Translate Service.")
    print()

    # get instructions
    print(Fore.WHITE + "What would you like to do?")
    print(Fore.WHITE + "1. Translate messages")
    print(Fore.WHITE + "2. Change settings")
    print(Fore.WHITE + "3. Exit")

    return input(Fore.WHITE + "Enter your choice: ")

def select_change_settings():
    """
    Choose what settings to change
    Call relevant method from settings file
    """
    # get instruction
    print()
    print(Fore.WHITE + "What would you like to change?")
    print(Fore.WHITE + "1. Telegram account")
    print(Fore.WHITE + "2. Translate Service")
    print(Fore.WHITE + "3. Language")
    choice = input(Fore.WHITE + "Enter your choice: ")

    if choice == '1': # telegram account
        settings.change_telegram_settings()
        print(Fore.GREEN + "[+] Telegram account settings changed")
        print()
    elif choice == '2': # translation api
        settings.change_api_key()
        print(Fore.GREEN + "[+] Translate Service settings changed")
        print()
    elif choice == '3': # language
        settings.change_language()
        print(Fore.GREEN + "[+] Language settings changed")
        print()
    else: # invalid choice
        print(Fore.RED + "[-] Invalid choice")
        select_change_settings()
        print()

    
async def main():
    exit = False

    while not exit:
        input = ui()

        # translate messages
        if input == '1':
            # get account details
            session = 'session'
            account = telegram.Account()
            async with TelegramClient(session, account.API_ID, account.API_HASH) as client:
                await client.start(account.PHONE_NUMBER)

                # choose group to extract messages from
                group_entity = await telegram.choose_group(client)
                if group_entity:
                    # get messages
                    await telegram.get_messages(client, group_entity)
            print(Fore.GREEN + f'[+] Completed! Messages saved to [chats/group_name_chat.csv]')

        # change API settings
        elif input == '2':
            select_change_settings()
            

        # exit
        elif input == '3':
            exit = True

        else:
            print(Fore.RED + "[-] Invalid choice")

if __name__ == '__main__':
    asyncio.run(main())