import time
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("**You are very lucky 🤞 I am alive ❤️ Press /start to use me**")

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")

@Client.on_message(filters.command("PIFchannels"))
async def PIFchannels(_, message):
    # Define your inline keyboard buttons with the image link
    keyboard = [
        [
            InlineKeyboardButton("🍁 ʜᴅ ᴛᴇʟᴜɢᴜ ᴍᴏᴠɪᴇs 🎖️", url="https://t.me/+wIa9vb3tRho3N2Q1")
        ],
        [
            InlineKeyboardButton("🧞‍♀️ ʜɪɴᴅɪ - ᴍᴀʟᴀʏᴀʟᴀᴍ 🧐", url="https://t.me/+97U9EyGMz_s2YzQ1"),
            InlineKeyboardButton("🔔 ᴛᴀᴍɪʟ - ᴋᴀɴɴᴀᴅᴀ 🤖", url="https://t.me/+a3-YTIF0zsFhMDc1")
        ],
        [
            InlineKeyboardButton("🔥 ʜᴏʟʟʏᴡᴏᴏᴅ - ᴅᴜʙʙᴇᴅ 🎉", url="https://t.me/+9Ks800pBuq9kMmNl"),
            InlineKeyboardButton("🙂 ᴡᴇʙ - sᴇʀɪᴇs ✨", url="https://t.me/+YcesJaZ8gwUyMTc1")
        ],
        [
            InlineKeyboardButton("🥵 ʀᴀʀᴇ ʜɪᴅᴅᴇɴ ᴍᴏᴠɪᴇꜱ ♥️", url="https://t.me/PIFRareHiddenMovies")
        ],
        [
            InlineKeyboardButton("☀️ ᴅᴠᴅ - ᴅᴀᴛᴀʙᴀsᴇ 🌚", url="https://t.me/PIFOficials"),
            InlineKeyboardButton("🌿 ʜᴅ - ᴅᴀᴛᴀʙᴀsᴇ 💧", url="https://t.me/PIFOficial")
        ],
        [
            InlineKeyboardButton("🔗 ʙᴏᴛᴢ ᴀʀᴇᴀ ⚙", url="https://t.me/BoTzUpdates0"),
            InlineKeyboardButton("🥵 ᴏɴʟʏ ᴀᴅᴜʟᴛꜱ 🙈", url="https://t.me/Pakkinte_Anty_Bitlu")
        ],
        [
            InlineKeyboardButton("⪦ ᴍᴏᴠɪᴇs ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ ⪧", url="https://t.me/+37-TDCcQqltlOTRl")
        ]
    ]

    # Set the image link as the url for the InlineKeyboardButton
    keyboard[0][0].thumb_url = "https://imgshare.xyz/img/2/6651a6e179b1dc5cfdbab1ba/20240525_142144.jpg"
    
    # Create the reply markup with the modified keyboard
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the message with the inline keyboard
    sent_message = await message.reply_text(
        text="""**🙃 __Welcome To My PanindiaFilmZ Community!! Cheak Our Channels & Groups List Below!!**__

__**He'llo .. I Am PanindiaFilmZ Admin, I Can Provide My Channels Invite links** __

**__✨  Deals 24/7 :- 
@Killer_Loot_Deals __**

**__✨ Rare Hidden Adult Movies 2.0 
@Telugu_Adults_Rare_Hidden_Movies__**

__**Target - Reaching ur Self 🎯**__

__**For Any Queries - @PanIndia_Flimz_Admin_bot**__

__**@PanindiaFilmZ 🔥**__""",
        reply_markup=reply_markup
    )
    
    # Delete the message after 10 seconds
    await asyncio.sleep(10)
    await sent_message.delete()
