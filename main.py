from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

TOKEN = "8529951592:AAH8ToZc__XkiCV8AKAke5vOYM1yM4SVqPE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_main_menu():
    buttons = [
        [InlineKeyboardButton(text="شراء 🌸", callback_data="buy")],
        [InlineKeyboardButton(text="سجل المشتريات 💿", callback_data="history"), 
         InlineKeyboardButton(text="الملف الشخصي 👤", callback_data="profile")],
        [InlineKeyboardButton(text="المحفظة 👛", callback_data="wallet")],
        [InlineKeyboardButton(text="الدعم 💬", callback_data="support")],
        [InlineKeyboardButton(text="رابط VIP الخاص بك 🔗", callback_data="vip_link")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# معالجة الضغط على الأزرار
@dp.callback_query()
async def callback_handler(callback: types.CallbackQuery):
    if callback.data == "buy":
        await callback.message.answer("لقد اخترت 'شراء'. يرجى إرسال اسم المنتج الذي تود شراءه.")
    elif callback.data == "support":
        await callback.message.answer("للتحدث مع الدعم الفني، يرجى كتابة استفسارك هنا وسنقوم بالرد عليك في أقرب وقت.")
    elif callback.data == "wallet":
        await callback.message.answer("رصيد محفظتك حالياً: 0.00$")
    else:
        await callback.answer("تم الضغط على الزر بنجاح!")
    
    # لإغلاق حالة التحميل في الزر
    await callback.answer()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    text = "🌸 أهلاً بك في متجر DigiPlus، استخدم القائمة أدناه لاستكشاف منتجاتنا:"
    await message.answer(text, reply_markup=get_main_menu())

async def main():
    await dp.start_polling(bot)

await main()