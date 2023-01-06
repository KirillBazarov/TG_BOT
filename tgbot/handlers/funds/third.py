from aiogram import types

from tgbot_template.tgbot.keyboards.inline_funds.ikb_third_funds import ikb_third_type_first_fund
from tgbot_template.tgbot.media.data import funsd


async def third_type_first_fund(call: types.CallbackQuery):
    text = funsd.get("third_fund_type").get("first_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_third_type_first_fund)