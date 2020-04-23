import logging
import time
from datetime import datetime

time = datetime.now()
file_out = time.strftime("%Y-%m-%d %H:%M:%S") + ".log"
logging.basicConfig(
    level = logging.INFO,
    filename = file_out,
    filemode = 'w',
    format = '%(asctime)s - %(name)s - %(process)d - %(levelname)s - %(message)s'
)
logging.warning('This will get logged into the file')
logging.info('This an info msg')
# filemode by default : a - append
# level by default warning
