from aiogram import Dispatcher
from aiogram.types import Message


async def user_start(message: Message):
    await message.reply("Сап, мне сказали сделать этого бота. Он тип покажет куда ты можешь задонить")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")

def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
