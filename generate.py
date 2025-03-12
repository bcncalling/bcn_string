import os
import asyncio
from pyrogram import Client
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from hydrogram import Client as HydrogramClient 

API_ID = 14688437  # PUT YOUR OWN API
API_HASH = "5310285db722d1dceb128b88772d53a6"  # PUT YOUR API HASH

async def telethon_session():
    api_id = API_ID
    api_hash = API_HASH

    async with TelegramClient(StringSession(), api_id, api_hash) as client:
        print("Generating Telethon String Session...")
        session_string = client.session.save()
        await client.send_message("me", f"**Your string session:**\n\n`{session_string}`")
        print("Your Telethon string session was saved in your saved messages.")
        return session_string

async def pyrogram_session():
    name = "BCN"
    api_id = API_ID
    api_hash = API_HASH

    async with Client(
        name,
        api_id=api_id,
        api_hash=api_hash
    ) as app:
        print("Generating Pyrogram V2 String Session...")
        session_string = await app.export_session_string()
        await app.send_message("me", f"**Your string session:**\n\n`{session_string}`")
        print("Your Pyrogram string session was saved in your saved messages.")
        return session_string

async def bcn():
    print("Please Choose an Option:")
    print("1. Generate Telethon Session")
    print("2. Generate Pyrogram V2 Session")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        telethon_session_result = await telethon_session()
        with open("telethon_session.txt", "w") as file:
            file.write(telethon_session_result)
    elif choice == "2":
        pyrogram_session_result = await pyrogram_session()
        with open("pyrogram_session.txt", "w") as file:
            file.write(pyrogram_session_result)
    else:
        print("🚫 Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    asyncio.run(bcn())
