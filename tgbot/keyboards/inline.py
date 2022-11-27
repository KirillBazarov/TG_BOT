from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tgbot_template.tgbot.media.mongo import funsd

ikb_funds = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[[

                                     InlineKeyboardButton(text=funsd.get("first_fund_type").get("type_name"),
                                                          callback_data=funsd.get("first_fund_type").get(
                                                              "type_name")),
                                     InlineKeyboardButton(funsd.get("second_fund_type").get("type_name"),
                                                          callback_data=funsd.get("second_fund_type").get(
                                                              "type_name")), ],
                                 ])

ikb_first_type_funds = InlineKeyboardMarkup(row_width=2,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(
                                                        text=funsd.get("first_fund_type").get("first_fund").get("name"),
                                                        callback_data=funsd.get("first_fund_type").get(
                                                            "first_fund").get("name")),
                                                    InlineKeyboardButton(
                                                        text=(funsd.get("first_fund_type").get("second_fund").get(
                                                            "name")),
                                                        callback_data=(
                                                            funsd.get("first_fund_type").get("second_fund").get(
                                                                "name"))),
                                                ],
                                                [
                                                    InlineKeyboardButton(text="Обратно",
                                                                         callback_data="stepback"),
                                                ]
                                            ]
                                            )

ikb_second_type_funds = InlineKeyboardMarkup(row_width=2,
                                             inline_keyboard=[
                                                 [
                                                     InlineKeyboardButton(
                                                         text=funsd.get("second_fund_type").get("first_fund").get(
                                                             "name"),
                                                         callback_data=funsd.get("second_fund_type").get(
                                                             "first_fund").get(
                                                             "name")),
                                                     InlineKeyboardButton(
                                                         text=funsd.get("second_fund_type").get("second_fund").get(
                                                             "name"),
                                                         callback_data=funsd.get("second_fund_type").get(
                                                             "second_fund").get(
                                                             "name")),
                                                 ],
                                                 [
                                                     InlineKeyboardButton(text="Обратно",
                                                                          callback_data="stepback"),
                                                 ]
                                             ])

ikb_fist_type_first_fund = InlineKeyboardMarkup(row_width=2,
                                                inline_keyboard=[
                                                    [
                                                        InlineKeyboardButton(
                                                            text=funsd.get("first_fund_type").get("first_fund").get(
                                                                "name"),
                                                            url=funsd.get("first_fund_type").get("first_fund").get("site")),
                                                    ],
                                                    [
                                                        InlineKeyboardButton(text="Обратно",
                                                                             callback_data="stepback"),
                                                    ]
                                                ])

ikb_fist_type_second_fund = InlineKeyboardMarkup(row_width=2,
                                                 inline_keyboard=[
                                                     [
                                                         InlineKeyboardButton(
                                                             text=funsd.get("first_fund_type").get("second_fund").get(
                                                                 "info"),
                                                             url=funsd.get("first_fund_type").get("second_fund").get("site")),
                                                     ],
                                                     [
                                                         InlineKeyboardButton(text="Обратно",
                                                                              callback_data="stepback"),
                                                     ]
                                                 ])

ikb_second_type_first_fund = InlineKeyboardMarkup(row_width=2,
                                                  inline_keyboard=[
                                                      [
                                                          InlineKeyboardButton(
                                                              text=funsd.get("second_fund_type").get("first_fund").get(
                                                                  "name"),
                                                              url=funsd.get("second_fund_type").get("first_fund").get("site"))],
                                                      [
                                                          InlineKeyboardButton(text="Обратно",
                                                                               callback_data="stepback"),
                                                      ]
                                                  ])

ikb_second_type_second_fund = InlineKeyboardMarkup(row_width=2,
                                                   inline_keyboard=[
                                                       [
                                                           InlineKeyboardButton(
                                                               text=funsd.get("second_fund_type").get(
                                                                   "second_fund").get("name"),
                                                               url=funsd.get("second_fund_type").get("second_fund").get("site"))],
                                                       [
                                                           InlineKeyboardButton(text="Обратно",
                                                                                callback_data="stepback"),
                                                       ]
                                                   ])


