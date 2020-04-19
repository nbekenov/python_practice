import logging

logging.basicConfig(
    level = logging.INFO,
    filename = 'app.log',
    filemode = 'w',
    format = '%(asctime)s - %(name)s - %(process)d - %(levelname)s - %(message)s'
)
logging.warning('This will get logged into the file')
logging.info('This an info msg')
# filemode by default : a - append
# level by default warning
