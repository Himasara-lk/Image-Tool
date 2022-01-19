from szbot import sz
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery







START_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🌷 About 🌷", callback_data="aboutmenu"),
                    InlineKeyboardButton(" 🌸Help 🌸", callback_data="helpmenu")
                ],
                [
                    InlineKeyboardButton("☘ Updates ☘", url="https://t.me/Altex_Updates"),
                    InlineKeyboardButton("🌸 Support 🌸", url="https://t.me/SLStockMusic")
                ],
                [
                    InlineKeyboardButton("➕Add me to your group ➕", url="http://t.me/Hasindu_Image_Tool_BOT?startgroup=botstart") 
                ]
            ]
        )

GROUP_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🌷 Help 🌷", callback_data="helpmenu")
                ],
                [
                    InlineKeyboardButton("🙋‍♂️ Update channel", url="https://t.me/Altex_Updates")
                ]
            ]
        )

HELP_TEXT = f"""
**🌷 This is @Hasindu_Image_Tool_BOT Help Menu**

⚠️️Read this before useing me ...

♞/logo logo name 
♞/logohq logo name 
♞/rmbg reply to photo 
♞/edit reply to photo 
♞/carbon reply to text
♞/text reply to text
♞/rlogo logo name
"""

BACKTOHOME = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔙Back", callback_data="startmenu")
                ]
            ]
        )

ABOUT_TEXT = """
           💡Bright 
           🖼 Mixed 
           🔘 Black & White 
           ⚪️ Circle 
           🩸 Blur
           🔲 Border 
           🗯 Sticker 
           🔄 Rotate
           🌀 Contrast 
           🌇 Sepia 
           ✏️ Pencil 
           ⛄️ Cartoon
"""

CLOSE_BTN =  InlineKeyboardMarkup(
        [
        [
        InlineKeyboardButton(text="ʜᴀꜱɪɴᴅᴜ ʜɪᴍᴀꜱᴀʀᴀ </>", url=f"https://t.me/HASINDU_HIMASARA")    
        ]
        ]      
    )

FSUB_TEXT = " **You cant use me untill subscribe our updates channel** ☹️\n\n So Please join our updates channel by the following button and hit on the ` /start ` again 😊"

FSUB_BTN = InlineKeyboardMarkup(
        [
        [
        InlineKeyboardButton(text="🗣 Join our update Channel ", url=f"https://t.me/Altex_Updates") 
        ]
        ]      
    )

@sz.on_callback_query(filters.regex("startmenu"))
async def startmenu(_, query: CallbackQuery):
    await query.edit_message_text(START_TEXT,
        reply_markup=START_BTN,
     disable_web_page_preview=True
    )

@sz.on_callback_query(filters.regex("helpmenu"))
async def helpmenu(_, query: CallbackQuery):
    await query.edit_message_text(HELP_TEXT,
        reply_markup=BACKTOHOME,
     disable_web_page_preview=True
    )

@sz.on_callback_query(filters.regex("aboutmenu"))
async def aboutenu(_, query: CallbackQuery):
    await query.edit_message_text(ABOUT_TEXT,
        reply_markup=BACKTOHOME,
     disable_web_page_preview=True
    )

@sz.on_callback_query(filters.regex("closeit"))
async def close(_, query: CallbackQuery):
    await query.message.delete()        
