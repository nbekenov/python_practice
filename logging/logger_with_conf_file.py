import logging
import logging.config

logging.config.fileConfig(fname='file.conf',disable_existing_loggers=False)

logger = logging.getLogger(__name__)

logger.debug('this is a debug msg')
