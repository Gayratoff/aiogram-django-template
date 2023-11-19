from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware


if __name__ == "robot.middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
