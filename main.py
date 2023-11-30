from aiogram import executor,types,Dispatcher,Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BOT_TOKEN = "6737669254:AAHOxhw36BmvXrBL3kFX6mcXWxyboWqsaLE"
bot = Bot(token=BOT_TOKEN,proxy='http://proxy.server:3128')
dp =Dispatcher(bot=bot)

@dp.message_handler(commands="start")
async def start(message:types.Message):
    await message.answer("hello")

@dp.message_handler(commands="help")
async def help(message:types.Message):
    await message.answer("sizga nima yordam kerak")


if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)

