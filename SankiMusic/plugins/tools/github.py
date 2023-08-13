import os
from requests import get
from pyrogram import filters
from SankiMusic import bot


@bot.on_message(filters.command(['git', 'github']))
async def git(_, message):
    if len(message.command) < 2:
        return await message.reply_text("gime github username")
    user = message.text.split(None, 1)[1]
    res = get(f'https://api.github.com/users/{user}').json()
    data = f"""**Name**: {res['name']}
**ᴜsᴇʀɴᴀᴍᴇ**: {res['login']}
**ʟɪɴᴋ**: [{res['login']}]({res['html_url']})
**ʙɪᴏ**: {res['bio']}
**ᴄᴏᴍᴘᴀɴʏ**: {res['company']}
**ʙʟᴏɢ**: {res['blog']}
**ʟᴏᴄᴀᴛɪᴏɴ**: {res['location']}
**ᴘᴜʙʟɪᴄ ʀᴇᴘᴏs**: {res['public_repos']}
**ғᴏʟʟᴏᴡᴇʀs**: {res['followers']}
**ғᴏʟʟᴏᴡɪɴɢ**: {res['following']}
**ᴀᴄᴄ ᴄʀᴇᴀᴛᴇᴅ**: {res['created_at']}
"""
    with open(f"{user}.jpg", "wb") as f:
        kek = get(res['avatar_url']).content
        f.write(kek)

    await message.reply_photo(f"{user}.jpg", caption=data)
    os.remove(f"{user}.jpg")
     
