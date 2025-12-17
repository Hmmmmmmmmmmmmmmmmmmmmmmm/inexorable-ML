import logging


for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
    
logging.basicConfig(
    filename='apps_tutorial_trial_1.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d ~ %H:%M:%S'
)
#log msg with different severity levels:
logging.debug('Debug msg')
logging.warning('warning msg')
logging.error('error msg')
logging.critical('critical msg')
logging.info('info msg')