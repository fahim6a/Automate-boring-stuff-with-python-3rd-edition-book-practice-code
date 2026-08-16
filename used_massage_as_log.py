# we can store massage in file instead of showing in display once 

import logging
logging.basicConfig(filename='store_message.txt', level= logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

