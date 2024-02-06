from pyrogram import Client, filters
from pyrogram.types import Message
from database import db

# Replace 'your_channel_username' with your channel username
force_channel_username = "Moviestudioabhi"

@Client.on_message(filters.private & filters.command(["start", "help"]))
async def force_subscribe_handler(client: Client, message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Check if the user is already subscribed
    if await db.is_user_subscribed(user_id):
        return

    # If not subscribed, prompt the user to join the channel
    await message.reply_text(
        f"Hey! To use this bot, you need to subscribe to our channel: @{force_channel_username}\n\n"
        "After subscribing, click the /start command again to access the bot's features."
    )

@Client.on_message(filters.private & filters.incoming & ~filters.command)
async def check_subscription(client: Client, message: Message):
    user_id = message.from_user.id

    # Check if the user is subscribed before processing other commands
    if not await db.is_user_subscribed(user_id):
        await message.reply_text("To use this bot, you need to subscribe to our channel first.")
        return
    # Continue processing other commands or logic here
    # ...
  
