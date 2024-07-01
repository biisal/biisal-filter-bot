from pyrogram import Client, filters , enums
from info import ADMINS
import re
from database.users_chats_db import db

@Client.on_message(filters.command("set_muc") & filters.user(ADMINS))
async def set_muc_id(client, message):
    try:
        id = message.command[1]
        if id and str(id).startswith('-100') and len(str(id)) == 14:
            is_suc = await db.movies_update_channel_id(id)
            if is_suc:
                await message.reply("Successfully set movies update  channel id : " + id)
            else:
                await message.reply("Failed to set movies update channel id : " + id)
        else:
            await message.reply("Invalid channel id : " + id)
    except Exception as e:
        print('Err in set_muc_id', e)
        await message.reply("Failed to set movies channel id! Because : " + str(e))


@Client.on_message(filters.command("stream") & filters.user(ADMINS))
async def set_stream_link(client, message):
    try:
        link = message.command[1]
        if link:
            await db.set_stream_link(link)
            await message.reply("Successfully set stream link!")
        else:
            await message.reply("Usage: /stream https://t.me/bisal_files or http://t.me/bisal_files")
    except IndexError:
        await message.reply("Usage: /stream https://t.me/bisal_files or http://t.me/bisal_files")
        return


@Client.on_message(filters.command("del_stream") & filters.user(ADMINS))
async def del_stream_link(client, message):
    current_link =await db.get_stream_link()
    is_sure = await client.ask(message.chat.id, f"<b>Are you sure you want to delete this: <code>{current_link}</code> link ?\nReply with /yes or /no</b>", parse_mode=enums.ParseMode.HTML)
    if is_sure.text == "/no":
        return await message.reply("Stream link not deleted!")
    if is_sure.text == "/yes":
        if current_link:
            is_deleted = await db.del_stream_link()
            if is_deleted:
                return await message.reply(f"Successfully deleted This: {current_link} link!")
            else:
                return await message.reply("Stream link not found!\nOr something went wrong! Check logs")
        else:
            return await message.reply("Stream link not found!")
    else:
        return await message.reply("Invalid command!")
    
def checkIfLinkIsValid(link):
    if re.match(r'^https?://(?:www\.)?\S+$', link):
        return True
    else: return False
    
    
@Client.on_message(filters.command("m_grp") & filters.user(ADMINS))
async def m_grp(client, message):
    links = []
    link = await client.ask(message.chat.id ,"send me your pm search grp link or send /skiplink to skip , default is bisal_files")
    if link.text == "/skiplink":
        links.append("https://t.me/bisal_files")
    else:
        if checkIfLinkIsValid(link.text):
            links.append(link.text)
        else:
            await message.reply("Invalid link")
    link1 = await client.ask(message.chat.id ,"send me your movies grp link or send /skiplink to skip . default is bisal_files")
    if link1.text == "/skiplink":
        links.append("https://t.me/bisal_files")
    else:
        if checkIfLinkIsValid(link1.text):
            links.append(link1.text)
        else:
            await message.reply("Invalid link")
    ispm = await client.ask(message.chat.id ,"send 0 or 1")
    if ispm.text == "0" or ispm.text == "1":
        ispm = int(ispm.text)
    await message.reply(f'link1 : {links[0]}\nlink2 : {links[1]}')
    await db.get_set_grp_links(links=links , ispm=ispm)
    return await message.reply('done')
