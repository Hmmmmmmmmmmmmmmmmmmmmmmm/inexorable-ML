from logger1 import logger

def add(a,b):
    result = a+b
    logger.debug(f'Adding {a} + {b} = {result}')
    return result


def sub(a,b):
    result = a-b
    logger.debug(f'Substracting {a} - {b} = {result}')
    return result


def mul(a,b):
    result = a*b
    logger.debug(f'Multiplying {a} x {b} = {result}')
    return result


def div(a,b):
    try:
        result = a/b
        logger.debug(f'Dividing {a} / {b} = {result}')  
        return result
    except ZeroDivisionError:
        logger.debug(" Dividing with zero error!")
        return None