from aiogram import Router

import logging
import json
from messages.message import *

# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )


import logging
import json

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_obj = {
            'time': self.formatTime(record, self.datefmt),
            'name': record.name,
            'level': record.levelname,
            'message': record.getMessage(),
        }
        return json.dumps(log_obj, ensure_ascii=False)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('app.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

json_formatter = JsonFormatter()
file_handler.setFormatter(json_formatter)

logger.addHandler(file_handler)
# logger = logging.getLogger(__name__)


router = Router()


import importlib
import pkgutil

core_module_name = '.core'
core_module = importlib.import_module(core_module_name, package=__name__.rsplit('.', 1)[0])

routers = []

handler_module = importlib.import_module(f"{core_module_name}.handler", package=__name__.rsplit('.', 1)[0])
for _, handler_name, _ in pkgutil.iter_modules(handler_module.__path__):
    handler_module_instance = importlib.import_module(f"{core_module_name}.handler.{handler_name}", package=__name__.rsplit('.', 1)[0])
    if hasattr(handler_module_instance, 'router'):
        routers.append(handler_module_instance.router)

callback_module = importlib.import_module(f"{core_module_name}.callback", package=__name__.rsplit('.', 1)[0])
for _, callback_name, _ in pkgutil.iter_modules(callback_module.__path__):
    callback_module_instance = importlib.import_module(f"{core_module_name}.callback.{callback_name}", package=__name__.rsplit('.', 1)[0])
    if hasattr(callback_module_instance, 'router'):
        routers.append(callback_module_instance.router)


router.include_routers(*routers)
