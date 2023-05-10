#!/usr/bin/env python3
# logger helper function
# @author: Abdur R. Fayjie
# @email. fayjie92@gmail.com
# @date: 18-02-2023, Sat


import logging
import os
import time

def create_logger():
    # define log file
    log_file = os.path.join('./logs', 'logging-{}.log'.format(time.strftime("%Y%m%d_%H%M%S", time.localtime())))
    # make log director/file if does not exists
    if not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    log_format = "[%(asctime)s  %(levelname)s  %(filename)s  line %(lineno)d  %(process)d]  %(message)s"
    handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(handler)

    logging.basicConfig(level=logging.DEBUG, format=log_format, filename=log_file)  # filename: build a FileHandler
    logger.info("************************ Start Logging ************************")
    
    return logger


def logger_as_print():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    log_format = "%(message)s"
                      
    logging.basicConfig(level=logging.INFO, format=log_format)

    return logger