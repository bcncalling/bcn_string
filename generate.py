import os
import asyncio
from pyrogram import Client
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

async def generate_telethon_session():
    api_id = 24414252
    api_hash = "247bc633310a5ce3dc8534c0d496197f"

    async with TelegramClient(StringSession(), api_id, api_hash) as client:
        print("Generating Telethon String Session...")
        session_string = client.session.save()
        await client.send_message("me", f"Your string session:\n`{session_string}`")
        print("Your Telethon string session was saved in your saved messages.")
        return session_string

async def generate_pyrogram_session():
    name = "BCN"
    api_id = 24414252
    api_hash = "247bc633310a5ce3dc8534c0d496197f"

    async with Client(
        name,
        api_id=api_id,
        api_hash=api_hash
    ) as app:
        print("Generating Pyrogram V2 String Session...")
        session_string = await app.export_session_string()
        await app.send_message("me", f"Your string session:\n`{session_string}`")
        print("Your Pyrogram string session was saved in your saved messages.")
        return session_string

async def init():
    print("Please Choose an Option:")
    print("1. Generate Telethon Session")
    print("2. Generate Pyrogram V2 Session")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        telethon_session = await generate_telethon_session()
        with open("telethon_session.txt", "w") as file:
            file.write(telethon_session)
    elif choice == "2":
        pyrogram_session = await generate_pyrogram_session()
        with open("pyrogram_session.txt", "w") as file:
            file.write(pyrogram_session)
    else:
        print("🚫 Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    asyncio.run(init())
