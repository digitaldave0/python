from ast import Return
from asyncio.log import logger
from dataclasses import dataclass
from importlib.resources import path
from locale import D_T_FMT
import logging
import time

#
logging.basicConfig(filename= "/tmp/test.log",
                    level = logging.DEBUG)
logger = logging.getLogger()

def read_files(path):
  start_time=time.time()
  try:
        f = open(path, mode="rb")
        data = f.read()
        return data
  except FileNotFoundError as err:
        logger.error(err)
        raise
  else:
        f.close()
  finally:
        stop_time = time.time()
        logger.info("time logged for {file} = {time}".format(file=path,time=D_T_FMT))

data = read_files("/home/dave/Pictures/Screenshot from 2021-02-01 21-28-03.png")
