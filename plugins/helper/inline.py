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
        await query.message.reply(
            caption="Choose Gates",
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
        await query.message.reply(
            "Auth Gate",
            reply_markup=InlineKeyboardMarkup(
                [
                [
                InlineKeyboardButton("Back", callback_data="_back"),
                ],
                ]
            ),
        )
    elif data == "_charge":
        await query.message.reply(
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
        await query.message.reply(
            "Charge Gate",
            reply_markup=buttons
        )
    elif data == "cvv_ccn":
        await query.message.reply(
            "Cvv Ccn Gate",
            reply_markup=InlineKeyboardMarkup(
                [
                [
                InlineKeyboardButton("Back", callback_data="_back"),
                ],
                ]
            ),
        )