from aiogram import Dispatcher

from tgbot_template.tgbot.templates.texts import *
from tgbot_template.tgbot.keyboards.inline_funds.all_funds import ikb_funds
from tgbot_template.tgbot.handlers.funds.choose_funds import *
from tgbot_template.tgbot.handlers.funds.first import *
from tgbot_template.tgbot.handlers.funds.second import *
from tgbot_template.tgbot.handlers.funds.third import *
from tgbot_template.tgbot.handlers.funds.fourth import *


async def choose_fund_type(message: types.Message):
    await message.answer('\n'.join([go_text]), reply_markup=ikb_funds)


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

    dp.register_callback_query_handler(choose_fund_fourth_type, text=funsd.get("fourth_fund_type").get("type_name"))
    dp.register_callback_query_handler(fourth_type_first_fund, text="fourth_fund_type:first_fund")
    dp.register_callback_query_handler(fourth_type_second_fund, text="fourth_fund_type:second_fund")
    dp.register_callback_query_handler(fourth_type_third_fund, text="fourth_fund_type:third_fund")

    dp.register_callback_query_handler(delete, text="обратно")
