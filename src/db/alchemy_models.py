from loguru import logger
from .alchemy import Base

try:  # Users/Employee Tables
    user = Base.classes.user


except Exception as err:
    logger.error("error while creating models - {}".format(err))
