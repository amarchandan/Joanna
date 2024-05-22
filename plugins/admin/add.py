from pyrogram import Client, filters

gc = -1002045361761


@Client.on_message(filters.command("add"))
async def cmd_add(Client, message):
    user_id = str(message.from_user.id)
    CEO = "1778110596"
    GROUP = open("plugins/group.txt").read().splitlines()
    if user_id != CEO:
        resp = "Require Owner Privilages ⚠️"
        await message.reply_text(resp, message.id)
    else:
        chat_add = message.text[len("/add ") :]
        if len(chat_add) == 0:
            chat_id = str(message.chat.id)
        else:
            chat_id = message.text[len("/add ") :]
        groupid = chat_id
        if groupid in GROUP:
            resp = f"""
Group (<code>{groupid}</code>) Is Already Authorized ⚠️.
      """
            await message.reply_text(resp, message.id)
        else:
            with open("plugins/group.txt", "a") as f:
                f.write(f"{groupid}\n")
            resp = f"""
Group (<code>{groupid}</code>) Is Now Authorized ✅.
      """
            await message.reply_text(resp, message.id)


@Client.on_message(filters.command("add1"))
async def cmd_ad1d(Client, message):
    user_id = str(message.from_user.id)
    CEO = "6697282163"
    GROUP = open("plugins/group.txt").read().splitlines()
    if user_id != CEO:
        resp = "Require Owner Privilages ⚠️"
        await message.reply_text(resp, message.id)
    else:
        chat_add = message.text[len("/add ") :]
        if len(chat_add) == 0:
            chat_id = str(message.chat.id)
        else:
            chat_id = message.text[len("/add ") :]
        groupid = chat_id
        if groupid in GROUP:
            resp = f"""
Group (<code>{groupid}</code>) Is Already Authorized ⚠️.
      """
            await message.reply_text(resp, message.id)
        else:
            with open("plugins/group.txt", "a") as f:
                f.write(f"{groupid}\n")
            resp = f"""
Group (<code>{groupid}</code>) Is Now Authorized ✅.
      """
            await message.reply_text(resp, message.id)
