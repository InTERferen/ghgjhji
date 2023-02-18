import os
import errno

from loguru import logger

SESSIONS_DIR = "sessions"  # Не менять


def check_sessions_folder():
    try:
        os.mkdir(SESSIONS_DIR)
        logger.info('Директория для сессий создана')
    except OSError as e:
        if e.errno == errno.EEXIST:
            logger.warning('Директория для сессий уже существует. Пропускаем...')
        else:
            logger.error('Не могу создать дерикторию для сессий')
            raise Exception


def get_sessions_list() -> list:
    check_sessions_folder()

    result = []
    for path in os.listdir(SESSIONS_DIR):
        if os.path.isfile(os.path.join(SESSIONS_DIR, path)):
            if path.endswith(".session"):
                result.append(SESSIONS_DIR + "/" + path)
    if not result:
        logger.error("Ни одной сесси не найдено")
        raise Exception

    return result
