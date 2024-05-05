# Don't Remove Credit @VJ_Botz

# Subscribe YouTube Channel For Amazing Bot @Tech_VJ

# Ask Doubt on telegram @KingVJ01



# premium code is implemented by - @VJBots

# referal code credit - @VJBots



import os

import string

import time

import logging

import random

import asyncio

import time

import datetime

from Script import script

from pyrogram import Client, filters, enums

from pyrogram.errors import ChatAdminRequired, FloodWait

from pyrogram.types import *

from database.ia_filterdb import Media, get_file_details, unpack_new_file_id, get_bad_files

from database.users_chats_db import db, delete_all_referal_users, get_referal_users_count, get_referal_all_users, referal_add_user

from info import CHANNELS, ADMINS, SHORTLINK_MODE, PREMIUM_AND_REFERAL_MODE, STREAM_MODE, AUTH_CHANNEL, OWNER_USERNAME, REFERAL_PREMEIUM_TIME, REFERAL_COUNT, PAYMENT_TEXT, PAYMENT_QR, LOG_CHANNEL, PICS, BATCH_FILE_CAPTION, CUSTOM_FILE_CAPTION, PROTECT_CONTENT, CHNL_LNK, GRP_LNK, REQST_CHANNEL, SUPPORT_CHAT_ID, SUPPORT_CHAT, MAX_B_TN, VERIFY, SHORTLINK_API, SHORTLINK_URL, TUTORIAL, VERIFY_TUTORIAL, IS_TUTORIAL, URL

from utils import get_settings, pub_is_subscribed, get_size, is_subscribed, save_group_settings, temp, verify_user, check_token, check_verification, get_token, get_shortlink, get_tutorial, get_seconds

from database.connections_mdb import active_connection

# from plugins.pm_filter import ENABLE_SHORTLINK

import re, asyncio, os, sys

import json

import base64

from urllib.parse import quote_plus

from TechVJ.util.file_properties import get_name, get_hash, get_media_file_size

logger = logging.getLogger(__name__)



BATCH_FILES = {}



@Client.on_message(filters.command("start") & filters.incoming)

async def start(client, message):

    await message.react(emoji="🔥")

    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:

        buttons = [[

            InlineKeyboardButton('⤬ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ⤬', url=f'http://t.me/{temp.U_NAME}?startgroup=true')

        ],[

            InlineKeyboardButton('✪ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ', url="https://t.me/+-duU_vRUZzswZDY1"),

            InlineKeyboardButton('⌬ Mᴏᴠɪᴇ Gʀᴏᴜᴘ', url='https://t.me/Telugu_Movies_999')

        ],[

            InlineKeyboardButton('✇ Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ✇', url=CHNL_LNK)

        ]]

        reply_markup = InlineKeyboardMarkup(buttons)

        await message.reply(script.START_TXT.format(message.from_user.mention if message.from_user else message.chat.title, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup, disable_web_page_preview=True)

        await asyncio.sleep(2) # 😢 https://github.com/EvamariaTG/EvaMaria/blob/master/plugins/p_ttishow.py#L17 😬 wait a bit, before checking.

        if not await db.get_chat(message.chat.id):

            total=await client.get_chat_members_count(message.chat.id)

            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, "Unknown"))       

            await db.add_chat(message.chat.id, message.chat.title)

        return 

    if not await db.is_user_exist(message.from_user.id):

        await db.add_user(message.from_user.id, message.from_user.first_name)

        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))

    if len(message.command) != 2:

        if PREMIUM_AND_REFERAL_MODE == True:

            buttons = [[

                InlineKeyboardButton('⤬ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ⤬', url=f'http://t.me/{temp.U_NAME}?startgroup=true')

            ],[

                InlineKeyboardButton('Eᴀʀɴ Mᴏɴᴇʏ 💸', callback_data="shortlink_info"),

                InlineKeyboardButton('⌬ Mᴏᴠɪᴇ Gʀᴏᴜᴘ', url=GRP_LNK)

            ],[

                InlineKeyboardButton('〄 Hᴇʟᴘ', callback_data='help'),

                InlineKeyboardButton('⍟ Aʙᴏᴜᴛ', callback_data='about')

            ],[

                InlineKeyboardButton('🔻 ɢᴇᴛ ғʀᴇᴇ/ᴘᴀɪᴅ sᴜʙsᴄʀɪᴘᴛɪᴏɴ 🔻', callback_data='subscription')

            ],[

                InlineKeyboardButton('✇ Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ✇', url=CHNL_LNK)

            ]]

        else:

            buttons = [[

                InlineKeyboardButton('⤬ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ⤬', url=f'http://t.me/{temp.U_NAME}?startgroup=true')

            ],[

                InlineKeyboardButton('Eᴀʀɴ Mᴏɴᴇʏ 💸', callback_data="shortlink_info"),

                InlineKeyboardButton('⌬ Mᴏᴠɪᴇ Gʀᴏᴜᴘ', url=GRP_LNK)

            ],[

                InlineKeyboardButton('〄 Hᴇʟᴘ', callback_data='help'),

                InlineKeyboardButton('⍟ Aʙᴏᴜᴛ', callback_data='about')

            ],[

                InlineKeyboardButton('✇ Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ✇', url=CHNL_LNK)

            ]]

        reply_markup = InlineKeyboardMarkup(buttons)

        m=await message.reply_sticker("CAACAgUAAxkBAAEKVaxlCWGs1Ri6ti45xliLiUeweCnu4AACBAADwSQxMYnlHW4Ls8gQMAQ") 

        await asyncio.sleep(1)

        await m.delete()

        await message.reply_photo(

            photo=random.choice(PICS),

            caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),

            reply_markup=reply_markup,

            parse_mode=enums.ParseMode.HTML

        )

        return

    

    if AUTH_CHANNEL and not await is_subscribed(client, message):

        try:

            invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))

        except ChatAdminRequired:

            logger.error("Make sure Bot is admin in Forcesub channel")

            return

        btn = [

            [

                InlineKeyboardButton("❆ Jᴏɪɴ Oᴜʀ Cʜᴀɴɴᴇʟ ❆", url=invite_link.invite_link)

            ],[

                InlineKeyboardButton('🤔 Why Iam Join🤔', callback_data='sinfo')

            ]

        ]



        if message.command[1] != "subscribe":

            try:

                kk, file_id = message.command[1].split("_", 1)

                btn.append([InlineKeyboardButton("↻ Tʀʏ Aɢᴀɪɴ", callback_data=f"checksub#{kk}#{file_id}")])

            except (IndexError, ValueError):

                btn.append([InlineKeyboardButton("↻ Tʀʏ Aɢᴀɪɴ", url=f"https://t.me/{temp.U_NAME}?start={message.command[1]}")])

        await client.send_photo(

            chat_id=message.from_user.id,

            photo="https://telegra.ph/file/20b4aaaddb8aba646e53c.jpg",

            caption="**You are not in our channel given below so you don't get the movie file...\n\nIf you want the movie file, click on the '🍿ᴊᴏɪɴ ᴏᴜʀ ʙᴀᴄᴋ-ᴜᴘ ᴄʜᴀɴɴᴇʟ🍿' button below and join our back-up channel, then click on the '🔄 Try Again' button below...\n\nThen you will get the movie files...**",

            reply_markup=InlineKeyboardMarkup(btn),

            parse_mode=enums.ParseMode.MARKDOWN

            )

        return

    if len(message.command) == 2 and message.command[1] in ["subscribe", "error", "okay", "help"]:

        if PREMIUM_AND_REFERAL_MODE == True:

            buttons = [[

                InlineKeyboardButton('⤬ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ⤬', url=f'http://t.me/{temp.U_NAME}?startgroup=true')

            ],[

                InlineKeyboardButton('Eᴀʀɴ Mᴏɴᴇʏ 💸', callback_data="shortlink_info"),

                InlineKeyboardButton('⌬ Mᴏᴠɪᴇ Gʀᴏᴜᴘ', url=GRP_LNK)

            ],[

                InlineKeyboardButton('〄 Hᴇʟᴘ', callback_data='help'),

                InlineKeyboardButton('⍟ Aʙᴏᴜᴛ', callback_data='about')

            ],[

                InlineKeyboardButton('🔻 ɢᴇᴛ ғʀᴇᴇ/ᴘᴀɪᴅ sᴜʙsᴄʀɪᴘᴛɪᴏɴ 🔻', callback_data='subscription')

            ],[

                InlineKeyboardButton('✇ Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ✇', url=CHNL_LNK)

            ]]

        else:

            buttons = [[

                InlineKeyboardButton('⤬ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ⤬', url=f'http://t.me/{temp.U_NAME}?startgroup=true')

            ],[

                InlineKeyboardButton('Eᴀʀɴ Mᴏɴᴇʏ 💸', callback_data="shortlink_info"),

                InlineKeyboardButton('⌬ Mᴏᴠɪᴇ Gʀᴏᴜᴘ', url=GRP_LNK)

            ],[

                InlineKeyboardButton('〄 Hᴇʟᴘ', callback_data='help'),

                InlineKeyboardButton('⍟ Aʙᴏᴜᴛ', callback_data='about')

            ],[

                InlineKeyboardButton('✇ Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ✇', url=CHNL_LNK)

            ]]

        reply_markup = InlineKeyboardMarkup(buttons)      

        await message.reply_photo(

            photo=random.choice(PICS),

            caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),

            reply_markup=reply_markup,

            parse_mode=enums.ParseMode.HTML

        )

        return

    data = message.command[1]

    if data.split("-", 1)[0] == "VJ":

        user_id = int(data.split("-", 1)[1])

        vj = await referal_add_user(user_id, message.from_user.id)

        if vj and PREMIUM_AND_REFERAL_MODE == True:

            await message.reply(f"<b>You have joined using the referral link of user with ID {user_id}\n\nSend /start again to use the bot</b>")

            num_referrals = await get_referal_users_count(user_id)

            await client.send_message(chat_id = user_id, text = "<b>{} start the bot with your referral link\n\nTotal Referals - {}</b>".format(message.from_user.mention, num_referrals))

            if num_referrals == REFERAL_COUNT:

                time = REFERAL_PREMEIUM_TIME       

                seconds = await get_seconds(time)

                if seconds > 0:

                    expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)

                    user_data = {"id": user_id, "expiry_time": expiry_time} 

                    await db.update_user(user_data)  # Use the update_user method to update or insert user data

                    await delete_all_referal_users(user_id)

                    await client.send_message(chat_id = user_id, text = "<b>You Have Successfully Completed Total Referal.\n\nYou Added In Premium For {}</b>".format(REFERAL_PREMEIUM_TIME))

                    return 

        else:

            if PREMIUM_AND_REFERAL_MODE == True:

                buttons = [[

                    InlineKeyboardButton('⤬ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ⤬', url=f'http://t.me/{temp.U_NAME}?startgroup=true')

                ],[

                    InlineKeyboardButton('Eᴀʀɴ Mᴏɴᴇʏ 💸', callback_data="shortlink_info"),

                    InlineKeyboardButton('⌬ Mᴏᴠɪᴇ Gʀᴏᴜᴘ', url=GRP_LNK)

                ],[

                    InlineKeyboardButton('〄 Hᴇʟᴘ', callback_data='help'),

                    InlineKeyboardButton('⍟ Aʙᴏᴜᴛ', callback_data='about')

                ],[

                    InlineKeyboardButton('🔻 ɢᴇᴛ ғʀᴇᴇ/ᴘᴀɪᴅ sᴜʙsᴄʀɪᴘᴛɪᴏɴ 🔻', callback_data='subscription')

                ],[

                    InlineKeyboardButton('✇ Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ✇', url=CHNL_LNK)

                ]]

            else:

                buttons = [[

                    InlineKeyboardButton('⤬ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ⤬', url=f'http://t.me/{temp.U_NAME}?startgroup=true')

                ],[

                    InlineKeyboardButton('Eᴀʀɴ Mᴏɴᴇʏ 💸', callback_data="shortlink_info"),

                    InlineKeyboardButton('⌬ Mᴏᴠɪᴇ Gʀᴏᴜᴘ', url=GRP_LNK)

                ],[

                    InlineKeyboardButton('〄 Hᴇʟᴘ', callback_data='help'),

                    InlineKeyboardButton('⍟ Aʙᴏᴜᴛ', callback_data='about')

                ],[

                    InlineKeyboardButton('✇ Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ✇', url=CHNL_LNK)

                ]]

            reply_markup = InlineKeyboardMarkup(buttons)

            m=await message.reply_sticker("CAACAgUAAxkBAAEKVaxlCWGs1Ri6ti45xliLiUeweCnu4AACBAADwSQxMYnlHW4Ls8gQMAQ") 

            await asyncio.sleep(1)

            await m.delete()

            await message.reply_photo(

                photo=random.choice(PICS),

                caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),

                reply_markup=reply_markup,

                parse_mode=enums.ParseMode.HTML

            )

            return 

    try:

        pre, file_id = data.split('_', 1)

    except:

        file_id = data

        pre = ""

    if data.split("-", 1)[0] == "BATCH":

        sts = await message.reply("<b>Please wait...</b>")

        file_id = data.split("-", 1)[1]

        msgs = BATCH_FILES.get(file_id)

        if not msgs:

            file = await client.download_media(file_id)

            try: 

                with open(file) as file_data:

                    msgs=json.loads(file_data.read())

            except:

                await sts.edit("FAILED")

                return await client.send_message(LOG_CHANNEL, "UNABLE TO OPEN FILE.")

            os.remove(file)

            BATCH_FILES[file_id] = msgs



        filesarr = []

        for msg in msgs:

            title = msg.get("title")

            size=get_size(int(msg.get("size", 0)))

            f_caption=msg.get("caption", "")

            if BATCH_FILE_CAPTION:

                try:

                    f_caption=BATCH_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)

                except Exception as e:

                    logger.exception(e)

                    f_caption=f_caption

            if f_caption is None:

                f_caption = f"{title}"

            try:

                if STREAM_MODE == True:

                    # Create the inline keyboard button with callback_data

                    user_id = message.from_user.id

                    username =  message.from_user.mention 



                    log_msg = await client.send_cached_media(

                        chat_id=LOG_CHANNEL,

                        file_id=msg.get("file_id"),

                    )

                    fileName = {quote_plus(get_name(log_msg))}

                    stream = f"{URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"

                    download = f"{URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"

 

                    await log_msg.reply_text(

                        text=f"•• ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴇᴅ ꜰᴏʀ ɪᴅ #{user_id} \n•• ᴜꜱᴇʀɴᴀᴍᴇ : {username} \n\n•• ᖴᎥᒪᗴ Nᗩᗰᗴ : {fileName}",

                        quote=True,

                        disable_web_page_preview=True,

                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🚀 Fast Download 🚀", url=download),  # we download Link

                                                            InlineKeyboardButton('🖥️ Watch online 🖥️', url=stream)]])  # web stream Link

                    )

                if STREAM_MODE == True:

                    button = [[

                        InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ', url=f'https://t.me/{SUPPORT_CHAT}'),

                        InlineKeyboardButton('Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ', url=CHNL_LNK)

                    ],[

                        InlineKeyboardButton('𝗕𝗢𝗧 𝗢𝗪𝗡𝗘𝗥', url="https://t.me/arya_bro")

                    ],[

                        InlineKeyboardButton("🚀 Fast Download 🚀", url=download),  # we download Link

                        InlineKeyboardButton('🖥️ Watch online 🖥️', url=stream)

                    ]]

                else:

                    button = [[

                        InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ', url=f'https://t.me/{SUPPORT_CHAT}'),

                        InlineKeyboardButton('Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ', url=CHNL_LNK)

                    ],[

                        InlineKeyboardButton('𝗕𝗢𝗧 𝗢𝗪𝗡𝗘𝗥', url="https://t.me/arya_bro")

                    ]]

                msg = await client.send_cached_media(

                    chat_id=message.from_user.id,

                    file_id=msg.get("file_id"),

                    caption=f_caption,

                    protect_content=msg.get('protect', False),

                    reply_markup=InlineKeyboardMarkup(button)

                )

                filesarr.append(msg)

                

            except FloodWait as e:

                await asyncio.sleep(e.x)

                logger.warning(f"Floodwait of {e.x} sec.")

                msg = await client.send_cached_media(

                    chat_id=message.from_user.id,

                    file_id=msg.get("file_id"),

                    caption=f_caption,

                    protect_content=msg.get('protect', False),

                    reply_markup=InlineKeyboardMarkup(button)

                )

                filesarr.append(msg)

                k = await client.send_message(chat_id = message.from_user.id, text=f"<b><u>❗️❗️❗️IMPORTANT❗️️❗️❗️</u></b>\n\nThis Movie Files/Videos will be deleted in <b><u>10 mins</u> 🫥 <i></b>(Due to Copyright Issues)</i>.\n\n<b><i>Please forward this ALL Files/Videos to your Saved Messages and Start Download there</i></b>")

                await asyncio.sleep(600)

                for x in filesarr:

                    await x.delete()

                await k.edit_text("<b>Your All Files/Videos is successfully deleted!!!</b>")

            

            except Exception as e:

                logger.warning(e, exc_info=True)

                continue

            await asyncio.sleep(1) 

        await sts.delete()

        k = await client.send_message(chat_id = message.from_user.id, text=f"<b><u>❗️❗️❗️IMPORTANT❗️️❗️❗️</u></b>\n\nThis Movie Files/Videos will be deleted in <b><u>10 mins</u> 🫥 <i></b>(Due to Copyright Issues)</i>.\n\n<b><i>Please forward this ALL Files/Videos to your Saved Messages and Start Download there</i></b>")

        await asyncio.sleep(600)

        for x in filesarr:

            await x.delete()

        await k.edit_text("<b>Your All Files/Videos is successfully deleted!!!</b>")       

        

        return

    

    elif data.split("-", 1)[0] == "DSTORE":

        sts = await message.reply("<b>Please wait...</b>")

        b_string = data.split("-", 1)[1]

        decoded = (base64.urlsafe_b64decode(b_string + "=" * (-len(b_string) % 4))).decode("ascii")

        try:

            f_msg_id, l_msg_id, f_chat_id, protect = decoded.split("_", 3)

        except:

            f_msg_id, l_msg_id, f_chat_id = decoded.split("_", 2)

            protect = "/pbatch" if PROTECT_CONTENT else "batch"

        diff = int(l_msg_id) - int(f_msg_id)

        async for msg in client.iter_messages(int(f_chat_id), int(l_msg_id), int(f_msg_id)):

            if msg.media:

                media = getattr(msg, msg.media.value)

                if BATCH_FILE_CAPTION:

                    try:

                        f_caption=BATCH_FILE_CAPTION.format(file_name=getattr(media, 'file_name', ''), file_size=getattr(media, 'file_size', ''), file_caption=getattr(msg, 'caption', ''))

                    except Exception as e:

                        logger.exception(e)

                        f_caption = getattr(msg, 'caption', '')

                else:

                    media = getattr(msg, msg.media.value)

                    file_name = getattr(media, 'file_name', '')

                    f_caption = getattr(msg, 'caption', file_name)

                try:

                    await msg.copy(message.chat.id, caption=f_caption, protect_content=True if protect == "/pbatch" else False)

                except FloodWait as e:

                    await asyncio.sleep(e.x)

                    await msg.copy(message.chat.id, caption=f_caption, protect_content=True if protect == "/pbatch" else False)

                except Exception as e:

                    logger.exception(e)

                    continue

            elif msg.empty:

                continue

            else:

                try:

                    await msg.copy(message.chat.id, protect_content=True if protect == "/pbatch" else False)

                except FloodWait as e:

                    await asyncio.sleep(e.x)

                    await msg.copy(message.chat.
