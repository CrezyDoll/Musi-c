from pyrogram import Client, filters
from pyrogram.types import Message
from SankiMusic.utilities.config import LOG_GROUP_ID
from SankiMusic import bot


async def new_message(chat_id: int, message: str):
    await bot.send_message(chat_id=chat_id, text=message)


@bot.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.mention if message.from_user else "wine User"
        title = message.chat.title
        chat_id = message.chat.id
        wine = f"**ɴᴇᴡ ɢʀᴏᴜᴘ**\n\n**ɢʀᴏᴜᴘ ɪᴅ**: {chat_id} \n**ɢʀᴏᴜᴘ ɴᴀᴍᴇ**: {title} \n**ᴀᴅᴅᴇᴅ ʙʏ**: {added_by}"
        await new_message(LOG_GROUP_ID, wine)
