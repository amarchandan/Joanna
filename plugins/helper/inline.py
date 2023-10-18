from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from datetime import date
from datetime import datetime

buttons = [
    [
        InlineKeyboardButton(text="Gate", callback_data="gates"),
        InlineKeyboardButton(text="Tools", callback_data="_tool"),
    ],
    [
        InlineKeyboardButton(text="Group", url="https://t.me/Illegal_Carder"),
        InlineKeyboardButton(text="Channel", url="https://t.me/Illegal_Carder"),
        ],
    [
        InlineKeyboardButton(text="Premium", callback_data="premium_data"),
        ],
]

backbutton = [
    [
        InlineKeyboardButton(text="Gate", callback_data="gates"),
        InlineKeyboardButton(text="Tools", callback_data="_tool"),
    ],
    [
        InlineKeyboardButton(text="Premium", callback_data="premium_data"),
        ],
]

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
backtext = f"""
Welcome To Joanna Api Bot  |  {dt_string} 
━━━━━━━━━━━━━━━                                                                  
Hello This Is Beta Version telegram bot, gateways, tools and functions are constantly being added, to know my different commands use the buttons shown here.
━━━━━━━━━━━━━━━
Api Bot Status Is: Online ✅ | Joanna Api Is Online!
"""
gatebutton = [
                [
                InlineKeyboardButton("Auth", callback_data="_auth"),
                InlineKeyboardButton("Charge", callback_data="_charge"),
                InlineKeyboardButton("CVV/CCN", callback_data="cvv_ccn"),
                ],
                [
                InlineKeyboardButton("Back",callback_data="__back"),
                ],
                ]
gatetext = """
Welcome to Joanna / Joanna Gateways Online
━━━━━━━━━━━━━━━━━━━━━
Gates CMDS:  None Api Gates! ✅
━━━━━━━━━━━━━━━
Gates auth: 0     |    Gates charge: 0
━━━━━━━━━━━━━━━━
Select the type of gate you want for your use!."""

buttonscharge = [
                [
                InlineKeyboardButton("Back", callback_data="___back"),
                InlineKeyboardButton("Next Page", callback_data="_chargepg2"),
                ],
                ]

@Client.on_callback_query()
async def button_click(client, query):
    data = query.data
    chat_id = query.message.chat.id
    if data == "gates":
        await query.edit_message_text(
            text=gatetext,
            reply_markup=InlineKeyboardMarkup(gatebutton),
        )
    elif data == "__back":
        await query.edit_message_text(
            text=backtext,
            reply_markup=InlineKeyboardMarkup(backbutton)
        )
    elif data == "_auth":
        await query.edit_message_text(
            """
┏ Joanna Gateways Online | Auth Gateways  [P: 1 | 6] ┒
┠ Name :-
┠ Format :- 
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :-
┠ Format :- 
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :-
┠ Format :- 
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits
┗━━━━━━━━━━━━━━━━━━━━━━━━┛
            """,
            reply_markup=InlineKeyboardMarkup(
                [
                [
                InlineKeyboardButton("Back", callback_data="__back"),
                ],
                ]
            ),
        )
    elif data == "_charge":
        await query.edit_message_text(
            """
┏ Joanna Gateways Online | Charge Gateways  [P: 1 | 1] ┒
┠ Name :-
┠ Format :- 
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :-
┠ Format :- 
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :-
┠ Format :- 
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :-
┠ Format :- 
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :-
┠ Format :- 
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits
┗━━━━━━━━━━━━━━━━━━━━━━━━┛
            """,
            reply_markup=InlineKeyboardMarkup(buttonscharge),
        )
    elif data == "cvv_ccn":
        await query.edit_message_text(
            "Cvv Ccn Gate",
            reply_markup=InlineKeyboardMarkup(
                [
                [
                InlineKeyboardButton("Back", callback_data="__back"),
                ],
                ]
            ),
        )
    elif data == "_tool":
        await query.edit_message_text(
            """
┏ Joanna Tools / [P: 1 | 1] ┒
━━━━━━━━━━━━
┠ Bin Generator:
┠ Format: $gen 601120  
┠ Condition: Online! ✅
 ━━━━━━━━━━━━
┠ Sk Ckeck:
┠ Format: $sk sk_live 
┠ Condition: Online! ✅
 ━━━━━━━━━━━━
┠ BIN Lookup:
┠ Format: $bin 601120 
┠ Condition: Online! ✅
 ━━━━━━━━━━━━
┠ Gen Address:
┠ Format: $dir Country_code 
┠ Condition: Online! ✅
 ━━━━━━━━━━━━
┠ IP Fraud Check:
┠ Format: $ip 1.1.1.1 
┠ Condition: Online! ✅
┗━━━━━━━━━━━━━━━━━━━━━━━━┛
            """,
            reply_markup=InlineKeyboardMarkup(
                [
                [
                InlineKeyboardButton("Back", callback_data="__back"),
                InlineKeyboardButton("Next Page", callback_data="_tool2"),
                ],
                ]
            ),
        )