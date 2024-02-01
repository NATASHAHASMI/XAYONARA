from pyrogram import Client, filters
import datetime
import time
from database.users_chats_db import db
from info import ADMINS
from utils import broadcast_messages, broadcast_messages_group
import asyncio

@Client.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)
async def broadcast_to_users(bot, message):
    users = await db.get_all_users()
    b_msg = message.reply_to_message
    status_message = await message.reply_text(text='Broadcasting your messages...')

    start_time = time.time()
    total_users = await db.total_users_count()
    done, blocked, deleted, failed, success = 0, 0, 0, 0, 0

    async for user in users:
        pti, sh = await broadcast_messages(int(user['id']), b_msg)
        if pti:
            success += 1
        elif pti is False:
            if sh == "Blocked":
                blocked += 1
            elif sh == "Deleted":
                deleted += 1
            elif sh == "Error":
                failed += 1
        done += 1

        if not done % 20:
            await status_message.edit(
                f"Broadcast in progress:\n\nTotal Users {total_users}\n"
                f"Completed: {done} / {total_users}\nSuccess: {success}\n"
                f"Blocked: {blocked}\nDeleted: {deleted}"
            )

    time_taken = datetime.timedelta(seconds=int(time.time() - start_time))
    await status_message.edit(
        f"Broadcast Completed:\nCompleted in {time_taken} seconds.\n\n"
        f"Total Users {total_users}\nCompleted: {done} / {total_users}\n"
        f"Success: {success}\nBlocked: {blocked}\nDeleted: {deleted}\nFailed: {failed}"
    )

@Client.on_message(filters.command("grp_broadcast") & filters.user(ADMINS) & filters.reply)
async def broadcast_to_groups(bot, message):
    groups = await db.get_all_chats()
    b_msg = message.reply_to_message
    status_message = await message.reply_text(text='Broadcasting your messages to groups...')

    start_time = time.time()
    total_groups = await db.total_chat_count()
    done, failed, success = 0, 0, 0

    async for group in groups:
        pti, sh = await broadcast_messages_group(int(group['id']), b_msg)
        if pti:
            success += 1
        elif sh == "Error":
            failed += 1
        done += 1

        if not done % 20:
            await status_message.edit(
                f"Broadcast in progress:\n\nTotal Groups {total_groups}\n"
                f"Completed: {done} / {total_groups}\nSuccess: {success}"
            )

    time_taken = datetime.timedelta(seconds=int(time.time() - start_time))
    await status_message.edit(
        f"Broadcast Completed:\nCompleted in {time_taken} seconds.\n\n"
        f"Total Groups {total_groups}\nCompleted: {done} / {total_groups}\n"
        f"Success: {success}\nFailed: {failed}"
    )
