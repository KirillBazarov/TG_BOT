from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tgbot_template.tgbot.media.somelol import funsd

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
                                                                "info"),
                                                            callback_data="lol"),
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
                                                             callback_data="lol"),
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
                                                                  "info"),
                                                              callback_data="lol"), ],
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
                                                                   "second_fund").get("info"),
                                                               callback_data="lol"), ],
                                                       [
                                                           InlineKeyboardButton(text="Обратно",
                                                                                callback_data="stepback"),
                                                       ]
                                                   ])

urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Перейти в блог Skillbox', callback_data='https://skillbox.ru/media/code/')
urlButton2 = InlineKeyboardButton(text='Перейти к курсам Skillbox', callback_data='https://skillbox.ru/code/')
urlButton3 = InlineKeyboardButton(text='Обратно', callback_data='stepback')
urlkb.add(urlButton, urlButton2, urlButton3)
