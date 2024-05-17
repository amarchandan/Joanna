from datetime import datetime

from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = [
    [InlineKeyboardButton(text="Menu", callback_data="__main")],
    [
        InlineKeyboardButton(text="Add Me", url="https://t.me/JoannaChkBot?startgroup"),
    ],
]

buttons = [
    [
        InlineKeyboardButton(text="Gate", callback_data="gates"),
        InlineKeyboardButton(text="Tools", callback_data="_tool"),
    ],
    [
        InlineKeyboardButton(text="Join Channel", url="https://t.me/MorPhoChat"),
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
Welcome To Joanna Bot  |  {dt_string} 
━━━━━━━━━━━━━━━                                                                  
Hello This Is Beta Version telegram bot, gateways, tools and functions are constantly being added, to know my different commands use the buttons shown here.
━━━━━━━━━━━━━━━
Api Bot Status Is: ONLINE ✅ | Joanna Api Is ONLINE ✅ !
"""
gatebutton = [
    [
        InlineKeyboardButton("AUTH", callback_data="_authgate_"),
        InlineKeyboardButton("CHARGE", callback_data="_charge"),
    ],
    [
        InlineKeyboardButton("CC KILLER", callback_data="_cckiller_"),
    ],
    [
        InlineKeyboardButton("Back", callback_data="__back"),
    ],
]
gatetext = """
Welcome to Joanna / Joanna Gateways Online
━━━━━━━━━━━━━━━━━━━━━
Gates CMDS :  None Api Gates! ✅
━━━━━━━━━━━━━━━
Gates : 13 ✅
━━━━━━━━━━━━━━━━
Select the type of gate you want for your use!."""

mainback = """
Welcome back to Joanna Bot, it is a beta bot, gateways, tools and functions are constantly being added, to know my different commands use the buttons shown here
"""

premm = ""


@Client.on_callback_query()
async def button_click(client, query):
    data = query.data
    query.message.chat.id
    if data == "gates":
        await query.edit_message_text(
            text=gatetext,
            reply_markup=InlineKeyboardMarkup(gatebutton),
        )
    elif data == "__main":
        await query.edit_message_text(
            f"""
Welcome To Joanna Api Bot  |  {dt_string} 
━━━━━━━━━━━━━━━                                                                  
Hello This Is Beta Version telegram bot, gateways, tools and functions are constantly being added, to know my different commands use the buttons shown here.
━━━━━━━━━━━━━━━
Api Bot Status Is: Online ✅ | Joanna Api Is Online!
            """,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif data == "__back":
        await query.edit_message_text(
            text=mainback, reply_markup=InlineKeyboardMarkup(backbutton)
        )
    elif data == "__gback":
        await query.edit_message_text(
            text=backtext, reply_markup=InlineKeyboardMarkup(gatebutton)
        )
    elif data == "premium_data":
        await query.edit_message_text(
            text=premm,
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
┏ Joanna Gateways Online | Charge Gateways  [P: 1 | 3] ┒
┠ Name :- SHOPIFY $10
┠ Format :- /spt card|month|year|cvv
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :- SHOPIFY+STRIPE $10 
┠ Format :- /ssc card|month|year|cvv
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :- SHOPIFY+STRIPE $54 
┠ Format :- /ssc1 card|month|year|cvv
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :- STRIPE $76
┠ Format :- /sc card|month|year|cvv
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits
┗━━━━━━━━━━━━━━━━━━━━━━━━┛
            """,
            reply_markup=InlineKeyboardMarkup(gatebutton),
        )
    elif data == "_cckiller_":
        await query.edit_message_text(
            """
┏ Joanna Gateways Online | CC Killer Gateways  [P: 3 | 3] ┒
┠ Name :- CC KILLER
┠ Format :- /kill card|month|year|cvv
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits
┗━━━━━━━━━━━━━━━━━━━━━━━━┛
            """,
            reply_markup=InlineKeyboardMarkup(gatebutton),
        )
    elif data == "_authgate_":
        await query.edit_message_text(
            """
┏ Joanna Gateways Online | Auth Gateways  [P: 3 | 3] ┒
┠ Name :- STRIPE AUTH
┠ Format :- /sa card|month|year|cvv
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :- PAYPAL AUTH
┠ Format :- /pa card|month|year|cvv
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :- ADYEN AUTH
┠ Format :- /aa card|month|year|cvv
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :- BRAINTREE AUTH V2
┠ Format :- /pa card|month|year|cvv
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits
┗━━━━━━━━━━━━━━━━━━━━━━━━┛
            """,
            reply_markup=InlineKeyboardMarkup(gatebutton),
        )
    elif data == "_tool":
        await query.edit_message_text(
            """
┏ Joanna Tools / [P: 1 | 3] ┒
┠ Url info chk like Captcha, Cloud, Payment:
┠ Format: $/gate link
┠ Condition: Online! ✅

┠ Mass Url info chk like Captcha, Cloud, Payment:
┠ Format: $/mgate link
┠ Condition: Online! ✅

┠ CC Scr:
┠ Format: $scr Username Quantity 
┠ Condition: Online! ✅

┠ CC GENERATE:
┠ Format: $gen [BIN] [QUANTITY](OPTIONAL)
┠ Condition: Online! ✅

┠ IP Lookup:
┠ Format: $ip Your IP
┠ Condition: Online! ✅

┠ BIN Lookup:
┠ Format: $bin 601120 
┠ Condition: Online! ✅

┠ SK Lookup:
┠ Format: $sk SK_LIVE..... 
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
    elif data == "_tool2":
        await query.edit_message_text(
            """
┏ Joanna SK Cracking Tool / [P: 2 | 3] ┒
┠ Checkout Parse:
┠ Format: $/c Checkout_Link
┠ Condition: Online! ✅

┠ GEN ADDRESS BY ZIP::
┠ Format: $zip [ZIP CODE]
┠ Condition: Online! ✅

┠ RANDOM US ADDRESS:
┠ Format: $rnd 
┠ Condition: Online! ✅

┠ MASS SK CHK:
┠ Format: $masssk Reply To TxT File 
┠ Condition: Online! ✅

┠ GENERATE SK :
┠ Format: $gensk [QUANTITY] [SK LEN]
┠ Sk Len :- 1 - LONG SK ; 2 - MEDIUM SK ; 3 - SHORT SK
┠ Condition: Online! ✅

┠ IPV4 IPV6 GEN:
┠ Format: $ips [QUANTITY] ipv4|ipv6
┠ Condition: Online! ✅

┠ ASN IP SCR :
┠ Format: $asnip [QUANTITY] 
┠ Condition: Online! ✅
┗━━━━━━━━━━━━━━━━━━━━━━━━┛
            """,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Prev Page", callback_data="_tool"),
                        InlineKeyboardButton("Next Page", callback_data="_tool3"),
                    ],
                    [
                        InlineKeyboardButton("Back", callback_data="__back"),
                    ],
                ]
            ),
        )
    elif data == "_tool3":
        await query.edit_message_text(
            """
┏ Joanna SK Cracking Tool / [P: 3 | 3] ┒
┠ GEN RANDOM IP :
┠ Format: $genip [QUANTITY]
┠ Condition: Online! ✅

┠ DEBUG SCAN :
┠ Format: $debug Reply To TxT File 
┠ Condition: Online! ✅

┠ ENV SCAN :
┠ Format: $env Reply To TxT File
┠ Condition: Online! ✅

┠ DOMAIN TO IP CON :
┠ Format: $dip Reply To TxT File
┠ Condition: Online! ✅

┠ IP RANGE :
┠ Format: $range Start_Ip - End_Ip
┠ Condition: Online! ✅

┠ IP TO DOMAIN :
┠ Format: $rev Reply To TxT File
┠ Condition: Online! ✅
┗━━━━━━━━━━━━━━━━━━━━━━━━┛
            """,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Prev Page", callback_data="_tool2"),
                    ],
                    [
                        InlineKeyboardButton("Back", callback_data="__back"),
                    ],
                ]
            ),
        )
