import logging
#setting up the log
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d ~ %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler() #with this we can see 
        #what is being logged via stdout()/console
    ]
)
logger = logging.getLogger("Arthematic_App")