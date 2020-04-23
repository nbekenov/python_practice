import logging
import logging.config
import time
from datetime import datetime

def my_logger():
    logging.config.fileConfig(fname='file.conf',disable_existing_loggers=False)
    logger = logging.getLogger('sampleLogger')
    logger.debug('this is a debug msg')
    logger.debug('this is a info msg')

if __name__ == '__main__':
    my_logger()
