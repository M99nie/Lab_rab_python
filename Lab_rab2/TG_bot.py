import asyncio
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "6775460441:AAHtVP5F9VPnCmu7e7b76apiw8-iv0wNM04"

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Обработчики команд


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Преподаватели"), KeyboardButton(text="Расписание")],
        [KeyboardButton(text="Контакты"), KeyboardButton(text="О боте")],
        [KeyboardButton(text="Стипендия")]
    ],
    resize_keyboard=True
)

menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Меню↩️")]
    ],
    resize_keyboard=True
)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Привет, {html.bold(message.from_user.full_name)}!",
        reply_markup=main_keyboard
    )


# Обработчик для "Меню↩️"
@dp.message(lambda message: message.text == "Меню↩️")
async def back_to_menu(message: Message) -> None:
    await message.answer("Вы вернулись в меню.", reply_markup=main_keyboard)


@dp.message(lambda message: message.text == "Контакты")
async def contact_handler(message: Message) -> None:
    await message.answer("Ссылка на контакты", reply_markup=menu_button)


@dp.message(lambda message: message.text == "Расписание")
async def timetable_handler(message: Message) -> None:
    await message.answer("Актуальное расписание любой группы, аудитории и преподавателей можно узнать в приложении: ", reply_markup=menu_button)

@dp.message(lambda message: message.text == "О боте")
async def info_handler(message: Message) -> None:
    await message.answer("Я-бот, созданый для того, чтобы отвечать на ваши вопросы", reply_markup=menu_button)

@dp.message(lambda message: message.text == "Преподаватели")
async def teachers_handler(message: Message) -> None:
    await message.answer(
        "Информацию о преподавателях можно найти на сайте: \n Информацию о том, когда и какие пары у преподователя можно узнать в приложении: ", reply_markup=menu_button)

@dp.message(lambda message: message.text == "Стипендия")
async def stip_handler(message: Message) -> None:
    await message.answer("Если не учиться, стипендия составит: 0 рублей", reply_markup=menu_button)


# Запуск бота
async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
