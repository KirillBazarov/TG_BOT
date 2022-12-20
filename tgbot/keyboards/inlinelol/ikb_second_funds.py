from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tgbot_template.tgbot.media.data import funsd
from tgbot_template.tgbot.keyboards.inline import stepback_button
from aiogram.utils.callback_data import CallbackData

idk_second_type_get_name = CallbackData("second_fund_type", "fund_number")

ikb_second_type_funds = InlineKeyboardMarkup(row_width=0,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(
                                                        text=funsd.get("second_fund_type").get("first_fund").get("name"),
                                                        callback_data=idk_second_type_get_name.new(fund_number="first_fund")),
                                                    InlineKeyboardButton(
                                                        text=(funsd.get("second_fund_type").get("second_fund").get(
                                                            "name")),
                                                        callback_data=idk_second_type_get_name.new(fund_number="second_fund")),
                                                ],
                                                [
                                                    InlineKeyboardButton(
                                                        text=funsd.get("second_fund_type").get("third_fund").get("name"),
                                                        callback_data=idk_second_type_get_name.new(fund_number="third_fund")),
                                                    InlineKeyboardButton(
                                                        text=(funsd.get("second_fund_type").get("fourth_fund").get(
                                                            "name")),
                                                        callback_data=idk_second_type_get_name.new(fund_number="fourth_fund")),
                                                ],


                                                [
                                                    stepback_button,
                                                ]
                                            ])

ikb_second_type_first_fund = InlineKeyboardMarkup(row_width=2,
                                                inline_keyboard=[
                                                    [
                                                        InlineKeyboardButton(
                                                            text=funsd.get("second_fund_type").get("first_fund").get(
                                                                "name"),
                                                            url=funsd.get("second_fund_type").get("first_fund").get(
                                                                "site")),
                                                    ],

                                                    [
                                                        stepback_button,
                                                    ]
                                                ])

ikb_second_type_second_fund = InlineKeyboardMarkup(row_width=2,
                                                 inline_keyboard=[
                                                     [
                                                         InlineKeyboardButton(
                                                             text=funsd.get("second_fund_type").get("second_fund").get(
                                                                 "info"),
                                                             url=funsd.get("second_fund_type").get("second_fund").get(
                                                                 "site")),
                                                     ],
                                                     [
                                                         stepback_button,
                                                     ]
                                                 ])

ikb_second_type_third_fund = InlineKeyboardMarkup(row_width=2,
                                                 inline_keyboard=[
                                                     [
                                                         InlineKeyboardButton(
                                                             text=funsd.get("second_fund_type").get("third_fund").get(
                                                                 "info"),
                                                             url=funsd.get("second_fund_type").get("third_fund").get(
                                                                 "site")),
                                                     ],
                                                     [
                                                         stepback_button,
                                                     ]
                                                 ])

ikb_second_type_fourth_fund = InlineKeyboardMarkup(row_width=2,
                                                 inline_keyboard=[
                                                     [
                                                         InlineKeyboardButton(
                                                             text=funsd.get("second_fund_type").get("fourth_fund").get(
                                                                 "info"),
                                                             url=funsd.get("second_fund_type").get("fourth_fund").get(
                                                                 "site")),
                                                     ],
                                                     [
                                                         stepback_button,
                                                     ]
                                                 ])
