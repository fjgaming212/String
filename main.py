# Copyleft (c) 2020 Mr.Miss, All wrongs reserved.
#
# Redistribution and use in source with or
# without modufication, are permitted.


import time
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from pyrogram import Client

select = " "

docs = """Generate your Telegram String Session

P -->> Pyrogram (Bot Music) [https://docs.pyrogram.org]
T -->> Telethon (Userbot)   [https://docs.telethon.dev]
"""

tutor = """
~ go-to my.telegram.org
~ Login using your Telegram account
~ Click on API Development Tools
~ Create a new application, by entering the required details
~ Check your Telegram saved messages section to copy the STRING_SESSION
"""

template = """
Thank you for Support @Farizsj
            
<code>STRING_SESSION</code>: <code>{}</code>

⚠️ <b>Please be carefull to pass this value to third parties</b>"""


print(docs)


        print("""\nPyrogram selected.\nRunning script...""")
        time.sleep(1)
        print(tutor)
        with Client(
        "UserBot", 
        api_id=int(input("Enter API ID: ")),
        api_hash=input("Enter API HASH: ")) as pyrogram:
            saved_messages_template = "Pyrogram session" + template.format(pyrogram.export_session_string())
            print("\nGenerating String session...\n")           
            pyrogram.send_message("me", saved_messages_template, parse_mode="html")
            time.sleep(1) 
            print("Your STRING_SESSION value have been sent to your Telegram Saved Messages")
        break
    
