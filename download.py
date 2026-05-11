from telethon import TelegramClient

api_id = 123456
api_hash = "your_api_hash"

chat = "username_or_chat_id"   # e.g. "mychannel" or -1001234567890
message_id = 123               # target message_id

client = TelegramClient("session", api_id, api_hash)

async def main():
    msg = await client.get_messages(chat, ids=message_id)

    if not msg:
        print("Message not found")
        return

    if not msg.media:
        print("No media in message")
        return

    path = await client.download_media(msg)
    print("Downloaded to:", path)

with client:
    client.loop.run_until_complete(main())
