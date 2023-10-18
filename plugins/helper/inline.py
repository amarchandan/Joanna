from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


buttons = [
    [
        InlineKeyboardButton(text="Gate", callback_data="gates"),
        InlineKeyboardButton(text="Tools", callback_data="toolss"),
    ],
    [
        InlineKeyboardButton(text="Group", url="https://t.me/Illegal_Carder"),
        InlineKeyboardButton(text="Channel", url="https://t.me/Illegal_Carder"),
        ],
    [
        InlineKeyboardButton(text="Premium", callback_data="premium_data"),
        ],
]
    
@Client.on_callback_query()
async def button_click(client, query):
    data = query.data
    chat_id = query.message.chat.id
    if data == "gates":
        await query.edit_message_text(
            """
Welcome to Joanna / Joanna Gateways Online
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Gates CMDS:  None Api Gates! ✅
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Gates auth: 0     |    Gates charge: 0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Select the type of gate you want for your use!.""",
            reply_markup=InlineKeyboardMarkup(
                [
                [
                InlineKeyboardButton("Auth", callback_data="_auth"),
                InlineKeyboardButton("Charge", callback_data="_charge"),
                ],
                [
                InlineKeyboardButton("CVV/CCN", callback_data="cvv_ccn"),
                InlineKeyboardButton("Back",callback_data="_back"),
                
                ],
                ]
            ),
        )
    elif data == "_auth":
        await query.edit_message_text(
            """
┏ Joanna Gateways Online | Auth Gateways  [P: 1 | 6] ┒
┠ Name :-
┠ Format :- 
┠ Condition :-
┠ Type :- Need-Credits

┠ Name :-
┠ Format :- 
┠ Condition :-
┠ Type :- Need-Credits

┠ Name :-
┠ Format :- 
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            """,
            reply_markup=InlineKeyboardMarkup(
                [
                [
                InlineKeyboardButton("Back", callback_data="_back"),
                ],
                ]
            ),
        )
    elif data == "_charge":
        await query.edit_message_text(
            "Charge Gate",
            reply_markup=InlineKeyboardMarkup(
                [
                [
                InlineKeyboardButton("Back", callback_data="_back"),
                ],
                ]
            ),
        )
    elif data == "_back":
        await query.edit_message_text(
            "Charge Gate",
            reply_markup=buttons
        )
    elif data == "cvv_ccn":
        await query.edit_message_text(
            "Cvv Ccn Gate",
            reply_markup=InlineKeyboardMarkup(
                [
                [
                InlineKeyboardButton("Back", callback_data="_back"),
                ],
                ]
            ),
        )