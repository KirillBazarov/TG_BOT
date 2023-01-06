from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tgbot_template.tgbot.media.data import funsd
from tgbot_template.tgbot.keyboards.stepback import stepback_button
from aiogram.utils.callback_data import CallbackData

idk_third_type_get_name = CallbackData("third_fund_type", "fund_number")


ikb_third_type_funds = InlineKeyboardMarkup(row_width=0,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(
                                                        text=funsd.get("third_fund_type").get("first_fund").get("name"),
                                                        callback_data=idk_third_type_get_name.new(fund_number="first_fund")),
                                                ],
                                                [
                                                    stepback_button,
                                                ]
                                            ])

ikb_third_type_first_fund = InlineKeyboardMarkup(row_width=2,
                                                inline_keyboard=[
                                                    [
                                                        InlineKeyboardButton(
                                                            text=funsd.get("third_fund_type").get("first_fund").get(
                                                                "name"),
                                                            url=funsd.get("third_fund_type").get("first_fund").get(
                                                                "site")),
                                                    ],

                                                    [
                                                        stepback_button,
                                                    ]
                                                ])