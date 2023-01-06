from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tgbot_template.tgbot.media.data import funsd
from tgbot_template.tgbot.keyboards.stepback import stepback_button
from aiogram.utils.callback_data import CallbackData

idk_first_type_get_name = CallbackData("first_fund_type", "fund_number")

ikb_first_type_funds = InlineKeyboardMarkup(row_width=0,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(
                                                        text=funsd.get("first_fund_type").get("first_fund").get("name"),
                                                        callback_data=idk_first_type_get_name.new(
                                                            fund_number="first_fund")),
                                                    InlineKeyboardButton(
                                                        text=(funsd.get("first_fund_type").get("second_fund").get(
                                                            "name")),
                                                        callback_data=idk_first_type_get_name.new(
                                                            fund_number="second_fund")),
                                                ],
                                                [
                                                    InlineKeyboardButton(
                                                        text=funsd.get("first_fund_type").get("third_fund").get("name"),
                                                        callback_data=idk_first_type_get_name.new(
                                                            fund_number="third_fund")),
                                                    InlineKeyboardButton(
                                                        text=(funsd.get("first_fund_type").get("fourth_fund").get(
                                                            "name")),
                                                        callback_data=idk_first_type_get_name.new(
                                                            fund_number="fourth_fund")),
                                                ],
                                                [
                                                    InlineKeyboardButton(
                                                        text=funsd.get("first_fund_type").get("fifth_fund").get("name"),
                                                        callback_data=idk_first_type_get_name.new(
                                                            fund_number="fifth_fund")),
                                                    InlineKeyboardButton(
                                                        text=(funsd.get("first_fund_type").get("sixth_fund").get(
                                                            "name")),
                                                        callback_data=idk_first_type_get_name.new(
                                                            fund_number="sixth_fund")),
                                                ],
                                                [
                                                    InlineKeyboardButton(
                                                        text=funsd.get("first_fund_type").get("seventh_fund").get(
                                                            "name"),
                                                        callback_data=idk_first_type_get_name.new(
                                                            fund_number="seventh_fund")),
                                                    InlineKeyboardButton(
                                                        text=(funsd.get("first_fund_type").get("eighth_fund").get(
                                                            "name")),
                                                        callback_data=idk_first_type_get_name.new(
                                                            fund_number="eighth_fund")),
                                                ],
                                                [
                                                    stepback_button,
                                                ]
                                            ])

ikb_fist_type_first_fund = InlineKeyboardMarkup(row_width=2,
                                                inline_keyboard=[
                                                    [
                                                        InlineKeyboardButton(
                                                            text=funsd.get("first_fund_type").get("first_fund").get(
                                                                "name"),
                                                            url=funsd.get("first_fund_type").get("first_fund").get(
                                                                "site")),
                                                    ],

                                                    [
                                                        stepback_button,
                                                    ]
                                                ])

ikb_fist_type_second_fund = InlineKeyboardMarkup(row_width=2,
                                                 inline_keyboard=[
                                                     [
                                                         InlineKeyboardButton(
                                                             text=funsd.get("first_fund_type").get("second_fund").get(
                                                                 "info"),
                                                             url=funsd.get("first_fund_type").get("second_fund").get(
                                                                 "site")),
                                                     ],
                                                     [
                                                         stepback_button,
                                                     ]
                                                 ])

ikb_fist_type_third_fund = InlineKeyboardMarkup(row_width=2,
                                                inline_keyboard=[
                                                    [
                                                        InlineKeyboardButton(
                                                            text=funsd.get("first_fund_type").get("third_fund").get(
                                                                "info"),
                                                            url=funsd.get("first_fund_type").get("third_fund").get(
                                                                "site")),
                                                    ],
                                                    [
                                                        stepback_button,
                                                    ]
                                                ])

ikb_fist_type_fourth_fund = InlineKeyboardMarkup(row_width=2,
                                                 inline_keyboard=[
                                                     [
                                                         InlineKeyboardButton(
                                                             text=funsd.get("first_fund_type").get("fourth_fund").get(
                                                                 "info"),
                                                             url=funsd.get("first_fund_type").get("fourth_fund").get(
                                                                 "site")),
                                                     ],
                                                     [
                                                         stepback_button,
                                                     ]
                                                 ])

ikb_fist_type_fifth_fund = InlineKeyboardMarkup(row_width=2,
                                                inline_keyboard=[
                                                    [
                                                        InlineKeyboardButton(
                                                            text=funsd.get("first_fund_type").get("fifth_fund").get(
                                                                "info"),
                                                            url=funsd.get("first_fund_type").get("fifth_fund").get(
                                                                "site")),
                                                    ],
                                                    [
                                                        stepback_button,
                                                    ]
                                                ])

ikb_fist_type_sixth_fund = InlineKeyboardMarkup(row_width=2,
                                                inline_keyboard=[
                                                    [
                                                        InlineKeyboardButton(
                                                            text=funsd.get("first_fund_type").get("sixth_fund").get(
                                                                "info"),
                                                            url=funsd.get("first_fund_type").get("sixth_fund").get(
                                                                "site")),
                                                    ],
                                                    [
                                                        stepback_button,
                                                    ]
                                                ])

ikb_fist_type_seventh_fund = InlineKeyboardMarkup(row_width=2,
                                                  inline_ke9yboard=[
                                                      [
                                                          InlineKeyboardButton(
                                                              text=funsd.get("first_fund_type").get("seventh_fund").get(
                                                                  "info"),
                                                              url=funsd.get("first_fund_type").get("seventh_fund").get(
                                                                  "site")),
                                                      ],
                                                      [
                                                          stepback_button,
                                                      ]
                                                  ])

ikb_fist_type_eighth_fund = InlineKeyboardMarkup(row_width=2,
                                                 inline_keyboard=[
                                                     [
                                                         InlineKeyboardButton(
                                                             text=funsd.get("first_fund_type").get("eighth_fund").get(
                                                                 "info"),
                                                             url=funsd.get("first_fund_type").get("eighth_fund").get(
                                                                 "site")),
                                                     ],
                                                     [
                                                         stepback_button,
                                                     ]
                                                 ])
