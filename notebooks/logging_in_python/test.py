from logger import logging

def add(a,b):
    logging.debug('Addition op taking place')
    return a+b

logging.debug('add() being called')
add(10,100)