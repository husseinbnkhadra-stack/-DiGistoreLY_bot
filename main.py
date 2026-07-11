from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '8529951592:AAGWQD_kvwKnI2lPWAP1ulKGZe6OtPsYhB0'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("أهلاً بك في متجر ALNiSi! البوت يعمل الآن بشكل صحيح.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
