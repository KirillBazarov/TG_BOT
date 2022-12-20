from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.utils.markdown import hcode
from tgbot_template.tgbot.keyboards.inlinelol.ikb_first_funds import ikb_first_type_funds, ikb_fist_type_first_fund, \
    ikb_fist_type_second_fund, ikb_fist_type_third_fund, ikb_fist_type_fourth_fund, ikb_fist_type_fifth_fund, \
    ikb_fist_type_sixth_fund, ikb_fist_type_seventh_fund, ikb_fist_type_eighth_fund

from tgbot_template.tgbot.keyboards.inlinelol.ikb_second_funds import ikb_second_type_funds,\
    ikb_second_type_first_fund ,ikb_second_type_second_fund, ikb_second_type_third_fund, ikb_second_type_fourth_fund

from tgbot_template.tgbot.keyboards.inlinelol.ikb_third_funds import ikb_third_type_funds, ikb_third_type_first_fund
from tgbot_template.tgbot.keyboards.inline import ikb_funds
from tgbot_template.tgbot.media.data import funsd


async def choose_fund_type(message: types.Message):
    text = [
        "Бот покажет куда ты можешь задонить.Вот пару направлений",
    ]
    await message.answer('\n'.join(text), reply_markup=ikb_funds)


async def choose_fund_fist_type(call: types.CallbackQuery):
    text = [
        f'так ты выбрал направление {funsd.get("first_fund_type").get("type_name")}, теперь выбирем сам фонд',
    ]
    await call.message.answer_photo(photo=funsd.get("first_fund_type").get("photo"), reply_markup=ikb_first_type_funds,
                                    caption='\n'.join(text))

async def fist_type_first_fund(call: types.CallbackQuery):
    text = funsd.get("first_fund_type").get("first_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_fist_type_first_fund)


async def fist_type_second_fund(call: types.CallbackQuery):
    text = funsd.get("first_fund_type").get("second_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_fist_type_second_fund)


async def fist_type_third_fund(call: types.CallbackQuery):
    text = funsd.get("first_fund_type").get("third_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_fist_type_third_fund)


async def fist_type_fourth_fund(call: types.CallbackQuery):
    text = funsd.get("first_fund_type").get("fourth_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_fist_type_fourth_fund)


async def fist_type_fifth_fund(call: types.CallbackQuery):
    text = funsd.get("first_fund_type").get("fifth_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_fist_type_fifth_fund)

async def fist_type_sixth_fund(call: types.CallbackQuery):
    text = funsd.get("first_fund_type").get("sixth_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_fist_type_sixth_fund)

async def fist_type_seventh_fund(call: types.CallbackQuery):
    text = funsd.get("first_fund_type").get("seventh_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_fist_type_seventh_fund)

async def fist_type_eighth_fund(call: types.CallbackQuery):
    text = funsd.get("first_fund_type").get("eighth_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_fist_type_eighth_fund)










async def choose_fund_second_type(call: types.CallbackQuery):
    text = [
        f'так ты выбрал направлению {funsd.get("second_fund_type").get("type_name")}, теперь выбирем сам фонд',
    ]
    await call.message.answer_photo(photo=funsd.get("second_fund_type").get("photo"),
                                    reply_markup=ikb_second_type_funds, caption='\n'.join(text))

async def second_type_first_fund(call: types.CallbackQuery):
    text = funsd.get("second_fund_type").get("first_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_second_type_first_fund)


async def second_type_second_fund(call: types.CallbackQuery):
    text = funsd.get("second_fund_type").get("second_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_second_type_second_fund)


async def second_type_third_fund(call: types.CallbackQuery):
    text = funsd.get("second_fund_type").get("third_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_second_type_third_fund)


async def second_type_fourth_fund(call: types.CallbackQuery):
    text = funsd.get("second_fund_type").get("fourth_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_second_type_fourth_fund)







async def choose_fund_third_type(call: types.CallbackQuery):
    text = [
        f'так ты выбрал направление {funsd.get("third_fund_type").get("type_name")}, теперь выбирем сам фонд',
    ]
    await call.message.answer_photo(photo=funsd.get("third_fund_type").get("photo"), reply_markup=ikb_third_type_funds,
                                    caption='\n'.join(text))

async def third_type_first_fund(call: types.CallbackQuery):
    text = funsd.get("third_fund_type").get("first_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_third_type_first_fund)





async def delete(call: types.CallbackQuery):
    await call.message.delete()


# хендлер если нужен bot
# async def my_handeler(message):
#     bot = message.bot
#     await bot.send_message(message.chat_id, "sup")


def register_echo(dp: Dispatcher):
    dp.register_message_handler(choose_fund_type, commands="go")

    dp.register_callback_query_handler(choose_fund_fist_type, text=funsd.get("first_fund_type").get("type_name"))
    dp.register_callback_query_handler(fist_type_first_fund, text="first_fund_type:first_fund")
    dp.register_callback_query_handler(fist_type_second_fund, text="first_fund_type:second_fund")
    dp.register_callback_query_handler(fist_type_third_fund, text="first_fund_type:third_fund")
    dp.register_callback_query_handler(fist_type_fourth_fund, text="first_fund_type:fourth_fund")
    dp.register_callback_query_handler(fist_type_fifth_fund, text="first_fund_type:fifth_fund")
    dp.register_callback_query_handler(fist_type_sixth_fund, text="first_fund_type:sixth_fund")
    dp.register_callback_query_handler(fist_type_seventh_fund, text="first_fund_type:seventh_fund")
    dp.register_callback_query_handler(fist_type_eighth_fund, text="first_fund_type:eighth_fund")



    dp.register_callback_query_handler(choose_fund_second_type, text=funsd.get("second_fund_type").get("type_name"))
    dp.register_callback_query_handler(second_type_first_fund, text="second_fund_type:first_fund")
    dp.register_callback_query_handler(second_type_second_fund, text="second_fund_type:second_fund")
    dp.register_callback_query_handler(second_type_third_fund, text="second_fund_type:third_fund")
    dp.register_callback_query_handler(second_type_fourth_fund, text="second_fund_type:fourth_fund")



    dp.register_callback_query_handler(choose_fund_third_type, text=funsd.get("third_fund_type").get("type_name"))
    dp.register_callback_query_handler(third_type_first_fund, text="third_fund_type:first_fund")

    dp.register_callback_query_handler(delete, text="обратно")
