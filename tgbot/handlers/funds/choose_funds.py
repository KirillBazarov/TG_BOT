from aiogram import types

from tgbot_template.tgbot.keyboards.inline_funds.ikb_first_funds import ikb_first_type_funds
from tgbot_template.tgbot.keyboards.inline_funds.ikb_fourth_funds4 import ikb_fourth_type_funds
from tgbot_template.tgbot.keyboards.inline_funds.ikb_second_funds import ikb_second_type_funds
from tgbot_template.tgbot.keyboards.inline_funds.ikb_third_funds import ikb_third_type_funds
from tgbot_template.tgbot.media.data import funsd
from tgbot_template.tgbot.templates.texts import tm_for_napravlenie


async def choose_fund_fist_type(call: types.CallbackQuery):
    text = [tm_for_napravlenie.render(napravlenie=funsd.get("third_fund_type").get("type_name"))]
    await call.message.answer_photo(photo=funsd.get("first_fund_type").get("photo"),
                                    reply_markup=ikb_first_type_funds,
                                    caption='\n'.join(text))


async def choose_fund_second_type(call: types.CallbackQuery):
    text = [tm_for_napravlenie.render(napravlenie=funsd.get("second_fund_type").get("type_name"))]
    await call.message.answer_photo(photo=funsd.get("second_fund_type").get("photo"),
                                    reply_markup=ikb_second_type_funds, caption='\n'.join(text))


async def choose_fund_third_type(call: types.CallbackQuery):
    text = [tm_for_napravlenie.render(napravlenie=funsd.get("third_fund_type").get("type_name"))]
    await call.message.answer_photo(photo=funsd.get("third_fund_type").get("photo"), reply_markup=ikb_third_type_funds,
                                    caption='\n'.join(text))


async def choose_fund_fourth_type(call: types.CallbackQuery):
    text = [tm_for_napravlenie.render(napravlenie=funsd.get("fourth_fund_type").get("type_name"))]
    await call.message.answer_photo(photo=funsd.get("fourth_fund_type").get("photo"),
                                    reply_markup=ikb_fourth_type_funds,
                                    caption='\n'.join(text))
