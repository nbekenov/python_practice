import logging
logging.basicConfig(
    level = logging.ERROR,
    filename = 'app_exception.log',
    filemode = 'w',
    format = '%(asctime)s - %(name)s - %(process)d - %(levelname)s - %(message)s'
)

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  logging.error("Exception occurred", exc_info=True)
